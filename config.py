# =======================
# Paramètres Généraux
# =======================
SAVE_DIR = "G:\\LLM\\outputs\\"
COMFYUI_URL = "http://127.0.0.1:8188"
# NOTE: Mettez à jour ce chemin pour qu'il corresponde à votre répertoire de sortie ComfyUI
COMFYUI_OUTPUT_DIR = "G:\\ComfyUI\\output\\"

# =======================
# Configuration des Workflows
# =======================

# --- Configuration du modèle FLUX (via ComfyUI) ---
FLUX_CONFIG = {
    "workflow_file": "flux_workflow.json",
    "prompt_node_id": "6",
    "lora_node_id": "38",
    "lora_themes": {
        "Neutre": [
            "aidmaFLUXPro1.1-FLUX-v0.3",
            "Fluxartis 28.11A",
            "HyperdetailedRealismMJ7Flux",
            "Luminous_Shadowscape-Flux",
            "Alex_Vede.safetensors"
        ],
        "HF": ["FluxDFaeTasticDetails", "dark_fantasy_flux"],
        "DH": ["dark_fantasy_flux"]
    }
}

# --- Configuration du modèle SDXL (via ComfyUI) ---
SDXL_CONFIG = {
    "workflow_file": "sdxl_workflow.json",
    "prompt_node_id": "6",
    # NOTE: Ce workflow a deux LoRAs. Nous ciblons le premier (style).
    "lora_node_id": "11",
    "lora_themes": {
        "Neutre": [
            "Splash_Art_SDXL", "ncase-ilff-v3-4", "Luminous_Shadowscape-000016",
            "Clean_Minimalist", "Digital_Impressionist_SDXL", "CinematicStyle_v1",
            "Adjust_SDXL_v4.0"
        ],
        "SF": ["Simon Stalenhag", "The_Petalbound"],
        "HF": ["EpicF4nta5yXL"],
        "NP": ["Thomas_Haller_Buchanan", "Simon Stalenhag", "The_Petalbound"],
        "HD": ["Sinfully_Stylish_1.0_SDXL"]
    }
}

# =======================
# Configuration d'Ollama (pour l'amélioration des prompts)
# =======================
OL_models = ['gemma3']
OLLAMA_PORT = 11434
MAX_RETRIES = 20
TIMEOUT = 60

# =======================
# Liste de prompts de base
# =======================
Prompt_list = [
    "Random prompt"
]
