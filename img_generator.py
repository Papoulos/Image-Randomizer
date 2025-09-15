import random
import requests
import json
import time
import os
import psutil
import subprocess
import datetime
import argparse
import base64
import websocket
import uuid
from urllib.parse import urlparse

# Import configuration and prompts
from config import (
    SAVE_DIR, OL_models, Prompt_list, OLLAMA_PORT, MAX_RETRIES, TIMEOUT,
    SDXL_CONFIG, FLUX_CONFIG, COMFYUI_URL, COMFYUI_OUTPUT_DIR, IMAGE_TIMEOUT
)
from prompts import generate_random_prompt

# =======================
# Process Management
# =======================

def is_process_running(name):
    for proc in psutil.process_iter(attrs=['pid', 'name']):
        if name.lower() in proc.info['name'].lower():
            return True
    return False

def is_server_alive(url):
    try:
        response = requests.get(url, timeout=5)
        return response.status_code == 200
    except requests.RequestException:
        return False

def kill_ollama():
    for proc in psutil.process_iter(attrs=['pid', 'name']):
        if "ollama" in proc.info['name'].lower():
            proc.kill()

def start_ollama():
    if is_server_alive(f"http://127.0.0.1:{OLLAMA_PORT}"):
        return True

    if not is_process_running("ollama"):
        print("🚀 Démarrage d'Ollama...")
        subprocess.Popen(["ollama", "serve"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        time.sleep(5)

    for _ in range(MAX_RETRIES):
        if is_server_alive(f"http://127.0.0.1:{OLLAMA_PORT}"):
            print("✅ Ollama est en ligne !")
            return True
        time.sleep(2)

    print("❌ Échec du démarrage d'Ollama.")
    return False

# =======================
# Prompt & LoRA Generation (Ollama)
# =======================

def call_ollama(prompt_template, input_data):
    """Generic function to call Ollama LLM."""
    if not start_ollama(): return None
    
    command = ["ollama", "run", OL_models[0]]
    if isinstance(input_data, tuple):
        full_prompt = prompt_template.format(*input_data)
    else:
        full_prompt = prompt_template.format(input_data)

    try:
        process = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, encoding="utf-8")
        output, error = process.communicate(input=full_prompt, timeout=60)
        if process.returncode == 0:
            return output.strip()
        else:
            print(f"❌ Erreur Ollama : {error}")
            return None
    except subprocess.TimeoutExpired:
        print("⚠️ Timeout: Ollama a mis trop de temps à répondre.")
        process.kill()
        return None

def generate_prompt_only(base_prompt):
    """Generates a detailed prompt without LoRA syntax."""
    prompt_template = """Vous êtes un expert en création de prompts pour les IA génératives d'images comme Stable Diffusion XL. Votre objectif est de transformer une description de scène simple en un prompt riche, structuré et efficace. Le prompt doit être clair, visuellement évocateur et optimisé pour une génération d'image de haute qualité.

Vous recevrez une description de base contenant des éléments clés (sujet, action, lieu, etc.).

Suivez impérativement ces règles pour créer le prompt final :

1.  **Structure du Prompt :**
    *   Le prompt final doit être un bloc de texte unique, **en anglais**, composé de segments descriptifs séparés par des virgules. Ne formez pas une seule longue phrase grammaticale.
    *   Organisez le prompt dans cet ordre logique :
        1.  **Sujet et Action :** Commencez par le sujet principal et son action.
        2.  **Description Détaillée :** Décrivez les détails importants du sujet (vêtements, apparence, expression).
        3.  **Décor et Environnement :** Décrivez la scène, l'arrière-plan et les éléments contextuels.
        4.  **Ambiance et Éclairage :** Ajoutez des mots-clés pour l'ambiance (mood), la lumière (lighting) et la composition.
        5.  **Style Artistique :** Terminez **toujours** par le style (ex: `photorealistic`, `oil painting`, `anime style`, `cinematic`).

2.  **Mise en Emphase :**
    *   Identifiez le **sujet principal** et/ou l'**action clé**. Mettez-le(s) en emphase en l'entourant de parenthèses avec un poids entre `1.4` et `1.6`. N'appliquez ce poids qu'à 1 ou 2 éléments maximum.
    *   Exemple : `(a beautiful warrior princess:1.5), (fighting a dragon:1.4)`.

3.  **Enrichissement Créatif :**
    *   Injectez **un ou deux détails créatifs et cohérents** qui ne sont pas dans la description initiale. Ces ajouts doivent enrichir la scène (ex: un détail sur la météo, un objet en arrière-plan, une texture particulière).

4.  **Contraintes de Qualité et Format :**
    *   Soyez descriptif mais **concis**. Visez une longueur totale de **40 à 80 mots**.
    *   Utilisez des mots-clés forts et visuels. Évitez les descriptions vagues.
    *   Le prompt doit être une seule chaîne de caractères, sans retour à la ligne.
    *   Ne produisez **que** le prompt final. N'ajoutez aucune explication, introduction, commentaire ou excuse.

Traitez la description suivante :
{}"""
    return call_ollama(prompt_template, base_prompt)

def select_lora_with_llm(prompt, config):
    """Selects the most appropriate LoRA for a given prompt."""
    all_loras = list(set(lora for loras in config["lora_themes"].values() for lora in loras))
    if not all_loras: return None

    prompt_template = 'From the following list, which LoRA is most thematically appropriate for the prompt below? Respond with ONLY the name of the LoRA.\n\nLoRA List: {1}\n\nPrompt: "{0}"'
    return call_ollama(prompt_template, (prompt, all_loras))

# =======================
# ComfyUI API Interaction
# =======================

def update_workflow(workflow_data, config, prompt, lora_name):
    """Robustly updates the ComfyUI API workflow dictionary."""
    prompt_node_id = config["prompt_node_id"]
    lora_node_id = config["lora_node_id"]

    # Update the prompt text in the specified node
    if prompt_node_id in workflow_data:
        workflow_data[prompt_node_id]["inputs"]["text"] = prompt
        print(f"✅ Prompt injecté dans le noeud {prompt_node_id}.")
    else:
        print(f"❌ Erreur: Noeud de prompt ID '{prompt_node_id}' non trouvé dans le workflow.")

    # Update the LoRA name in the specified node, if a LoRA is provided
    if lora_name and lora_node_id in workflow_data:
        workflow_data[lora_node_id]["inputs"]["lora_name"] = lora_name
        print(f"✅ LoRA '{lora_name}' injecté dans le noeud {lora_node_id}.")
    elif lora_name:
        # This case handles when a lora_name is available but the node ID is not found
        print(f"❌ Erreur: Noeud de LoRA ID '{lora_node_id}' non trouvé dans le workflow.")

    return workflow_data

def queue_prompt(json_filename):
    """Queues a prompt on the ComfyUI server using curl."""
    json_filepath = os.path.join("jsons", json_filename)

    if not os.path.exists(json_filepath):
        print(f"❌ Erreur: Fichier workflow '{json_filepath}' non trouvé.")
        return None

    command = [
        "curl",
        "-X", "POST",
        "--silent",
        "--data", f"@{json_filepath}",
        f"{COMFYUI_URL}/prompt"
    ]

    try:
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            check=True,
            timeout=30,
            encoding='utf-8'
        )
        response_json = json.loads(result.stdout)
        prompt_id = response_json.get('prompt_id')
        if prompt_id:
            print(f"✅ Prompt mis en file d'attente avec l'ID : {prompt_id}")
            return prompt_id
        else:
            print(f"❌ Erreur: 'prompt_id' non trouvé dans la réponse de ComfyUI.")
            print(f"Réponse complète: {result.stdout}")
            return None
    except subprocess.CalledProcessError as e:
        print(f"❌ Erreur lors de l'appel curl à ComfyUI.")
        print(f"Stderr: {e.stderr}")
        if e.stdout:
            print(f"Stdout: {e.stdout}")
        return None
    except subprocess.TimeoutExpired:
        print("⚠️ Timeout: curl a mis trop de temps à répondre.")
        return None
    except json.JSONDecodeError:
        print(f"❌ Erreur de décodage JSON. Réponse de ComfyUI: {result.stdout}")
        return None
    except Exception as e:
        print(f"❌ Une erreur inattendue est survenue avec curl: {e}")
        return None

