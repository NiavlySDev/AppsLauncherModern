import customtkinter as ctk
from .components import ModernCard, ModernButton, ModernHeader, ModernGrid
from .theme import ModernTheme
from data import get_category, get_applications_for_category, launch_application
from icon_manager import IconManager
from PIL import Image
import os

class ModernCategoryView(ctk.CTkFrame):
    """Vue moderne d'une catégorie avec ses applications"""
    
    def __init__(self, parent, category_id: str, back_callback=None, **kwargs):
        super().__init__(
            parent,
            fg_color=ModernTheme.BG_PRIMARY,
            **kwargs
        )
        
        self.parent = parent
        self.category_id = category_id
        self.back_callback = back_callback
        self.category = get_category(category_id)
        
        if not self.category:
            self.show_error()
            return
            
        self.setup_ui()
        self.refresh_applications()
    
    def setup_ui(self):
        """Configure l'interface utilisateur"""
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        
        # En-tête avec nom de catégorie et bouton retour
        app_count = len(self.category.get("applications", {}))
        subtitle = f"{app_count} application{'s' if app_count != 1 else ''}"
        
        self.header = ModernHeader(
            self,
            title=self.category["name"],
            subtitle=subtitle,
            back_callback=self.back_callback
        )
        self.header.grid(row=0, column=0, sticky="ew")
        
        # Conteneur principal
        main_container = ctk.CTkFrame(self, fg_color="transparent")
        main_container.grid(row=1, column=0, sticky="nsew", padx=20, pady=20)
        main_container.grid_columnconfigure(0, weight=1)
        main_container.grid_rowconfigure(0, weight=1)
        
        # Grille d'applications
        self.apps_grid = ModernGrid(main_container)
        self.apps_grid.grid(row=0, column=0, sticky="nsew")
        
        # Boutons d'actions
        actions_frame = ctk.CTkFrame(main_container, fg_color="transparent")
        actions_frame.grid(row=1, column=0, pady=(20, 0), sticky="ew")
        actions_frame.grid_columnconfigure(0, weight=1)
        actions_frame.grid_columnconfigure(1, weight=1)
        
        self.add_app_button = ModernButton(
            actions_frame,
            text="+ Nouvelle Application",
            style="primary",
            command=self.open_add_application
        )
        self.add_app_button.grid(row=0, column=0, padx=(0, 10), sticky="ew")
        
        self.add_subcat_button = ModernButton(
            actions_frame,
            text="+ Sous-catégorie",
            style="secondary",
            command=self.open_add_subcategory
        )
        self.add_subcat_button.grid(row=0, column=1, padx=(10, 0), sticky="ew")
    
    def refresh_applications(self):
        """Actualise l'affichage des applications"""
        self.apps_grid.clear_cards()
        
        applications = get_applications_for_category(self.category_id)
        
        if not applications:
            # Message si aucune application
            empty_label = ctk.CTkLabel(
                self.apps_grid,
                text="Aucune application dans cette catégorie\nAjoutez votre première application !",
                font=ModernTheme.FONT_MEDIUM,
                text_color=ModernTheme.TEXT_MUTED,
                justify="center"
            )
            empty_label.grid(row=0, column=0, pady=50)
            return
        
        # Création des cartes d'applications
        for app_id, app in applications.items():
            # Informations de l'application
            app_name = app["name"]
            app_path = app.get("shortcut_path", app.get("path", ""))
            
            # Type d'application
            if app.get("shortcut_path"):
                app_type = "Raccourci"
            elif "steam" in app_path.lower():
                app_type = "Jeu Steam"
            else:
                app_type = "Application"
            
            # Création de la carte
            card = ModernApplicationCard(
                self.apps_grid,
                app_name=app_name,
                app_type=app_type,
                app_path=app_path,
                click_callback=lambda aid=app_id: self.launch_app(aid),
                width=280,
                height=160
            )
            
            self.apps_grid.add_card(card)
    
    def launch_app(self, app_id: str):
        """Lance une application"""
        try:
            launch_application(self.category_id, app_id)
        except Exception as e:
            self.show_error_dialog(f"Erreur lors du lancement : {str(e)}")
    
    def open_add_application(self):
        """Ouvre le dialogue d'ajout d'application"""
        from .dialogs import ModernAddApplicationDialog
        
        def on_app_added():
            self.refresh_applications()
            # Met à jour le sous-titre du header
            app_count = len(get_applications_for_category(self.category_id))
            subtitle = f"{app_count} application{'s' if app_count != 1 else ''}"
            self.header.subtitle_label.configure(text=subtitle)
        
        dialog = ModernAddApplicationDialog(
            self, 
            category_id=self.category_id,
            callback=on_app_added
        )
        dialog.grab_set()
    
    def open_add_subcategory(self):
        """Ouvre le dialogue d'ajout de sous-catégorie"""
        from .dialogs import ModernAddCategoryDialog
        
        def on_subcat_added():
            self.refresh_applications()
        
        dialog = ModernAddCategoryDialog(
            self, 
            parent_category=self.category_id,
            callback=on_subcat_added
        )
        dialog.grab_set()
    
    def show_error(self):
        """Affiche un message d'erreur si la catégorie n'existe pas"""
        error_label = ctk.CTkLabel(
            self,
            text="Catégorie introuvable",
            font=ModernTheme.FONT_LARGE,
            text_color=ModernTheme.ERROR
        )
        error_label.pack(expand=True)
    
    def show_error_dialog(self, message: str):
        """Affiche une boîte de dialogue d'erreur"""
        dialog = ctk.CTkToplevel(self)
        dialog.title("Erreur")
        dialog.geometry("400x200")
        dialog.resizable(False, False)
        
        # Centre la fenêtre
        dialog.transient(self)
        dialog.grab_set()
        
        # Message d'erreur
        error_label = ctk.CTkLabel(
            dialog,
            text=message,
            font=ModernTheme.FONT_MEDIUM,
            text_color=ModernTheme.ERROR,
            wraplength=350
        )
        error_label.pack(pady=40, padx=20)
        
        # Bouton OK
        ok_button = ModernButton(
            dialog,
            text="OK",
            style="primary",
            command=dialog.destroy
        )
        ok_button.pack(pady=20)

