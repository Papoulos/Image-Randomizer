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

# LORAs
UTILITY_LORAS = [
    "OtherStyle_08-Merge5_06_04_02_02",
    "g0th1c2XLP",
    "gopXLP",
    "Adjust_SDXL_v4.0",
    "MJ52_v2.0",
    "add-detail-xl"
]

LORA_THEMES = {
    "Neutre": [
        "Splash_Art_SDXL",
        "ncase-ilff-v3-4",
        "Luminous_Shadowscape-000016",
        "Clean_Minimalist",
        "Digital_Impressionist_SDXL",
        "CinematicStyle_v1"
    ],
    "SF": [
        "Simon Stalenhag",
        "The_Petalbound"
    ],
    "HF": [
        "EpicF4nta5yXL"
    ],
    "NP": [
        "Thomas_Haller_Buchanan",
        "Simon Stalenhag",
        "The_Petalbound"
    ],
    "HD": [
        "Sinfully_Stylish_1.0_SDXL"
    ]
}
