import customtkinter as ctk
import sys
import os

# Ajouter le répertoire parent au path pour les imports
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from modern_ui.main_view import ModernMainView
from modern_ui.theme import ModernTheme
from data import load_data

class ModernLauncherApp(ctk.CTk):
    """Application principale avec interface moderne"""
    
    def __init__(self):
        super().__init__()
        
        # Configuration de la fenêtre
        self.title("Lanceur d'Applications - Interface Moderne")
        self.geometry("1200x800")
        self.minsize(800, 600)
        
        # Configuration du thème
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")
        
        # Chargement des données
        load_data()
        
        # Configuration de l'interface
        self.setup_ui()
        
        # Centre la fenêtre
        self.center_window()
    
    def setup_ui(self):
        """Configure l'interface utilisateur principale"""
        # Configuration de la grille principale
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        
        # Vue principale
        self.main_view = ModernMainView(self)
        self.main_view.grid(row=0, column=0, sticky="nsew")
    
    def center_window(self):
        """Centre la fenêtre sur l'écran"""
        self.update_idletasks()
        x = (self.winfo_screenwidth() // 2) - (self.winfo_width() // 2)
        y = (self.winfo_screenheight() // 2) - (self.winfo_height() // 2)
        self.geometry(f"+{x}+{y}")

def main():
    """Fonction principale"""
    try:
        # Vérification des dépendances
        import customtkinter
        from PIL import Image
        print("✅ Toutes les dépendances sont installées")
        
        # Création et lancement de l'application
        app = ModernLauncherApp()
        print("🚀 Lancement de l'interface moderne...")
        app.mainloop()
        
    except ImportError as e:
        print(f"❌ Erreur d'import : {e}")
        print("Installez les dépendances avec : pip install customtkinter pillow")
        input("Appuyez sur Entrée pour fermer...")
    except Exception as e:
        print(f"❌ Erreur : {e}")
        input("Appuyez sur Entrée pour fermer...")

if __name__ == "__main__":
    main()