class ModernApplicationCard(ModernCard):
    """Carte spécialisée pour les applications avec icône"""
    
    def __init__(self, parent, app_name: str, app_type: str, app_path: str, 
                 click_callback=None, **kwargs):
        
        self.app_name = app_name
        self.app_type = app_type
        self.app_path = app_path
        
        # Appel du constructeur parent
        super().__init__(
            parent,
            title=app_name,
            subtitle=app_type,
            click_callback=click_callback,
            **kwargs
        )
        
        # Charge l'icône après que l'interface soit créée
        self.after_idle(self.load_app_icon)
    
    def load_app_icon(self):
        """Charge l'icône spécifique de l'application"""
        try:
            # Utilise le gestionnaire d'icônes pour obtenir l'icône
            icon_manager = IconManager()
            icon_path = icon_manager.get_icon_for_app(self.app_name, self.app_path)
            
            if icon_path and os.path.exists(icon_path):
                print(f"🔍 Tentative de chargement: {icon_path}")
                
                # Charge l'icône depuis le fichier
                pil_image = Image.open(icon_path)
                print(f"📏 Image chargée: {pil_image.size} {pil_image.mode}")
                
                # S'assurer que l'image est en RGBA
                if pil_image.mode != 'RGBA':
                    pil_image = pil_image.convert('RGBA')
                
                # Crée l'objet CTkImage avec les deux tailles
                icon_image = ctk.CTkImage(
                    light_image=pil_image,
                    dark_image=pil_image,
                    size=(48, 48)  # Taille d'affichage
                )
                
                self.icon_label.configure(
                    image=icon_image,
                    text="",  # Enlève le texte
                    fg_color="transparent"
                )
                
                # Force la mise à jour
                self.icon_label.update()
                
                print(f"✅ Icône chargée avec succès pour {self.app_name}")
                return
                
        except Exception as e:
            print(f"❌ Erreur lors du chargement de l'icône pour {self.app_name}: {e}")
            import traceback
            traceback.print_exc()
        
        # Fallback avec initiales colorées selon le type
        self.create_fallback_icon()
    
    def create_fallback_icon(self):
        """Crée une icône de fallback avec initiales pour applications"""
        color_map = {
            "Jeu Steam": "#1e88e5",
            "Raccourci": "#43a047", 
            "Application": "#fb8c00"
        }
        
        color = color_map.get(self.app_type, ModernTheme.PRIMARY)
        initials = "".join([word[0].upper() for word in self.app_name.split()[:2]])
        if not initials:
            initials = self.app_name[0].upper() if self.app_name else "?"
        
        # Met à jour l'icône existante
        if hasattr(self, 'icon_label') and self.icon_label:
            self.icon_label.configure(
                image=None,  # Enlève l'image
                text=initials,
                font=("Segoe UI", 16, "bold"),
                fg_color=color,
                text_color="white"
            )
            print(f"🎨 Icône fallback créée pour {self.app_name}: {initials}")
        else:
            # Utilise la méthode parent si icon_label n'existe pas encore
            super().create_fallback_icon()
