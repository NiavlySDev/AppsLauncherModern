#!/usr/bin/env python3
"""
AppsLauncher Modern - Point d'entrée principal
Lanceur d'applications moderne avec interface CustomTkinter
"""

import sys
import os

# Ajouter le répertoire current au path pour les imports
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, current_dir)

if __name__ == "__main__":
    try:
        # Import du lanceur principal
        from launcher import SimpleLauncherApp
        
        # Lancement de l'application
        app = SimpleLauncherApp()
        app.mainloop()
        
    except ImportError as e:
        print(f"❌ Erreur d'importation: {e}")
        print("💡 Assurez-vous que toutes les dépendances sont installées:")
        print("   pip install customtkinter pillow requests beautifulsoup4")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Erreur lors du lancement: {e}")
        sys.exit(1)