import random
import requests
import json
import time
import os
import gc
import ollama
import base64
import psutil
import subprocess
import datetime
import argparse

# Import configuration and prompts
from config import (
    SAVE_DIR, OL_models, Prompt_list, LORA_THEMES, UTILITY_LORAS,
    OLLAMA_PORT, MAX_RETRIES, TIMEOUT, SDXL_CONFIG, FLUX_CONFIG
)
from prompts import generate_random_prompt

# =======================
# Vérification des processus
# =======================

def is_process_running(name):
    """Vérifie si un processus est actif par son nom"""
    for proc in psutil.process_iter(attrs=['pid', 'name']):
        if name.lower() in proc.info['name'].lower():
            return True
    return False

def is_server_alive(url):
    """Vérifie si un serveur est actif via HTTP"""
    try:
        response = requests.get(url, timeout=5)
        return response.status_code == 200
    except requests.RequestException:
        return False

def kill_ollama():
    """Tue toutes les instances d'Ollama"""
    for proc in psutil.process_iter(attrs=['pid', 'name']):
        if "ollama" in proc.info['name'].lower():
            print(f"🛑 Fermeture d'Ollama (PID {proc.info['pid']})...")
            proc.terminate()
            try:
                proc.wait(timeout=5)
            except psutil.TimeoutExpired:
                proc.kill()