def listen_on_websocket(ws, prompt_id):
    """Listens on an existing websocket for generation to complete."""
    print("⏳ Attente de la fin de la génération sur le websocket...")
    start_time = time.time()
    try:
        while time.time() - start_time < IMAGE_TIMEOUT:
            try:
                ws.settimeout(2.0)
                out = ws.recv()
                if isinstance(out, str):
                    message = json.loads(out)
                    if message['type'] == 'executed':
                        data = message['data']
                        if data['prompt_id'] == prompt_id:
                            print("✅ Génération terminée.")
                            return True
                    elif message['type'] == 'executing':
                        data = message['data']
                        if data['prompt_id'] == prompt_id and data.get('node') is None:
                            print("✅ Fin de la file d'attente de génération.")
                            return True
            except websocket.WebSocketTimeoutException:
                continue
            except json.JSONDecodeError:
                print("⚠️ Message websocket non-JSON reçu, ignoré.")
                continue
    except Exception as e:
        print(f"❌ Erreur durant l'écoute du websocket: {e}")
        return False

    print("❌ Timeout: La génération n'a pas été confirmée à temps via websocket.")
    return False

# =======================
# File Saving
# =======================

def save_json_workflow(workflow_data, filename, client_id):
    """Saves the workflow JSON to the 'jsons' directory with a given filename."""
    JSON_SAVE_DIR = "jsons"
    if not os.path.exists(JSON_SAVE_DIR):
        os.makedirs(JSON_SAVE_DIR)

    file_path = os.path.join(JSON_SAVE_DIR, filename)

    try:
        api_payload = {"prompt": workflow_data, "client_id": client_id}
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(api_payload, f, indent=4, ensure_ascii=False)
        print(f"✅ JSON workflow sauvegardé à : {file_path}")
    except Exception as e:
        print(f"❌ Erreur de sauvegarde du JSON: {e}")

