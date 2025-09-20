#!/usr/bin/env python3
"""Test avec extraction et amélioration des icônes locales."""

from icon_manager import icon_manager
import os

def test_local_icon_enhancement():
    """Test l'amélioration des icônes locales"""
    
    print("🔧 Test d'Amélioration d'Icônes Locales")
    print("=" * 50)
    
    # Chercher des raccourcis sur le bureau
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    
    if os.path.exists(desktop_path):
        shortcuts = [f for f in os.listdir(desktop_path) if f.endswith('.lnk')][:5]  # 5 premiers
        
        print(f"📁 Bureau: {desktop_path}")
        print(f"🔗 Raccourcis trouvés: {len(shortcuts)}")
        
        for i, shortcut in enumerate(shortcuts, 1):
            shortcut_path = os.path.join(desktop_path, shortcut)
            app_name = os.path.splitext(shortcut)[0]
            
            print(f"\n[{i}/{len(shortcuts)}] {app_name}")
            print("-" * 30)
            
            # Nettoyer le cache pour forcer l'extraction locale
            cache_key = app_name.lower()
            if cache_key in icon_manager.cache:
                old_path = icon_manager.cache[cache_key]
                if os.path.exists(old_path):
                    os.remove(old_path)
                del icon_manager.cache[cache_key]
            
            # Obtenir l'icône (devrait essayer en ligne puis local)
            icon_path = icon_manager.get_icon_for_app(app_name, shortcut_path)
            
            if icon_path and os.path.exists(icon_path):
                file_size = os.path.getsize(icon_path)
                print(f"  ✅ Icône: {os.path.basename(icon_path)}")
                print(f"     Taille: {file_size:,} bytes")
                
                # Déterminer la source
                if "_enhanced" in icon_path:
                    print(f"     🔧 Source: Icône locale améliorée")
                elif "_default" in icon_path:
                    print(f"     🎨 Source: Icône générée par défaut")
                else:
                    print(f"     🌐 Source: Icône téléchargée en ligne")
            else:
                print(f"  ❌ Échec")
    
    # Sauvegarder les changements
    icon_manager.save_cache()
    print(f"\n💾 Cache sauvegardé")

if __name__ == "__main__":
    test_local_icon_enhancement()
