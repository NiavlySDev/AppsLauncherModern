#!/usr/bin/env python3
"""Démonstration du système d'icônes haute qualité."""

import os
from icon_manager import icon_manager

def demo_icon_system():
    """Démonstration complète du système d'icônes"""
    
    print("🎨 Démonstration du Système d'Icônes Haute Qualité")
    print("=" * 60)
    
    # Applications populaires à tester
    popular_apps = [
        "Discord", "Steam", "Chrome", "Firefox", "Spotify", 
        "Visual Studio Code", "Photoshop", "WhatsApp", "Telegram",
        "Notion", "Slack", "Zoom", "Teams", "Netflix"
    ]
    
    print(f"\n🔍 Test avec {len(popular_apps)} applications populaires:")
    print("-" * 60)
    
    successful_downloads = 0
    cached_icons = 0
    
    for i, app_name in enumerate(popular_apps, 1):
        print(f"\n[{i:2d}/{len(popular_apps)}] {app_name}")
        
        # Vérifier si déjà en cache
        cache_key = app_name.lower()
        if cache_key in icon_manager.cache:
            cached_path = icon_manager.cache[cache_key]
            if os.path.exists(cached_path):
                print(f"  💾 Déjà en cache: {os.path.basename(cached_path)}")
                cached_icons += 1
                continue
        
        # Obtenir l'icône
        icon_path = icon_manager.get_icon_for_app(app_name)
        
        if icon_path and os.path.exists(icon_path):
            file_size = os.path.getsize(icon_path)
            print(f"  ✅ Icône obtenue: {os.path.basename(icon_path)} ({file_size} bytes)")
            successful_downloads += 1
        else:
            print(f"  ❌ Échec pour {app_name}")
    
    # Statistiques finales
    print("\n" + "=" * 60)
    print("📊 STATISTIQUES FINALES")
    print("=" * 60)
    print(f"✅ Icônes réussies: {successful_downloads}")
    print(f"💾 Icônes en cache: {cached_icons}")
    print(f"❌ Échecs: {len(popular_apps) - successful_downloads - cached_icons}")
    print(f"📈 Taux de succès: {((successful_downloads + cached_icons) / len(popular_apps) * 100):.1f}%")
    
    # Informations sur le cache
    print(f"\n💾 CACHE D'ICÔNES")
    print("-" * 30)
    print(f"Entrées en cache: {len(icon_manager.cache)}")
    
    # Informations sur le dossier d'icônes
    icons_dir = "icons"
    if os.path.exists(icons_dir):
        icon_files = [f for f in os.listdir(icons_dir) if f.endswith('.png')]
        total_size = sum(os.path.getsize(os.path.join(icons_dir, f)) for f in icon_files)
        print(f"Fichiers d'icônes: {len(icon_files)}")
        print(f"Taille totale: {total_size / 1024:.1f} KB")
        
        # Afficher quelques exemples
        print(f"\n📄 Exemples d'icônes sauvegardées:")
        for icon_file in sorted(icon_files)[:5]:
            file_path = os.path.join(icons_dir, icon_file)
            file_size = os.path.getsize(file_path)
            print(f"  • {icon_file} ({file_size} bytes)")
        
        if len(icon_files) > 5:
            print(f"  ... et {len(icon_files) - 5} autres")
    
    print(f"\n🎉 Démonstration terminée!")
    print("Les icônes sont maintenant sauvegardées et prêtes à être utilisées dans l'application!")

if __name__ == "__main__":
    demo_icon_system()
