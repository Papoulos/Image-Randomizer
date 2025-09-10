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
import base64

# =======================
# Paramètres modifiables
# =======================
# curl -X GET http://127.0.0.1:7860/sdapi/v1/sd-models
# curl -X GET http://127.0.0.1:7860/sdapi/v1/lora-models


steps = 30  # Nombre d'étapes pour la génération de l'image
width = 1024  # Largeur de l'image
height = 1024  # Hauteur de l'image
OL_models = ['gemma3',]
SD_models = [albedobaseXL_v31Large']
SD_model = ""
Prompt_list = [
    "Random prompt"
    ]
    

OLLAMA_PORT = 11434

# =======================
# Vérification des processus
# =======================
MAX_RETRIES = 20  # Nombre maximum de tentatives
TIMEOUT = 60  # Temps maximum en secondes avant de relancer tout

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
            proc.terminate()  # Demande l'arrêt du processus
            try:
                proc.wait(timeout=5)  # Attend un peu pour voir s'il se ferme proprement
            except psutil.TimeoutExpired:
                proc.kill()  # Force la fermeture si nécessaire

def start_ollama():
    """Démarre Ollama et s'assure qu'il répond, sinon il relance après nettoyage"""
    retries = 0
    start_time = time.time()

    while retries < MAX_RETRIES and (time.time() - start_time) < TIMEOUT:
        if not is_process_running("ollama"):
            print("🚀 Démarrage d'Ollama...")
            subprocess.Popen(["ollama", "serve"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            time.sleep(5)  # Laisse le temps à Ollama de démarrer

        if is_server_alive(f"http://127.0.0.1:{OLLAMA_PORT}"):
            print("✅ Ollama est en ligne !")
            return True  # Succès

        retries += 1
        print(f"⏳ Tentative {retries}/{MAX_RETRIES}...")

    print("❌ Échec du démarrage d'Ollama après plusieurs tentatives. Tentative de redémarrage...")
    kill_ollama()
    time.sleep(5)  # Laisse le temps aux processus de se fermer
    return start_ollama()  # Relance le processus après nettoyage

# =======================
# Fonction pour améliorer le prompt avec Ollama
# =======================

def improve_prompt(base_prompt,Ollama_model):
    
    """Utilise Ollama pour améliorer un prompt"""
    start_ollama()  # Vérifier et démarrer Ollama si besoin
    
    now = datetime.datetime.now()
    timestamp = now.strftime("%Y%m%d_%H%M%S")
    print(f"ollama started : {timestamp}")
    command = ["ollama", "run", Ollama_model]
    prompt_template = """
You are a Stable Diffusion prompt generation expert. Your task is to transform a basic scene description into a highly detailed, effective, and imaginative prompt suitable for image generation models like Stable Diffusion XL. You will receive a basic prompt containing core elements (subject, action, setting, clothing, mood, composition, details, style). Refine and enhance this input into a single, comma-separated English sentence adhering strictly to these rules:
1.  **Core Prompt Structure & Content:**
    * Begin the prompt string with the primary artistic **Style** keyword (e.g., "Oil painting", "Anime style", "Photorealistic", "Pop Art 60s").
    * Weave the provided elements (Subject, Action, Setting, Clothing, Mood, Composition, Details) into a coherent and descriptive scene. Use precise and evocative keywords.
    * Identify the main **Subject** and potentially the core **Action**, enclose them in parentheses with a weight between `(main subject:1.5)` and `(key action:1.7)` to emphasize them. Apply weight only to these 1 or 2 core elements.
    * Separate distinct concepts, descriptors, and elements *only* with commas. Avoid using commas within a single descriptive phrase.
    * Ensure the description is visually specific, detailed, and avoids ambiguity or euphemisms, focusing on clear visual representation (explicit and uncensored where appropriate for artistic expression).

2.  **Detail Enhancement:**
    * Inject **one or two** additional *thematically consistent* details that are not present in the input. These details should enrich the scene's atmosphere, narrative, or visual interest (e.g., environmental details, subtle character features, small background objects). Integrate them naturally within the prompt description.

3. **LoRA Integration:**
    * Add the LORAS at the end of the prompt
    * Select 1 or 2 relevant LoRAs from: [ "OtherStyle_08-Merge5_06_04_02_02",  "g0th1c2XLP", "gopXLP", "Adjust_SDXL_v4.0", "MJ52_v2.0","add-detail-xl"].
    * Select 1 style Lora from:  [ "Splash_Art_SDXL", "incase-ilff-v3-4", "EpicF4nta5yXL", "Luminous_Shadowscape-000016", "Clean_Minimalist", "The_Petalbound", "Digital_Impressionist_SDXL", "Simon Stalenhag", "Thomas_Haller_Buchanan", "Sinfully_Stylish_1.0_SDXL", "CinematicStyle_v1"]
    * Integrate LoRAs as `<lora:lora_name:weight>`, weight 0.5-0.8, use only this syntaxe for Loras.
    * Omit LoRAs if irrelevant.
 
4.  **Output Constraints:**
    * Output *only* the final, single-sentence prompt string.
    * No explanations, comments, introductions, or apologies.

Process this input prompt:
{}

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
        # Ferme toutes les instances d'Ollama après usage
        kill_ollama()

# =======================
# Fonction pour générer l'image
# =======================
def generate_image(prompt, model):
    """Génère une image avec un LoRA via Stable Diffusion API"""
    
    # Paramètres de l'API Stable Diffusion
    payload = {
        "prompt": prompt,
        "steps": steps,
        "width": width,
        "height": height,
        "cfg_scale": "7",
        "sampler_name": "DPM++ 2M", # Définir la méthode de sampling
        "scheduler": "karras", # Définir le schedule
        "override_settings": {
            "sd_model_checkpoint": model
        }
    }

    # Appel à l'API Stable Diffusion pour générer l'image
    url = "http://127.0.0.1:7860/sdapi/v1/txt2img"
    headers = {"Content-Type": "application/json"}
    
    response = requests.post(url, data=json.dumps(payload), headers=headers)
    
    if response.status_code == 200:
        print(f"✅ Image générée avec le prompt: {prompt}")
        return response.json()  # Retourne les informations des images générées
    else:
        print(f"❌ Erreur lors de la génération de l'image : {response.text}")
        return None

# =======================
# Fonction pour télécharger et sauvegarder l'image
# =======================

def save_image(image_base64, save_dir="G:\\LLM\\outputs\\", filename="generated_image.png"):
    """Décode l'image base64 et la sauvegarde dans le répertoire spécifié."""

    # Vérifier si le répertoire existe, sinon le créer
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    # Décodage de l'image base64
    try:
        image_data = base64.b64decode(image_base64.split(",", 1)[0])
    except Exception as e:
        print(f"❌ Erreur lors du décodage de l'image base64: {e}")
        return None

    # Chemin complet de l'image
    image_path = os.path.join(save_dir, filename)

    # Sauvegarde de l'image
    try:
        with open(image_path, 'wb') as f:
            f.write(image_data)
        print(f"✅ Image sauvegardée à : {image_path}")
        return image_path
    except Exception as e:
        print(f"❌ Erreur lors de la sauvegarde de l'image: {e}")
        return None






def generate_random_prompt():

# --- Lists Theme: SCIENCE-FICTION (Standard & Dark) ---

    sujets_sf = [
        "a weary starship captain",
        "a rogue android assassin",
        "a cyborg bounty hunter",
        "an alien ambassador",
        "a mech pilot ",
        "a scientist",
        "a deep-space smuggler",
        "an artificial intelligence",
        "a colonist",
        "a xeno-archaeologist ",
        "a heavily augmented corporate enforcer",
        "a mutant scavenger",
        "a bio-engineer",
        "an explorer",
        "a tech-priest",
        "a data-thief",
        "a lone survivor",
        "a mind-wiped agent ",
        "an alien entity"
    ]

    actions_sf = [
        "hacking into a corrupted corporate datastream",
        "piloting a battered starfighter through wreckage fields",
        "performing emergency repairs on a failing life support system",
        "navigating treacherous, decaying urban underlevels",
        "activating an unstable, forbidden alien device",
        "analyzing a disturbing, non-Euclidean artifact",
        "evading relentless security drones in zero-gravity combat",
        "making a desperate plea to an uncaring alien hive mind",
        "scanning a planet scarred by orbital bombardment",
        "fleeing from grotesque, bio-engineered monstrosities",
        "interfacing with a dying ship's corrupted AI core",
        "deploying a nanobot swarm that consumes organic matter",
        "witnessing the terrifying spectacle of a warp drive malfunction",
        "monitoring flickering screens showing catastrophic data",
        "plugging into a dangerous, unregulated virtual reality",
        "receiving painful, involuntary cybernetic augmentation",
        "escaping a containment breach in a research facility",
        "scavenging vital supplies from derelict spacecraft",
        "decrypting a transmission foretelling cosmic doom",
        "battling malfunctioning security robots in dark corridors"
    ]

    lieux_sf = [
        "the derelict bridge of a ghost starship, alarms dead",
        "a rain-slicked, garbage-filled alley in a cyberpunk megalopolis",
        "an abandoned orbital station venting atmosphere slowly",
        "a toxic alien jungle where plants actively hunt",
        "the decaying, labyrinthine interior of a planet-sized supercomputer",
        "a poorly lit, overcrowded mining colony on a desolate moon",
        "a clandestine bio-engineering lab filled with failed experiments",
        "the ruins of a city destroyed by advanced weaponry",
        "a black market bazaar hidden deep within a space hulk",
        "the cold, humming core of a Doomsday machine",
        "an underwater research facility compromised by alien pressure",
        "a glitching, nightmarish landscape within virtual reality",
        "a graveyard of decommissioned, rusting war machines",
        "a cryo-storage facility where occupants have mutated",
        "a resource-stripped desert planet under a sickly sun",
        "the oppressive, bio-mechanical interior of an alien vessel",
        "a quarantine zone surrounding an extraterrestrial plague outbreak",
        "a heavily fortified corporate arcology casting long shadows",
        "an impossible alien city built with disturbing geometry",
        "the eerie, silent void near a black hole's event horizon"
    ]

    ambiances_sf = [
        "a sleek, black environmental suit, subtly damaged",
        "a heavy combat exoskeleton stained with alien ichor",
        "crude, visible cybernetic limbs sparking intermittently",
        "glitching holographic clothing displaying corrupted ads",
        "ragged scavenger gear patched with scrap metal and bio-fiber",
        "a long, stained trench coat concealing multiple weapons",
        "a minimalist, utilitarian uniform of a dystopian regime",
        "dark, form-fitting stealth suit with optical camouflage",
        "a sterile, blood-spattered hazard suit from a lab outbreak",
        "flowing, tattered robes of a void cultist leader",
        "a pilot's G-suit, torn and stained with hydraulic fluid",
        "exposed, crude cybernetics replacing missing body parts",
        "a grimy virtual reality interface suit covered in wires",
        "heavy, scarred power armor marked with kill counts",
        "patched, mismatched clothing of a desperate survivor",
        "angular, intimidating armor of corporate security forces",
        "a bulky, damaged EVA spacesuit leaking oxygen",
        "augmented reality goggles displaying ominous warnings",
        "adaptive camouflage fatigues flickering erratically",
        "bio-luminescent symbiotic plating fused to the skin"
    ]

    atmosphere_sf = [
        "cold, sterile fluorescent lighting casting harsh shadows",
        "flickering emergency lights bathing corridors in red",
        "the oppressive silence of a vacuum or dead station",
        "lens flares from harsh, industrial spotlights",
        "dense, acidic rain under a perpetually overcast sky",
        "eerie bioluminescent glow from toxic alien fungi",
        "oppressive, sterile white light of a sinister medical bay",
        "the disturbing green glow of unknown energy fields",
        "constant blaring of distant, ignored warning sirens",
        "artificial, sickly yellow sunlight in a polluted biodome",
        "disorienting strobe lights from malfunctioning equipment",
        "the cold, pale blue glow from countless data screens",
        "absolute, terrifying darkness swallowing all light",
        "thick, choking smog obscuring visibility in a dense city",
        "electrical arcing illuminating scenes in brief, violent flashes",
        "the blinding, unforgiving glare of a nearby binary star",
        "a gritty, noir atmosphere with deep shadows and high contrast",
        "shimmering heat haze over irradiated tech ruins",
        "holographic projections glitching, showing disturbing images",
        "an unsettling sense of being watched or hunted"
    ]

    compositions_sf = [
        "extreme close-up on a frantic, cybernetic eye",
        "desolate wide shot of a lone figure against industrial ruins",
        "imposing low angle shot emphasizing oppressive architecture",
        "claustrophobic centered shot within a cramped cockpit",
        "over-the-shoulder shot revealing a screen full of errors",
        "disorienting dutch angle during a system failure or attack",
        "symmetrical shot down a long, empty, decaying corridor",
        "erratic tracking shot following someone running in fear",
        "fisheye lens perspective from a damaged security camera",
        "isolating long shot showing vulnerability against vast machinery",
        "split diopter focusing on a weapon and a terrified face",
        "oppressive high angle looking down into slums or work pits",
        "shaky first-person POV from inside a damaged helmet",
        "rule of thirds placing a character against a dangerous void",
        "ominous rack focus from a dripping pipe to a shadowy figure",
        "stark silhouette against a burning cityscape or explosion",
        "uncomfortably tight framing leaving little breathing room",
        "detailed macro shot of malfunctioning, sparking circuitry",
        "worm's-eye view of towering, hostile alien structures",
        "cinematic widescreen showing isolation in a vast, dead space"
    ]

    details_sf = [
        "flickering neon signs casting long, dancing shadows",
        "visible streams of corrupted data code glitching in the air",
        "puddles of iridescent chemical waste bubbling slightly",
        "discarded, damaged cybernetic limbs lying in alleys",
        "distant, muffled warning klaxons echoing constantly",
        "pressurized steam hissing menacingly from broken vents",
        "patches of invasive, pulsating alien bio-mold",
        "small metallic debris gently floating in zero-gravity",
        "smashed security monitors displaying only static or errors",
        "glitching holographic 'Wanted' posters showing grim faces",
        "visible ripples or distortions from strange energy fluctuations",
        "pools of leaking, luminous coolant dripping from machinery",
        "scattered, empty nutrient paste tubes and ration packs",
        "exposed, sparking electrical wiring panels hanging loose",
        "a severed, malfunctioning robotic arm twitching erratically",
        "silent, ominous surveillance drones drifting slowly overhead",
        "glowing, cryptic graffiti tags warning of danger",
        "open, ice-covered cryogenic suspension pods, contents unknown",
        "scattered brass bullet casings glinting under harsh light",
        "trails of viscous, black unidentified slime on floors"
    ]

    styles_sf = [
        "gritty, dystopian cyberpunk aesthetic (style of Blade Runner 2049)",
        "dark industrial sci-fi (style of Alien, Event Horizon)",
        "retro-futurism noir (style of Bioshock, Dark City)",
        "bio-punk horror emphasizing grotesque body modification",
        "hard science fiction realism with a sense of dread",
        "cosmic horror sci-fi (style of H.P. Lovecraft, Prometheus)",
        "anime mech design with dark, psychological themes (style of Evangelion)",
        "dieselpunk post-apocalypse (style of Mad Max)",
        "photorealistic concept art depicting oppressive futures",
        "glitch art aesthetics representing system corruption",
        "surreal bio-mechanical horror (style of H.R. Giger, Zdzisław Beksiński)",
        "found footage or security camera perspective",
        "cinematic sci-fi horror film look (style of John Carpenter)",
        "stark brutalist architectural focus, emphasizing scale and coldness",
        "monochromatic noir photography with high contrast",
        "Soviet-era brutalist retrofuturism",
        "detailed technical illustration of decaying machinery",
        "cell-shaded graphics with dark outlines and grim palettes",
        "abstract art depicting technological singularity or cosmic dread",
        "infra-red or thermal vision point-of-view"
    ]
        
    
  
# Lists for generating fantasy and science-fantasy prompts

    sujets_hf = [
        "A mystical dragon", "An ancient sorcerer", "A cybernetic knight", "A rogue assassin",
        "A wise old sage", "A futuristic bounty hunter", "A dark elf", "A noble paladin",
        "A steampunk inventor", "A ghostly apparition", "A celestial being", "A shadowy figure",
        "A time-traveling adventurer", "A cursed warrior", "A mystic seer", "A fallen angel",
        "A bio-engineered creature", "A holographic entity", "A sentient robot", "A vampire lord"
    ]

    actions_hf = [
        "Casting a powerful spell", "Wielding a legendary sword", "Flying through the sky",
        "Sneaking through shadows", "Summoning a magical creature", "Fighting a horde of enemies",
        "Exploring an ancient ruin", "Riding a mythical beast", "Inventing a magical device",
        "Performing a dark ritual", "Guarding a sacred artifact", "Traveling through time",
        "Battling a fierce dragon", "Channeling cosmic energy", "Uncovering a hidden secret",
        "Leading an army into battle", "Confronting a powerful foe", "Healing a wounded ally",
        "Seeking ancient knowledge", "Protecting a vulnerable village"
    ]

    lieux_hf = [
        "A dense, enchanted forest", "A towering, ancient castle", "A futuristic, neon-lit city",
        "A haunted, abandoned mansion", "A vast, otherworldly landscape", "A bustling, steampunk market",
        "A serene, mystical lake", "A dark, underground cavern", "A floating, sky island",
        "A post-apocalyptic wasteland", "A hidden, elven sanctuary", "A grand, gothic cathedral",
        "A lush, alien jungle", "A frozen, icy tundra", "A mystical, crystal cave",
        "A war-torn battlefield", "A tranquil, hidden grove", "A bustling, space station",
        "A eerie, ghostly graveyard", "A majestic, mountain peak"
    ]

    vetements_hf = [
        "Ornate, magical robes", "Futuristic, cybernetic armor", "Dark, leather assassin gear",
        "Elegant, elven attire", "Heavy, plate mail armor", "Mystical, rune-covered cloak",
        "Steampunk, goggle-adorned outfit", "Gothic, Victorian-era dress", "Ancient, ritualistic garb",
        "Light, ethereal fabric", "Shadowy, hooded cloak", "Bio-luminescent suit", "Holographic clothing",
        "Battle-scarred armor", "Ceremonial, royal regalia", "Time-traveler's eclectic outfit",
        "Cursed, enchanted armor", "Noble, knightly attire", "Alien, exosuit", "Vampiric, elegant wear"
    ]

    ambiances_hf = [
        "Mystical and ethereal", "Dark and foreboding", "Futuristic and sleek", "Ancient and timeless",
        "Eerie and haunting", "Vibrant and otherworldly", "Gothic and moody", "Heroic and inspiring",
        "Melancholic and somber", "Chaotic and intense", "Serene and tranquil", "Majestic and awe-inspiring",
        "Apocalyptic and desolate", "Whimsical and playful", "Dramatic and tense", "Enchanting and magical",
        "Cybernetic and cold", "Mysterious and intriguing", "Grand and epic", "Shadowy and ominous"
    ]

    compositions_hf = [
        "Close-up portrait", "Wide, sweeping landscape", "Bird's-eye view", "Dramatic silhouette",
        "Symmetrical and balanced", "Dynamic and action-packed", "Isolated and focused", "Crowded and chaotic",
        "Low-angle, heroic shot", "High-angle, diminishing perspective", "Dutch angle, disorienting",
        "Rule of thirds composition", "Leading lines drawing focus", "Frame within a frame",
        "Natural framing with environment", "Deep space with atmospheric effects",
        "Shallow depth of field, subject focus", "Panoramic and expansive", "Intimate and personal",
        "Monumental and grand"
    ]

    details_hf = [
        "floating crystal shards shimmering nearby",
        "glowing arcane runes carved into walls or stones",
        "patches of strange bioluminescent fungi on surfaces",
        "wisps of spectral energy drifting through the air",
        "scattered, broken mechanical parts on the ground",
        "a small, hovering, silent observation drone",
        "puddles of iridescent, unidentifiable liquid",
        "glowing cracks in the ground revealing energy/lava",
        "ancient, weathered carvings on nearby pillars",
        "swirling motes of magical dust in the light",
        "a flickering, damaged holographic advertisement",
        "thick, metallic vines snaking across structures",
        "a small pile of bleached, unidentified bones",
        "sparking, exposed power conduits arcing occasionally",
        "intricate, floating geometric energy patterns",
        "a shimmering heat haze distorting the background",
        "clumps of rare, unusually colored exotic flowers",
        "mysterious glowing symbols painted on surfaces",
        "a small, unattended bubbling cauldron or beaker",
        "discarded, faintly glowing energy cells littered about"
    ]

    styles_hf = [
        "Dark fantasy", "Cyberpunk", "Steampunk", "High fantasy", "Gothic horror", "Science fantasy",
        "Mythological", "Post-apocalyptic", "Ethereal and dreamlike", "Heroic and epic",
        "Mystical and enchanting", "Dystopian and grim", "Alien and otherworldly", "Ancient and mystical",
        "Futuristic and sleek", "Shadowy and ominous", "Vibrant and whimsical", "Melancholic and somber",
        "Grand and majestic", "Eerie and haunting"
    ]
    
    Themes = [ "SF","HF" ]
    
    theme = random.choice(Themes)
    
    if theme == "SF" :  
        print("SF")
        sujet = random.choice(sujets_sf)
        action = random.choice(actions_sf)
        lieu = random.choice(lieux_sf)
        atmosphere = random.choice(atmosphere_sf)
        ambiance = random.choice(ambiances_sf)
        composition = random.choice(compositions_sf)
        style = random.choice(styles_sf)

        # Choisir 2 ou 3 détails distincts
        nb_details = random.randint(2, 3)
        details_choisis = random.sample(details_sf, nb_details)
        details_str = ", ".join(details_choisis) # Les sépare par une virgule

        # Assembler le prompt brut
        # Vous pouvez varier la structure ici
        # random_prompt = f"{composition} d'un(e) {sujet} {vetement}, {action} dans un(e) {lieu}. {details_str}. Ambiance {ambiance}. Style {style}."
        random_prompt = f"Science-fiction, {composition}, {sujet}, {action}, {lieu}, {details_str}, {atmosphere}, {ambiance}, {style}."
    elif theme == "HF" :
        print("HF")
        sujet = random.choice(sujets_hf)
        action = random.choice(actions_hf)
        lieu = random.choice(lieux_hf)
        vetement = random.choice(vetements_hf)
        ambiance = random.choice(ambiances_hf)
        composition = random.choice(compositions_hf)
        style = random.choice(styles_hf)

        # Choisir 2 ou 3 détails distincts
        nb_details = random.randint(2, 3)
        details_choisis = random.sample(details_hf, nb_details)
        details_str = ", ".join(details_choisis) # Les sépare par une virgule

        # Assembler le prompt brut
        # Vous pouvez varier la structure ici
        # random_prompt = f"{composition} d'un(e) {sujet} {vetement}, {action} dans un(e) {lieu}. {details_str}. Ambiance {ambiance}. Style {style}."
        random_prompt = f"Heroic-Fantasy, {composition}, {sujet}, {vetement}, {action}, {lieu}, {details_str}, {ambiance}, {style}."



    # Ici, vous enverriez prompt_brut à votre LLM pour l'améliorer
    # prompt_final = appeler_llm(prompt_brut)
    # return prompt_final

    return random_prompt # Pour l'instant, on retourne le prompt brut



def generate_images_with_variations(num_iterations, variation_interval):
    num_iterations = num_iterations + 1
    # Initialisation de l'itération
    for i in range(1, num_iterations):
        
        base_prompt = random.choice(Prompt_list)
               
        now = datetime.datetime.now()
        timestamp = now.strftime("%Y%m%d_%H%M%S")
        print(f"Start : {timestamp}")
        print(f" Itération {i}/{num_iterations}")
        
        # Changement du modèle
        SD_model = random.choice(SD_models)

        print(f"Itération {i}: SD model = {SD_model}")
     
        # Améliorer le prompt tous les X itérations
        if base_prompt == "Random prompt" or i % variation_interval == 0:
            
            if base_prompt == "Random prompt":
                base_prompt= generate_random_prompt()
                print(f"Random : {base_prompt}")
            
            n = len(OL_models)
            index = i % n
            Ollama_model = OL_models[index]

            print(f"Amelioration {i}: modèle = {Ollama_model}")
            
            base_prompt = improve_prompt(base_prompt,Ollama_model)
            now = datetime.datetime.now()
            timestamp = now.strftime("%Y%m%d_%H%M%S")
            print(f"Prompt : {timestamp}")
            print(f"Prompt: {base_prompt}")
        else:
            print(f"Prompt: {base_prompt}")
        
        
        # Générer l'image avec ce prompt et LoRA
        
        response = generate_image(base_prompt,SD_model)  # Correcte l'appel ici
        timestamp = now.strftime("%Y%m%d_%H%M%S")
        
        if response and "images" in response:
            # Si l'image est générée, récupérer la chaîne base64 et sauvegarder l'image
            image_base64 = response["images"][0]
            if image_base64:
                # Générer un nom de fichier unique
                filename = f"generated_image_{timestamp}.png"
                # filename = f"generated_image_{i}.png"
                # Sauvegarder l'image dans le répertoire spécifié
                image_path = save_image(image_base64, filename=filename)

                # Si c'est la première itération, sauvegarder également cette image
                if i == 0:
                    print(f"✅ Première image sauvegardée à {image_path}")
                    now = datetime.datetime.now()
                    timestamp = now.strftime("%Y%m%d_%H%M%S")
                    print(f"End : {timestamp}")

        # Pause pour éviter de surcharger l'API
        time.sleep(5)


generate_images_with_variations( num_iterations=200, variation_interval=1)
