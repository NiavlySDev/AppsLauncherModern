#!/usr/bin/env python3
"""Script pour nettoyer les données existantes."""

import os
import json

DATA_FILE = "launcher_data.json"

def clean_data():
    """Supprime le fichier de données existant"""
    if os.path.exists(DATA_FILE):
        try:
            os.remove(DATA_FILE)
            print(f"✅ Fichier de données '{DATA_FILE}' supprimé")
        except Exception as e:
            print(f"❌ Erreur lors de la suppression: {e}")
    else:
        print(f"ℹ️  Fichier de données '{DATA_FILE}' n'existe pas")

if __name__ == "__main__":
    clean_data()