# =======================
# Main Generation Loop
# =======================

def main_generation_loop(config, num_iterations):
    """The main unified generation loop."""
    parsed_url = urlparse(COMFYUI_URL)
    server_address = parsed_url.netloc

    for i in range(1, num_iterations + 1):
        print(f"\n--- Itération {i}/{num_iterations} ---")

        # Establish websocket connection
        client_id = str(uuid.uuid4())
        ws = websocket.WebSocket()
        ws_url = f"ws://{server_address}/ws?clientId={client_id}"

        try:
            ws.connect(ws_url)

            # 1. Generate unique filenames for this iteration
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            base_filename = f"generated_{timestamp}"
            json_filename = f"{base_filename}.json"
            image_filename = f"{base_filename}.png"

            # 2. Load workflow template
            with open(config['workflow_file'], 'r', encoding='utf-8-sig') as f:
                workflow_wrapper = json.load(f)
            workflow = workflow_wrapper.get("prompt")
            if not workflow:
                print(f"❌ Erreur: Le fichier workflow '{config['workflow_file']}' ne semble pas être au format API correct.")
                continue

            # 3. Generate prompt
            base_prompt, _ = generate_random_prompt()
            prompt = generate_prompt_only(base_prompt)
            if not prompt:
                print("⚠️ Impossible de générer un prompt, passage à l'itération suivante.")
                continue
            print(f"📝 Prompt: {prompt[:100]}...")

            # 4. Select LoRA
            lora = select_lora_with_llm(prompt, config)
            if not lora:
                print("⚠️ Impossible de sélectionner un LoRA.")
            else:
                print(f"🎨 LoRA: {lora}")

            # 5. Update workflow
            updated_workflow = update_workflow(workflow, config, prompt, lora)

            # 6. Save JSON workflow BEFORE queuing
            save_json_workflow(updated_workflow, json_filename, client_id)

            # 7. Queue prompt for generation
            prompt_id = queue_prompt(json_filename)

            # 8. Wait for generation to complete on the existing websocket
            if prompt_id:
                generation_completed = listen_on_websocket(ws, prompt_id)
                if not generation_completed:
                    print("⚠️ La confirmation de la génération a échoué ou a expiré, passage à l'itération suivante.")
                    continue

        except Exception as e:
            print(f"❌ Une erreur majeure est survenue dans la boucle de génération : {e}")
            continue # Continue to the next iteration
        finally:
            # Ensure the websocket is always closed
            if ws.connected:
                ws.close()

# =======================
# Entry Point
# =======================
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Générateur d'images unifié via ComfyUI.")
    parser.add_argument("--flux", action="store_true", help="Utiliser le workflow Flux au lieu de SDXL.")
    parser.add_argument("--iterations", type=int, default=10, help="Nombre d'itérations de génération.")
    args = parser.parse_args()

    active_config = FLUX_CONFIG if args.flux else SDXL_CONFIG
    model_type = "Flux" if args.flux else "SDXL"

    print(f"🚀 Démarrage du générateur d'images en mode {model_type} via ComfyUI.")

    main_generation_loop(active_config, args.iterations)
