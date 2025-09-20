#!/usr/bin/env python3
"""Test spécifique pour les jeux Steam et l'amélioration des icônes."""

from icon_manager import icon_manager
import os

def test_steam_games():
    """Test spécifique pour les jeux Steam avec amélioration des icônes"""
    
    print("🎮 Test Spécial - Jeux Steam et Amélioration d'Icônes")
    print("=" * 60)
    
    # Jeux Steam problématiques à tester
    steam_games = [
        "American Truck Simulator",
        "Euro Truck Simulator 2", 
        "Satisfactory",
        "Kerbal Space Program",
        "ASTRONEER",
        "Left 4 Dead 2"
    ]
    
    print(f"\n🔍 Test avec {len(steam_games)} jeux Steam:")
    print("-" * 60)
    
    for i, game_name in enumerate(steam_games, 1):
        print(f"\n[{i:2d}/{len(steam_games)}] {game_name}")
        print("-" * 40)
        
        # Forcer la recherche (nettoyer le cache pour ce jeu)
        cache_key = game_name.lower()
        if cache_key in icon_manager.cache:
            old_path = icon_manager.cache[cache_key]
            if os.path.exists(old_path):
                os.remove(old_path)
                print(f"  🗑️  Ancien cache supprimé: {os.path.basename(old_path)}")
            del icon_manager.cache[cache_key]
        
        # Obtenir l'icône avec le nouveau système
        icon_path = icon_manager.get_icon_for_app(game_name)
        
        if icon_path and os.path.exists(icon_path):
            file_size = os.path.getsize(icon_path)
            print(f"  ✅ Icône haute qualité: {os.path.basename(icon_path)}")
            print(f"     Taille fichier: {file_size:,} bytes")
            
            # Vérifier les dimensions de l'image
            try:
                from PIL import Image
                with Image.open(icon_path) as img:
                    print(f"     Dimensions: {img.size[0]}x{img.size[1]} pixels")
                    print(f"     Mode couleur: {img.mode}")
            except Exception as e:
                print(f"     Erreur lecture image: {e}")
        else:
            print(f"  ❌ Échec pour {game_name}")
    
    # Sauvegarder le cache mis à jour
    icon_manager.save_cache()
    
    print("\n" + "=" * 60)
    print("📊 RÉSULTATS DU TEST")
    print("=" * 60)
    
    # Vérifier le dossier d'icônes
    icons_dir = "icons"
    if os.path.exists(icons_dir):
        icon_files = [f for f in os.listdir(icons_dir) if f.endswith('.png')]
        total_size = sum(os.path.getsize(os.path.join(icons_dir, f)) for f in icon_files)
        
        print(f"📁 Fichiers d'icônes: {len(icon_files)}")
        print(f"💾 Taille totale: {total_size / 1024:.1f} KB")
        print(f"📈 Taille moyenne: {total_size / len(icon_files) / 1024:.1f} KB par icône")
        
        # Afficher les nouvelles icônes créées
        new_icons = [f for f in icon_files if any(game.lower().replace(' ', '').replace('®', '') in f.lower() for game in steam_games)]
        if new_icons:
            print(f"\n🆕 Nouvelles icônes créées:")
            for icon_file in new_icons:
                file_path = os.path.join(icons_dir, icon_file)
                file_size = os.path.getsize(file_path)
                print(f"  • {icon_file} ({file_size:,} bytes)")
    
    print(f"\n🎉 Test terminé!")

if __name__ == "__main__":
    test_steam_games()