def start_ollama():
    """Démarre Ollama et s'assure qu'il répond, sinon il relance après nettoyage"""
    retries = 0
    start_time = time.time()

    while retries < MAX_RETRIES and (time.time() - start_time) < TIMEOUT:
        if not is_process_running("ollama"):
            print("🚀 Démarrage d'Ollama...")
            subprocess.Popen(["ollama", "serve"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            time.sleep(5)

        if is_server_alive(f"http://127.0.0.1:{OLLAMA_PORT}"):
            print("✅ Ollama est en ligne !")
            return True

        retries += 1
        print(f"⏳ Tentative {retries}/{MAX_RETRIES}...")

    print("❌ Échec du démarrage d'Ollama après plusieurs tentatives. Tentative de redémarrage...")
    kill_ollama()
    time.sleep(5)
    return start_ollama()

# =======================
# Fonction pour améliorer le prompt avec Ollama
# =======================

def improve_prompt(base_prompt, Ollama_model, theme):
    """Utilise Ollama pour améliorer un prompt"""
    start_ollama()
    
    now = datetime.datetime.now()
    timestamp = now.strftime("%Y%m%d_%H%M%S")
    print(f"ollama started : {timestamp}")
    command = ["ollama", "run", Ollama_model]

    style_loras = LORA_THEMES.get("Neutre", [])
    if theme:
        if "-" in theme:
            themes = theme.split('-')
            for t in themes:
                style_loras.extend(LORA_THEMES.get(t, []))
        else:
            style_loras.extend(LORA_THEMES.get(theme, []))
    style_loras = list(set(style_loras))

    prompt_template = f"""
You are a Stable Diffusion prompt generation expert. Your task is to transform a basic scene description into a highly detailed, effective, and imaginative prompt suitable for image generation models like Stable Diffusion XL. You will receive a basic prompt containing core elements (subject, action, setting, clothing, mood, composition, details, style). Refine and enhance this input into a single, comma-separated English sentence adhering strictly to these rules:
1.  **Core Prompt Structure & Content:**
    * Begin the prompt string with the primary artistic **Style** keyword (e.g., "Oil painting", "Anime style", "Photorealistic", "Pop Art 60s").
    * Weave the provided elements (Subject, Action, Setting, Clothing, Mood, Composition, Details) into a coherent and descriptive scene. Use precise and evocative keywords.
    * Identify the main **Subject** and potentially the core **Action**, enclose them in parentheses with a weight between `(main subject:1.5)` and `(key action:1.7)` to emphasize them. Apply weight only to these 1 or 2 core elements.
    * Separate distinct concepts, descriptors, and elements *only* with commas. Avoid using commas within a single descriptive phrase.
    * Ensure the description is visually specific, detailed, and avoids ambiguity or euphemisms, focusing on clear visual representation (explicit and uncensored where appropriate for artistic expression).
2.  **Detail Enhancement:**
    * Inject **one or two** additional *thematically consistent* details that are not present in the input. These details should enrich the scene's atmosphere, narrative, or visual interest (e.g., environmental details, subtle character features, small background objects). Integrate them naturally within the prompt description.
3. **LoRA Integration:**
    * Add the LORAS at the end of the prompt
    * Select 1 or 2 relevant LoRAs from: {UTILITY_LORAS}.
    * Select 1 style Lora from: {style_loras}
    * Integrate LoRAs as `<lora:lora_name:weight>`, weight 0.5-0.8, use only this syntaxe for Loras.
    * Omit LoRAs if irrelevant.
4.  **Output Constraints:**
    * Output *only* the final, single-sentence prompt string.
    * No explanations, comments, introductions, or apologies.
Process this input prompt:
{{}}
"""
    input_data = prompt_template.format(base_prompt)

    try:
        process = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, encoding="utf-8")
        output, error = process.communicate(input=input_data, timeout=50)
        now = datetime.datetime.now()
        timestamp = now.strftime("%Y%m%d_%H%M%S")
        print(f"process : {timestamp}")
        
        if process.returncode == 0:
            process.kill()
            print ("Process killed")
            return output.strip()
        else:
            print(f"❌ Erreur Ollama : {error}")
            return base_prompt
    except subprocess.TimeoutExpired:
        now = datetime.datetime.now()
        timestamp = now.strftime("%Y%m%d_%H%M%S")
        print(f"process : {timestamp}")
        print("⚠️ Timeout: Ollama a mis trop de temps à répondre.")
        process.kill()
        return base_prompt 
    finally:
        kill_ollama()

# =======================
# Fonction pour générer l'image
# =======================
def generate_image(prompt, model, config):
    """Génère une image avec un LoRA via Stable Diffusion API"""
    
    payload = {
        "prompt": prompt,
        "steps": config["steps"],
        "width": config["width"],
        "height": config["height"],
        "cfg_scale": config["cfg_scale"],
        "sampler_name": config["sampler_name"],
        "scheduler": config["scheduler"],
        "override_settings": {
            "sd_model_checkpoint": model
        }
    }

    url = "http://127.0.0.1:7860/sdapi/v1/txt2img"
    headers = {"Content-Type": "application/json"}
    
    response = requests.post(url, data=json.dumps(payload), headers=headers)
    
    if response.status_code == 200:
        print(f"✅ Image générée avec le prompt: {prompt}")
        return response.json()
    else:
        print(f"❌ Erreur lors de la génération de l'image : {response.text}")
        return None

# =======================
# Fonction pour télécharger et sauvegarder l'image
# =======================

def save_image(image_base64, filename="generated_image.png", save_dir=SAVE_DIR):
    """Décode l'image base64 et la sauvegarde dans le répertoire spécifié."""
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    try:
        image_data = base64.b64decode(image_base64.split(",", 1)[0])
    except Exception as e:
        print(f"❌ Erreur lors du décodage de l'image base64: {e}")
        return None
    image_path = os.path.join(save_dir, filename)
    try:
        with open(image_path, 'wb') as f:
            f.write(image_data)
        print(f"✅ Image sauvegardée à : {image_path}")
        return image_path
    except Exception as e:
        print(f"❌ Erreur lors de la sauvegarde de l'image: {e}")
        return None

def generate_images_with_variations(num_iterations, variation_interval, config):
    num_iterations = num_iterations + 1
    for i in range(1, num_iterations):
        base_prompt = random.choice(Prompt_list)
        theme = None
               
        now = datetime.datetime.now()
        timestamp = now.strftime("%Y%m%d_%H%M%S")
        print(f"Start : {timestamp}")
        print(f" Itération {i}/{num_iterations}")
        
        sd_model_choice = random.choice(config["models"])
        print(f"Itération {i}: SD model = {sd_model_choice}")
     
        if base_prompt == "Random prompt" or i % variation_interval == 0:
            if base_prompt == "Random prompt":
                base_prompt, theme = generate_random_prompt()
                print(f"Random : {base_prompt}")
            
            n = len(OL_models)
            index = i % n
            Ollama_model = OL_models[index]
            print(f"Amelioration {i}: modèle = {Ollama_model}, Thème = {theme}")
            
            base_prompt = improve_prompt(base_prompt, Ollama_model, theme)
            now = datetime.datetime.now()
            timestamp = now.strftime("%Y%m%d_%H%M%S")
            print(f"Prompt : {timestamp}")
            print(f"Prompt: {base_prompt}")
        else:
            print(f"Prompt: {base_prompt}")
        
        response = generate_image(base_prompt, sd_model_choice, config)
        timestamp = now.strftime("%Y%m%d_%H%M%S")
        
        if response and "images" in response:
            image_base64 = response["images"][0]
            if image_base64:
                filename = f"generated_image_{timestamp}.png"
                image_path = save_image(image_base64, filename=filename)

                if image_path and i == 0:
                    print(f"✅ Première image sauvegardée à {image_path}")
                    now = datetime.datetime.now()
                    timestamp = now.strftime("%Y%m%d_%H%M%S")
                    print(f"End : {timestamp}")
        time.sleep(5)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Générateur d'images avec support pour SDXL et Flux.")
    parser.add_argument("--flux", action="store_true", help="Utiliser le modèle Flux au lieu de SDXL.")
    args = parser.parse_args()

    config = FLUX_CONFIG if args.flux else SDXL_CONFIG
    model_type = "Flux" if args.flux else "SDXL"

    print(f"🚀 Démarrage de la génération d'images avec le modèle {model_type}.")

    generate_images_with_variations(num_iterations=200, variation_interval=1, config=config)
