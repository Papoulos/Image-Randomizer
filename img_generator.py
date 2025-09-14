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

def queue_prompt(workflow):
    """Queues a prompt on the ComfyUI server."""
    payload = {"prompt": workflow}
    try:
        response = requests.post(f"{COMFYUI_URL}/prompt", json=payload)
        response.raise_for_status()
        return response.json()['prompt_id']
    except requests.RequestException as e:
        print(f"❌ Erreur lors de l'envoi à ComfyUI: {e}")
        return None

def get_image(prompt_id):
    """Polls the ComfyUI history and retrieves the generated image."""
    print("⏳ En attente de la génération de l'image par ComfyUI...")
    # Poll for IMAGE_TIMEOUT seconds max
    for _ in range(IMAGE_TIMEOUT // 2):
        try:
            res = requests.get(f"{COMFYUI_URL}/history/{prompt_id}")
            res.raise_for_status()
            history = res.json()
            if prompt_id in history and history[prompt_id].get('outputs'):
                outputs = history[prompt_id]['outputs']
                for node_id in outputs:
                    if 'images' in outputs[node_id]:
                        img_info = outputs[node_id]['images'][0]
                        img_path = os.path.join(COMFYUI_OUTPUT_DIR, img_info.get('subfolder', ''), img_info['filename'])
                        print(f"✅ Image trouvée : {img_path}")
                        if os.path.exists(img_path):
                            with open(img_path, 'rb') as f:
                                return f.read()
                return None # Still processing
            time.sleep(2)
        except requests.RequestException as e:
            print(f"❌ Erreur de connexion à ComfyUI : {e}")
            return None
    print("❌ Timeout: L'image n'a pas été générée à temps.")
    return None

# =======================
# File Saving
# =======================

def save_image(image_data, filename_prefix):
    """Saves image data to the specified save directory."""
    if not os.path.exists(SAVE_DIR):
        os.makedirs(SAVE_DIR)
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{filename_prefix}_{timestamp}.png"
    image_path = os.path.join(SAVE_DIR, filename)
    try:
        with open(image_path, 'wb') as f:
            f.write(image_data)
        print(f"✅ Image sauvegardée à : {image_path}")
    except Exception as e:
        print(f"❌ Erreur de sauvegarde: {e}")

# =======================
# Main Generation Loop
# =======================

def main_generation_loop(config, num_iterations):
    """The main unified generation loop."""
    for i in range(1, num_iterations + 1):
        print(f"\n--- Itération {i}/{num_iterations} ---")

        # 1. Load workflow template
        with open(config['workflow_file'], 'r', encoding='utf-8-sig') as f:
            workflow_wrapper = json.load(f)

        # The API format wraps the workflow in a "prompt" key. We need to extract it.
        workflow = workflow_wrapper.get("prompt")
        if not workflow:
            print(f"❌ Erreur: Le fichier workflow '{config['workflow_file']}' ne semble pas être au format API correct (clé 'prompt' manquante).")
            continue

        # 2. Generate prompt
        base_prompt, _ = generate_random_prompt()
        prompt = generate_prompt_only(base_prompt)
        if not prompt:
            print("⚠️ Impossible de générer un prompt, passage à l'itération suivante.")
            continue
        print(f"📝 Prompt: {prompt[:100]}...")

        # 3. Select LoRA
        lora = select_lora_with_llm(prompt, config)
        if not lora:
            print("⚠️ Impossible de sélectionner un LoRA.")
        else:
            print(f"🎨 LoRA: {lora}")

        # 4. Update workflow and queue for generation
        updated_workflow = update_workflow(workflow, config, prompt, lora)
        prompt_id = queue_prompt(updated_workflow)
        
        # 5. Get and save the image
        if prompt_id:
            image_data = get_image(prompt_id)
            if image_data:
                save_image(image_data, "generated")
        
        time.sleep(5)

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
