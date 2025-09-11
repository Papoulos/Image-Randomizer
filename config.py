# =======================
# Paramètres modifiables
# =======================

# Configurations de génération d'images
SDXL_CONFIG = {
    "steps": 30,
    "width": 1024,
    "height": 1024,
    "cfg_scale": "7",
    "sampler_name": "DPM++ 2M",
    "scheduler": "karras",
    "models": ['albedobaseXL_v31Large'],
    "utility_loras": [
        "OtherStyle_08-Merge5_06_04_02_02",
        "g0th1c2XLP",
        "gopXLP",
        "Adjust_SDXL_v4.0",
        "MJ52_v2.0",
        "add-detail-xl"
    ],
    "lora_themes": {
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
}

FLUX_CONFIG = {
    # NOTE: Ces paramètres sont des placeholders.
    # Ajustez-les en fonction de votre modèle Flux et de vos préférences.
    "steps": 20,
    "width": 1024,
    "height": 1024,
    "cfg_scale": "5",
    "sampler_name": "DPM++ 2M SDE",
    "scheduler": "sgm_uniform",
    "models": ["flux-schnell.safetensors"],
    "utility_loras": [],
    "lora_themes": {
        "Neutre": [  # Mappé depuis "Généralistes"
            "aidmaFLUXPro1.1-FLUX-v0.3",
            "Fluxartis 28.11A",
            "HyperdetailedRealismMJ7Flux",
            "Luminous_Shadowscape-Flux"
        ],
        "HF": [
            "FluxDFaeTasticDetails",
            "dark_fantasy_flux"
        ],
        "DH": [
            "dark_fantasy_flux"
        ]
    }
}

# Modèles d'amélioration de prompt
OL_models = ['gemma3']

# Liste de prompts de base
Prompt_list = [
    "Random prompt"
]

# Configuration d'Ollama
OLLAMA_PORT = 11434
MAX_RETRIES = 20
TIMEOUT = 60

# Répertoire de sauvegarde
SAVE_DIR = "G:\\LLM\\outputs\\"
