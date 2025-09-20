#!/usr/bin/env python3
"""Test de l'API Steam pour un jeu spécifique."""

from icon_api import icon_api

def test_steam_api():
    """Test de l'API Steam"""
    
    print("🎮 Test de l'API Steam")
    print("=" * 30)
    
    # Tester avec un jeu populaire
    game = "Counter-Strike 2"
    
    print(f"\n🔍 Test avec: {game}")
    result = icon_api.search_steamdb(game)
    
    if result:
        print(f"✅ Trouvé: {result}")
    else:
        print("❌ Rien trouvé")

if __name__ == "__main__":
    test_steam_api()
