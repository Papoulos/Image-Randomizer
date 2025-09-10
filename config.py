# =======================
# Paramètres modifiables
# =======================

# Paramètres de génération d'image
steps = 30  # Nombre d'étapes pour la génération de l'image
width = 1024  # Largeur de l'image
height = 1024  # Hauteur de l'image
cfg_scale = "7"
sampler_name = "DPM++ 2M"
scheduler = "karras"

# Modèles
OL_models = ['gemma3']
SD_models = ['albedobaseXL_v31Large']
SD_model = "" # Laisser vide pour une sélection aléatoire

# Liste de prompts de base
Prompt_list = [
    "Random prompt"
]

# Configuration d'Ollama
OLLAMA_PORT = 11434
MAX_RETRIES = 20  # Nombre maximum de tentatives
TIMEOUT = 60  # Temps maximum en secondes avant de relancer tout

# Répertoire de sauvegarde
SAVE_DIR = "G:\\LLM\\outputs\\"
