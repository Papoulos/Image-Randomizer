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
    # NOTE: This function requires the 'ollama' executable to be in the system's PATH.
    if is_server_alive(f"http://127.0.0.1:{OLLAMA_PORT}"):
        return True

    if not is_process_running("ollama"):
        print("🚀 Démarrage d'Ollama...")
        try:
            subprocess.Popen(["ollama", "serve"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            time.sleep(5)
        except FileNotFoundError:
            print("❌ Erreur: La commande 'ollama' est introuvable. Veuillez l'installer et vous assurer qu'elle est dans votre PATH.")
            return False

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
    """
    Selects the most appropriate LoRA for a given prompt using an LLM,
    then finds the exact matching filename.
    """
    all_loras = list(set(lora for loras in config["lora_themes"].values() for lora in loras))
    if not all_loras:
        return None

    # Ask the LLM for a suggestion
    prompt_template = 'From the following list, which LoRA is most thematically appropriate for the prompt below? Respond with ONLY the name of the LoRA.\n\nLoRA List: {1}\n\nPrompt: "{0}"'
    llm_suggestion = call_ollama(prompt_template, (prompt, all_loras))

    if not llm_suggestion:
        print("⚠️ Le LLM n'a pas suggéré de LoRA.")
        return None

    # Clean up the suggestion
    # Remove common extensions and surrounding quotes
    suggestion_clean = llm_suggestion.replace(".safetensors", "").replace(".safetensor", "").strip().strip('"')

    print(f"🧠 Suggestion du LLM pour le LoRA : '{llm_suggestion}' (nettoyé : '{suggestion_clean}')")

    # Find potential matches
    # We look for filenames that contain the cleaned suggestion
    possible_matches = [lora for lora in all_loras if suggestion_clean.lower() in lora.lower()]

    # Check for a unique match
    if len(possible_matches) == 1:
        found_lora = possible_matches[0]
        print(f"✅ LoRA trouvé par correspondance unique : {found_lora}")
        return found_lora
    elif len(possible_matches) > 1:
        print(f"⚠️ Ambiguïté : La suggestion '{suggestion_clean}' correspond à plusieurs LoRAs : {possible_matches}. Aucun LoRA ne sera utilisé.")
        return None
    else:
        print(f"❌ Aucun LoRA correspondant à la suggestion '{suggestion_clean}' n'a été trouvé. Aucun LoRA ne sera utilisé.")
        return None

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
    """Queues a prompt on the ComfyUI server using the requests library."""
    json_filepath = os.path.join("jsons", json_filename)

    if not os.path.exists(json_filepath):
        print(f"❌ Erreur: Fichier workflow '{json_filepath}' non trouvé.")
        return None

    try:
        with open(json_filepath, 'r', encoding='utf-8') as f:
            prompt_data = json.load(f)

        headers = {'Content-Type': 'application/json'}
        response = requests.post(f"{COMFYUI_URL}/prompt", json=prompt_data, headers=headers, timeout=30)
        response.raise_for_status() # Lève une exception pour les codes d'erreur HTTP

        response_json = response.json()
        prompt_id = response_json.get('prompt_id')

        if prompt_id:
            print(f"✅ Prompt mis en file d'attente avec l'ID : {prompt_id}")
            return prompt_id
        else:
            print(f"❌ Erreur: 'prompt_id' non trouvé dans la réponse de ComfyUI.")
            print(f"Réponse complète: {response.text}")
            return None

    except requests.exceptions.RequestException as e:
        print(f"❌ Erreur lors de la communication avec le serveur ComfyUI: {e}")
        return None
    except json.JSONDecodeError:
        print(f"❌ Erreur de décodage JSON en lisant '{json_filepath}'.")
        return None
    except Exception as e:
        print(f"❌ Une erreur inattendue est survenue: {e}")
        return None

def get_image_from_websocket(prompt_id, all_node_ids):
    """
    Connects to the ComfyUI WebSocket, waits for generation to complete by tracking
    all nodes, fetches the result via HTTP, and returns the image data.
    """
    client_id = str(uuid.uuid4())
    ws_url = f"ws://{COMFYUI_URL.split('//')[1]}/ws?clientId={client_id}"

    print(f"📡 Connexion au WebSocket : {ws_url}")
    ws = websocket.WebSocket()
    try:
        ws.connect(ws_url)
        print("✅ Connexion WebSocket établie.")
    except Exception as e:
        print(f"❌ Erreur de connexion WebSocket : {e}")
        return None

    start_time = time.time()
    finished_nodes = set()
    total_nodes = len(all_node_ids)

    try:
        while True:
            elapsed_time = time.time() - start_time
            if elapsed_time > IMAGE_TIMEOUT:
                print("❌ Timeout: La génération de l'image a dépassé le temps imparti.")
                break # Exit loop to try fetching history anyway

            try:
                ws.settimeout(2.0)
                out_str = ws.recv()
            except websocket.WebSocketTimeoutException:
                continue
            except websocket.WebSocketConnectionClosedException:
                print("❌ La connexion WebSocket a été fermée prématurément.")
                break

            if isinstance(out_str, str):
                message = json.loads(out_str)
                msg_type = message.get('type')
                data = message.get('data', {})

                if data.get('prompt_id') != prompt_id:
                    continue # Ignore messages from other prompts

                if msg_type == 'executed':
                    node_id = data.get('node')
                    if node_id and node_id not in finished_nodes:
                        finished_nodes.add(node_id)
                        print(f"✅ Nœud terminé : {node_id} ({len(finished_nodes)}/{total_nodes})")

                elif msg_type == 'execution_cached':
                    cached_nodes = data.get('nodes', [])
                    for node_id in cached_nodes:
                        if node_id not in finished_nodes:
                            finished_nodes.add(node_id)
                            print(f"✅ Nœud (cache) : {node_id} ({len(finished_nodes)}/{total_nodes})")

                elif msg_type == 'progress':
                    value = data.get('value', 0)
                    max_val = data.get('max', 0)
                    if max_val > 0:
                        print(f"⏳ Progression : {value}/{max_val} ({(value/max_val)*100:.1f}%)")

                # Check for completion
                if len(finished_nodes) >= total_nodes:
                    print("🏁 Tous les nœuds ont été exécutés.")
                    break

    except Exception as e:
        print(f"❌ Une erreur est survenue pendant la communication WebSocket: {e}")
    finally:
        if ws.connected:
            ws.close()
            print("🔌 Connexion WebSocket fermée.")

    # After execution finishes, get the image from history
    print("📋 Récupération de l'historique...")
    try:
        history_url = f"{COMFYUI_URL}/history/{prompt_id}"
        time.sleep(1) # Give ComfyUI a moment to write the history
        response = requests.get(history_url)
        response.raise_for_status()
        history = response.json()

        if prompt_id not in history:
            print(f"❌ Erreur: ID de prompt '{prompt_id}' non trouvé dans l'historique.")
            return None

        prompt_history = history[prompt_id]
        outputs = prompt_history.get('outputs', {})
        for node_id in outputs:
            if 'images' in outputs[node_id]:
                for img_info in outputs[node_id]['images']:
                    if img_info['type'] == 'output':
                        img_path = os.path.join(COMFYUI_OUTPUT_DIR, img_info.get('subfolder', ''), img_info['filename'])
                        time.sleep(1)
                        if os.path.exists(img_path):
                            print(f"✅ Image trouvée : {img_path}")
                            with open(img_path, 'rb') as f:
                                return f.read()
                        else:
                            print(f"❌ Erreur : Fichier image non trouvé : {img_path}")
                            return None

        print("❌ Aucune image de type 'output' trouvée dans l'historique.")
        return None

    except requests.RequestException as e:
        print(f"❌ Erreur lors de la récupération de l'historique : {e}")
        return None
    except Exception as e:
        print(f"❌ Une erreur inattendue est survenue lors du traitement de l'historique : {e}")
        return None

# =======================
# File Saving
# =======================

def save_json_workflow(workflow_data, filename):
    """Saves the workflow JSON to the 'jsons' directory with a given filename."""
    JSON_SAVE_DIR = "jsons"
    if not os.path.exists(JSON_SAVE_DIR):
        os.makedirs(JSON_SAVE_DIR)

    file_path = os.path.join(JSON_SAVE_DIR, filename)

    try:
        api_payload = {"prompt": workflow_data}
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
    for i in range(1, num_iterations + 1):
        print(f"\n--- Itération {i}/{num_iterations} ---")

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
        save_json_workflow(updated_workflow, json_filename)

        # 7. Queue prompt for generation
        prompt_id = queue_prompt(json_filename)

        # 8. Get the image (path is printed by get_image_from_websocket)
        if prompt_id:
            # The keys of the workflow dictionary are the node IDs
            node_ids = list(updated_workflow.keys())
            image_data = get_image_from_websocket(prompt_id, node_ids)
            if image_data:
                # Optionnel : Sauvegarder l'image localement si nécessaire
                # Par exemple, en utilisant le `image_filename` généré plus tôt
                save_path = os.path.join(SAVE_DIR, image_filename)
                try:
                    with open(save_path, 'wb') as f:
                        f.write(image_data)
                    print(f"🖼️  Image finale sauvegardée dans le script à : {save_path}")
                except Exception as e:
                    print(f"❌ Erreur lors de la sauvegarde de l'image finale : {e}")

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
