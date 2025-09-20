import customtkinter as ctk
import sys
import os
from PIL import Image, ImageDraw, ImageFont
import threading
import time

# Ajouter le répertoire parent au path pour les imports
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from src.ui.modern_ui.main_view import ModernMainView
from src.ui.modern_ui.theme import ModernTheme
from src.ui.modern_ui.effects import LoadingSpinner
from src.core.data import load_data

class SplashScreen(ctk.CTkToplevel):
    """Écran de chargement moderne"""
    
    def __init__(self):
        super().__init__()
        
        # Configuration de la fenêtre
        self.title("")
        self.geometry("600x400")
        self.resizable(False, False)
        
        # Supprime la barre de titre
        self.overrideredirect(True)
        
        # Configuration du style
        self.configure(fg_color=ModernTheme.BG_PRIMARY)
        
        # Centre la fenêtre
        self.center_window()
        
        # Interface
        self.setup_ui()
        
        # Animation de chargement
        self.start_loading()
    
    def center_window(self):
        """Centre la fenêtre sur l'écran"""
        self.update_idletasks()
        x = (self.winfo_screenwidth() // 2) - (300)
        y = (self.winfo_screenheight() // 2) - (200)
        self.geometry(f"600x400+{x}+{y}")
    
    def setup_ui(self):
        """Configure l'interface du splash screen"""
        # Container principal
        main_frame = ctk.CTkFrame(
            self,
            fg_color=ModernTheme.BG_PRIMARY,
            corner_radius=20,
            border_width=2,
            border_color=ModernTheme.PRIMARY
        )
        main_frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Logo/Titre
        logo_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
        logo_frame.pack(expand=True, pady=50)
        
        # Icône principale
        app_icon = ctk.CTkLabel(
            logo_frame,
            text="🚀",
            font=("Segoe UI Emoji", 80),
            text_color=ModernTheme.PRIMARY
        )
        app_icon.pack(pady=(0, 20))
        
        # Titre
        title_label = ctk.CTkLabel(
            logo_frame,
            text="Lanceur d'Applications",
            font=("Segoe UI", 32, "bold"),
            text_color=ModernTheme.TEXT_PRIMARY
        )
        title_label.pack(pady=(0, 10))
        
        # Sous-titre
        subtitle_label = ctk.CTkLabel(
            logo_frame,
            text="Interface Moderne • Gestionnaire d'Icônes Intelligent",
            font=("Segoe UI", 14),
            text_color=ModernTheme.TEXT_SECONDARY
        )
        subtitle_label.pack(pady=(0, 30))
        
        # Barre de progression
        self.progress_bar = ctk.CTkProgressBar(
            logo_frame,
            width=300,
            height=8,
            progress_color=ModernTheme.PRIMARY,
            fg_color=ModernTheme.BG_SECONDARY
        )
        self.progress_bar.pack(pady=20)
        self.progress_bar.set(0)
        
        # Statut de chargement
        self.status_label = ctk.CTkLabel(
            logo_frame,
            text="Initialisation...",
            font=("Segoe UI", 12),
            text_color=ModernTheme.TEXT_MUTED
        )
        self.status_label.pack(pady=(10, 0))
        
        # Version
        version_label = ctk.CTkLabel(
            main_frame,
            text="Version 2.0 • Interface Moderne",
            font=("Segoe UI", 10),
            text_color=ModernTheme.TEXT_MUTED
        )
        version_label.pack(side="bottom", pady=20)
    
    def start_loading(self):
        """Démarre le processus de chargement"""
        def loading_process():
            steps = [
                ("Chargement des modules...", 0.2),
                ("Configuration du thème...", 0.4),
                ("Chargement des données...", 0.6),
                ("Initialisation de l'interface...", 0.8),
                ("Finalisation...", 1.0)
            ]
            
            for step_text, progress in steps:
                self.after(0, lambda t=step_text, p=progress: self.update_progress(t, p))
                time.sleep(0.5)
            
            # Simule le chargement des données
            self.after(0, self.load_app_data)
        
        # Lance le chargement dans un thread séparé
        threading.Thread(target=loading_process, daemon=True).start()
    
    def update_progress(self, text: str, progress: float):
        """Met à jour la barre de progression"""
        self.status_label.configure(text=text)
        self.progress_bar.set(progress)
    
    def load_app_data(self):
        """Charge les données de l'application"""
        try:
            # Chargement réel des données
            load_data()
            self.status_label.configure(text="Lancement de l'application...")
            
            # Attend un peu puis lance l'app principale
            self.after(1000, self.launch_main_app)
            
        except Exception as e:
            self.status_label.configure(text=f"Erreur: {str(e)}")
            self.after(3000, self.quit)
    
    def launch_main_app(self):
        """Lance l'application principale"""
        self.withdraw()  # Cache le splash screen
        
        # Lance l'application principale
        main_app = ModernLauncherApp()
        main_app.mainloop()
        
        # Ferme le splash screen
        self.quit()

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
        
        # Configuration de l'interface
        self.setup_ui()
        
        # Centre la fenêtre
        self.center_window()
        
        # Gestion de la fermeture
        self.protocol("WM_DELETE_WINDOW", self.on_closing)
    
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
    
    def on_closing(self):
        """Gestion de la fermeture de l'application"""
        # Optionnel: sauvegarder les données
        self.quit()

def main():
    """Fonction principale avec splash screen"""
    try:
        # Vérification des dépendances
        import customtkinter
        from PIL import Image
        print("✅ Toutes les dépendances sont installées")
        
        # Lance le splash screen
        splash = SplashScreen()
        splash.mainloop()
        
    except ImportError as e:
        print(f"❌ Erreur d'import : {e}")
        print("Installez les dépendances avec : pip install customtkinter pillow")
        input("Appuyez sur Entrée pour fermer...")
    except Exception as e:
        print(f"❌ Erreur : {e}")
        import traceback
        traceback.print_exc()
        input("Appuyez sur Entrée pour fermer...")

if __name__ == "__main__":
    main()
