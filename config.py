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
            "aidmaFLUXPro1.1-FLUX-v0.3.safetensors",
            "Fluxartis 28.11A.safetensors",
            "HyperdetailedRealismMJ7Flux.safetensors",
            "Luminous_Shadowscape-Flux.safetensors", "Phandigrams_II.safetensors",
            "Alex_Vede.safetensors"
        ],
        "HF": ["FluxDFaeTasticDetails.safetensors", "dark_fantasy_flux.safetensors", "Ev_Ganin_IV.safetensors"],
        "DH": ["dark_fantasy_flux.safetensors"],
        "SF": ["Mecha-flux.safetensors","Xuer - FLUX.safetensors"]
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
            "Splash_Art_SDXL.safetensors", "Luminous_Shadowscape-000016.safetensors",
            "CinematicStyle_v1.safetensors", "Adjust_SDXL_v4.0.safetensors","Phandigrams_II.safetensors" ],
        "SF": ["The_Petalbound.safetensors"],
        "HF": ["incase_style_v3-1_ponyxl_ilff.safetensors","Ev_Ganin_IV.safetensors"],
        "NP": ["The_Petalbound.safetensors"],
        "HD": ["gopXL.safetensors"]
    }
}

# =======================
# Configuration d'Ollama (pour l'amélioration des prompts)
# =======================
OL_models = ['gemma3']
OLLAMA_PORT = 11434
MAX_RETRIES = 20
TIMEOUT = 60
IMAGE_TIMEOUT = 300

# =======================
# Liste de prompts de base
# =======================
Prompt_list = [
    "Random prompt"
]
