#!/usr/bin/env python3
"""Configuration et paramètres de l'application."""

# Paramètres de l'interface
UI_CONFIG = {
    "window_width": 900,
    "window_height": 600,
    "cards_per_row": 4,
    "card_width": 150,
    "card_height": 120,
    "icon_size": 24,
    "preview_icon_size": 32
}

# Paramètres des raccourcis
SHORTCUT_CONFIG = {
    "supported_extensions": ['.lnk', '.exe', '.bat', '.cmd', '.url'],
    "default_search_paths": [
        "~/Desktop",
        "~/AppData/Roaming/Microsoft/Windows/Start Menu/Programs",
        "C:/ProgramData/Microsoft/Windows/Start Menu/Programs"
    ],
    "auto_fill_name": True,
    "extract_icons": True
}

# Paramètres de sauvegarde
DATA_CONFIG = {
    "auto_save": True,
    "backup_count": 3,
    "data_file": "launcher_data.json"
}

def get_config(section):
    """Récupère une section de configuration"""
    configs = {
        "ui": UI_CONFIG,
        "shortcut": SHORTCUT_CONFIG,
        "data": DATA_CONFIG
    }
    return configs.get(section, {})
