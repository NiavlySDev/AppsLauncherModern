#!/usr/bin/env python3
"""Script pour tester le nouveau système de gestion d'icônes."""

from icon_manager import icon_manager
import os

def test_icon_manager():
    """Teste le gestionnaire d'icônes avec quelques applications"""
    
    print("🧪 Test du gestionnaire d'icônes amélioré")
    print("=" * 50)
    
    # Applications de test
    test_apps = [
        ("Discord", None),
        ("Steam", None),
        ("Visual Studio Code", None),
        ("Chrome", None),
        ("Photoshop", None),
    ]
    
    print("\n📦 Test d'icônes pour applications courantes:")
    for app_name, shortcut_path in test_apps:
        print(f"\n🔍 Traitement de: {app_name}")
        
        try:
            icon_path = icon_manager.get_icon_for_app(app_name, shortcut_path)
            if icon_path and os.path.exists(icon_path):
                print(f"  ✅ Icône obtenue: {os.path.basename(icon_path)}")
                print(f"     Chemin: {icon_path}")
            else:
                print(f"  ❌ Aucune icône obtenue")
                
        except Exception as e:
            print(f"  ❌ Erreur: {e}")
    
    # Vérifier le cache
    print(f"\n💾 Cache d'icônes:")
    print(f"  Entrées en cache: {len(icon_manager.cache)}")
    for app, path in icon_manager.cache.items():
        if os.path.exists(path):
            print(f"  ✅ {app} -> {os.path.basename(path)}")
        else:
            print(f"  ❌ {app} -> {path} (fichier manquant)")
    
    # Vérifier le dossier d'icônes
    icons_dir = "icons"
    if os.path.exists(icons_dir):
        icon_files = [f for f in os.listdir(icons_dir) if f.endswith('.png')]
        print(f"\n📁 Dossier d'icônes:")
        print(f"  Fichiers d'icônes: {len(icon_files)}")
        for icon_file in icon_files[:10]:  # Afficher les 10 premiers
            file_path = os.path.join(icons_dir, icon_file)
            file_size = os.path.getsize(file_path)
            print(f"  📄 {icon_file} ({file_size} bytes)")
        
        if len(icon_files) > 10:
            print(f"  ... et {len(icon_files) - 10} autres fichiers")
    
    print(f"\n✅ Test terminé!")

if __name__ == "__main__":
    test_icon_manager()
