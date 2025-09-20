#!/usr/bin/env python3
"""Script pour vérifier les données sauvegardées."""

import json
import os

DATA_FILE = "launcher_data.json"

def check_saved_data():
    """Vérifie et affiche les données sauvegardées"""
    
    if not os.path.exists(DATA_FILE):
        print(f"❌ Fichier de données '{DATA_FILE}' non trouvé")
        return
    
    try:
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        categories = data.get("categories", {})
        applications = data.get("applications", {})
        
        print(f"✅ Données chargées depuis '{DATA_FILE}'")
        print(f"📁 Catégories: {len(categories)}")
        print(f"📱 Applications: {len(applications)}")
        print()
        
        print("Catégories:")
        for cat_id, cat_info in categories.items():
            print(f"  - {cat_info['name']} {cat_info.get('icon', '')} (ID: {cat_id[:8]}...)")
        
        print()
        print("Applications (avec raccourcis):")
        for app_id, app_info in applications.items():
            shortcut = app_info.get('shortcut_path', 'Aucun raccourci')
            if shortcut != 'Aucun raccourci':
                shortcut = os.path.basename(shortcut)
            print(f"  - {app_info['name']} -> {shortcut}")
        
    except Exception as e:
        print(f"❌ Erreur lors du chargement: {e}")

if __name__ == "__main__":
    check_saved_data()
