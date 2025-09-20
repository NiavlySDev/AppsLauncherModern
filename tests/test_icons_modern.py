#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Script de test pour le chargement des icônes dans l'interface moderne
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from icon_manager import IconManager
from data import load_data, get_categories, get_applications_for_category
from PIL import Image

def test_icon_loading():
    """Test le chargement des icônes pour quelques applications"""
    print("🔧 Test du chargement des icônes")
    print("=" * 50)
    
    # Charge les données
    load_data()
    
    # Initialise le gestionnaire d'icônes
    icon_manager = IconManager()
    
    # Récupère quelques applications pour test
    categories = get_categories()
    test_count = 0
    success_count = 0
    
    for cat_id, category in categories.items():
        print(f"\n📁 Catégorie: {category['name']}")
        applications = get_applications_for_category(cat_id)
        
        for app_id, app in applications.items():
            if test_count >= 5:  # Limite le test à 5 apps
                break
                
            app_name = app["name"]
            app_path = app.get("shortcut_path", app.get("path", ""))
            
            print(f"\n🎮 Test: {app_name}")
            print(f"   📂 Chemin: {app_path}")
            
            # Test du chargement d'icône
            try:
                icon_path = icon_manager.get_icon_for_app(app_name, app_path)
                
                if icon_path and os.path.exists(icon_path):
                    # Vérifie que c'est une vraie image
                    try:
                        img = Image.open(icon_path)
                        print(f"   ✅ Icône trouvée: {icon_path}")
                        print(f"      📏 Taille: {img.size}")
                        print(f"      🎨 Mode: {img.mode}")
                        success_count += 1
                    except Exception as e:
                        print(f"   ❌ Fichier icône corrompu: {e}")
                else:
                    print(f"   ⚠️  Pas d'icône trouvée, utilise fallback")
                    
            except Exception as e:
                print(f"   ❌ Erreur: {e}")
            
            test_count += 1
        
        if test_count >= 5:
            break
    
    print(f"\n📊 Résultats:")
    print(f"   🔢 Apps testées: {test_count}")
    print(f"   ✅ Icônes chargées: {success_count}")
    print(f"   📈 Taux de réussite: {success_count/test_count*100:.1f}%")
    
    # Test du dossier des icônes
    icons_dir = "icons"
    if os.path.exists(icons_dir):
        icon_files = [f for f in os.listdir(icons_dir) if f.endswith('.png')]
        print(f"\n📁 Dossier icons/:")
        print(f"   📂 {len(icon_files)} fichiers PNG trouvés")
        
        # Affiche quelques exemples
        for i, icon_file in enumerate(icon_files[:3]):
            icon_path = os.path.join(icons_dir, icon_file)
            try:
                img = Image.open(icon_path)
                print(f"   📄 {icon_file}: {img.size} {img.mode}")
            except:
                print(f"   ❌ {icon_file}: corrompu")
    else:
        print(f"\n⚠️  Dossier icons/ n'existe pas encore")
    
    print(f"\n🎯 Pour voir les icônes, lancez: python simple_modern.py")

if __name__ == "__main__":
    test_icon_loading()
