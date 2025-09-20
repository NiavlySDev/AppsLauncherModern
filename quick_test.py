#!/usr/bin/env python3
"""Test rapide pour quelques applications spécifiques."""

from icon_manager import icon_manager

def quick_test():
    """Test rapide avec quelques applications populaires"""
    
    apps = ["Discord", "Steam", "Chrome"]
    
    print("🚀 Test rapide du système d'icônes amélioré")
    print("=" * 50)
    
    for app in apps:
        print(f"\n🔍 Test pour: {app}")
        icon_path = icon_manager.get_icon_for_app(app)
        if icon_path:
            print(f"  ✅ Icône créée: {icon_path}")
        else:
            print(f"  ❌ Échec")

if __name__ == "__main__":
    quick_test()
