import customtkinter as ctk
from .theme import ModernTheme
from .components import ModernButton
from data import add_category, add_application
from tkinter import filedialog, messagebox
import os

class ModernDialog(ctk.CTkToplevel):
    """Classe de base pour les dialogues modernes"""
    
    def __init__(self, parent, title: str, width: int = 500, height: int = 400):
        super().__init__(parent)
        
        self.title(title)
        self.geometry(f"{width}x{height}")
        self.resizable(False, False)
        
        # Centre la fenêtre
        self.transient(parent)
        self.attributes('-topmost', True)
        
        # Configuration du style
        self.configure(fg_color=ModernTheme.BG_PRIMARY)
        
        self.setup_ui()
    
    def setup_ui(self):
        """À implémenter dans les sous-classes"""
        pass
    
    def center_window(self):
        """Centre la fenêtre sur l'écran"""
        self.update_idletasks()
        x = (self.winfo_screenwidth() // 2) - (self.winfo_width() // 2)
        y = (self.winfo_screenheight() // 2) - (self.winfo_height() // 2)
        self.geometry(f"+{x}+{y}")

class ModernAddCategoryDialog(ModernDialog):
    """Dialogue moderne pour ajouter une catégorie"""
    
    def __init__(self, parent, parent_category=None, callback=None):
        self.parent_category = parent_category
        self.callback = callback
        self.color_var = ctk.StringVar(value=ModernTheme.PRIMARY)
        self.icon_var = ctk.StringVar(value="📁")
        
        title = "Nouvelle Sous-catégorie" if parent_category else "Nouvelle Catégorie"
        super().__init__(parent, title, 450, 500)
        self.center_window()
    
    def setup_ui(self):
        # Padding principal
        main_frame = ctk.CTkFrame(self, fg_color="transparent")
        main_frame.pack(fill="both", expand=True, padx=30, pady=30)
        
        # Titre
        title_label = ctk.CTkLabel(
            main_frame,
            text="Créer une nouvelle catégorie",
            font=ModernTheme.FONT_LARGE,
            text_color=ModernTheme.TEXT_PRIMARY
        )
        title_label.pack(pady=(0, 30))
        
        # Nom de la catégorie
        name_label = ctk.CTkLabel(
            main_frame,
            text="Nom de la catégorie :",
            font=ModernTheme.FONT_MEDIUM,
            text_color=ModernTheme.TEXT_PRIMARY
        )
        name_label.pack(anchor="w", pady=(0, 10))
        
        self.name_entry = ctk.CTkEntry(
            main_frame,
            height=40,
            font=ModernTheme.FONT_NORMAL,
            placeholder_text="Ex: Jeux, Bureautique, Multimédia..."
        )
        self.name_entry.pack(fill="x", pady=(0, 20))
        self.name_entry.focus()
        
        # Sélection d'icône
        icon_label = ctk.CTkLabel(
            main_frame,
            text="Icône :",
            font=ModernTheme.FONT_MEDIUM,
            text_color=ModernTheme.TEXT_PRIMARY
        )
        icon_label.pack(anchor="w", pady=(0, 10))
        
        # Grille d'icônes prédéfinies
        icons_frame = ctk.CTkFrame(main_frame, fg_color=ModernTheme.BG_SECONDARY)
        icons_frame.pack(fill="x", pady=(0, 20))
        
        default_icons = ["📁", "🎮", "💼", "🔧", "📊", "🎵", "📷", "🌐", "📝", "⚡"]
        
        for i, icon in enumerate(default_icons):
            icon_btn = ctk.CTkButton(
                icons_frame,
                text=icon,
                width=40,
                height=40,
                font=("Segoe UI Emoji", 20),
                fg_color="transparent",
                command=lambda ic=icon: self.select_icon(ic)
            )
            icon_btn.grid(row=i//5, column=i%5, padx=5, pady=5)
        
        # Affichage de l'icône sélectionnée
        selected_frame = ctk.CTkFrame(main_frame, fg_color=ModernTheme.BG_SECONDARY)
        selected_frame.pack(fill="x", pady=(0, 20))
        
        ctk.CTkLabel(
            selected_frame,
            text="Icône sélectionnée :",
            font=ModernTheme.FONT_NORMAL
        ).pack(side="left", padx=10, pady=10)
        
        self.selected_icon_label = ctk.CTkLabel(
            selected_frame,
            text=self.icon_var.get(),
            font=("Segoe UI Emoji", 24),
            width=40,
            height=40,
            fg_color=self.color_var.get(),
            corner_radius=20
        )
        self.selected_icon_label.pack(side="right", padx=10, pady=10)
        
        # Sélection de couleur
        color_label = ctk.CTkLabel(
            main_frame,
            text="Couleur :",
            font=ModernTheme.FONT_MEDIUM,
            text_color=ModernTheme.TEXT_PRIMARY
        )
        color_label.pack(anchor="w", pady=(0, 10))
        
        colors_frame = ctk.CTkFrame(main_frame, fg_color=ModernTheme.BG_SECONDARY)
        colors_frame.pack(fill="x", pady=(0, 30))
        
        default_colors = [
            ModernTheme.PRIMARY, "#e53e3e", "#38a169", "#d69e2e", 
            "#805ad5", "#dd6b20", "#319795", "#e53e3e"
        ]
        
        for i, color in enumerate(default_colors):
            color_btn = ctk.CTkButton(
                colors_frame,
                text="",
                width=30,
                height=30,
                fg_color=color,
                command=lambda c=color: self.select_color(c)
            )
            color_btn.grid(row=0, column=i, padx=5, pady=10)
        
        # Boutons d'action
        buttons_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
        buttons_frame.pack(fill="x", pady=(20, 0))
        buttons_frame.grid_columnconfigure(0, weight=1)
        buttons_frame.grid_columnconfigure(1, weight=1)
        
        cancel_btn = ModernButton(
            buttons_frame,
            text="Annuler",
            style="secondary",
            command=self.destroy
        )
        cancel_btn.grid(row=0, column=0, padx=(0, 10), sticky="ew")
        
        create_btn = ModernButton(
            buttons_frame,
            text="Créer",
            style="primary",
            command=self.create_category
        )
        create_btn.grid(row=0, column=1, padx=(10, 0), sticky="ew")
        
        # Bind Enter pour créer
        self.bind('<Return>', lambda e: self.create_category())
    
    def select_icon(self, icon):
        """Sélectionne une icône"""
        self.icon_var.set(icon)
        self.selected_icon_label.configure(text=icon)
    
    def select_color(self, color):
        """Sélectionne une couleur"""
        self.color_var.set(color)
        self.selected_icon_label.configure(fg_color=color)
    
    def create_category(self):
        """Crée la catégorie"""
        name = self.name_entry.get().strip()
        
        if not name:
            messagebox.showerror("Erreur", "Veuillez entrer un nom pour la catégorie")
            return
        
        try:
            add_category(
                name=name,
                icon=self.icon_var.get(),
                color=self.color_var.get(),
                parent=self.parent_category
            )
            
            if self.callback:
                self.callback()
            
            self.destroy()
            
        except Exception as e:
            messagebox.showerror("Erreur", f"Erreur lors de la création : {str(e)}")

class ModernAddApplicationDialog(ModernDialog):
    """Dialogue moderne pour ajouter une application"""
    
    def __init__(self, parent, category_id, callback=None):
        self.category_id = category_id
        self.callback = callback
        self.selected_path = ""
        
        super().__init__(parent, "Nouvelle Application", 500, 400)
        self.center_window()
    
    def setup_ui(self):
        # Padding principal
        main_frame = ctk.CTkFrame(self, fg_color="transparent")
        main_frame.pack(fill="both", expand=True, padx=30, pady=30)
        
        # Titre
        title_label = ctk.CTkLabel(
            main_frame,
            text="Ajouter une application",
            font=ModernTheme.FONT_LARGE,
            text_color=ModernTheme.TEXT_PRIMARY
        )
        title_label.pack(pady=(0, 30))
        
        # Sélection de fichier
        file_frame = ctk.CTkFrame(main_frame, fg_color=ModernTheme.BG_SECONDARY)
        file_frame.pack(fill="x", pady=(0, 20))
        
        file_label = ctk.CTkLabel(
            file_frame,
            text="Fichier :",
            font=ModernTheme.FONT_MEDIUM,
            text_color=ModernTheme.TEXT_PRIMARY
        )
        file_label.pack(anchor="w", padx=20, pady=(15, 5))
        
        file_select_frame = ctk.CTkFrame(file_frame, fg_color="transparent")
        file_select_frame.pack(fill="x", padx=20, pady=(0, 15))
        file_select_frame.grid_columnconfigure(0, weight=1)
        
        self.path_entry = ctk.CTkEntry(
            file_select_frame,
            height=40,
            font=ModernTheme.FONT_NORMAL,
            placeholder_text="Chemin vers le fichier ou raccourci..."
        )
        self.path_entry.grid(row=0, column=0, sticky="ew", padx=(0, 10))
        
        browse_btn = ModernButton(
            file_select_frame,
            text="Parcourir",
            style="secondary",
            command=self.browse_file,
            width=100
        )
        browse_btn.grid(row=0, column=1)
        
        # Nom de l'application
        name_label = ctk.CTkLabel(
            main_frame,
            text="Nom de l'application :",
            font=ModernTheme.FONT_MEDIUM,
            text_color=ModernTheme.TEXT_PRIMARY
        )
        name_label.pack(anchor="w", pady=(0, 10))
        
        self.name_entry = ctk.CTkEntry(
            main_frame,
            height=40,
            font=ModernTheme.FONT_NORMAL,
            placeholder_text="Nom affiché dans le lanceur..."
        )
        self.name_entry.pack(fill="x", pady=(0, 20))
        
        # Aperçu de l'icône (placeholder)
        preview_frame = ctk.CTkFrame(main_frame, fg_color=ModernTheme.BG_SECONDARY)
        preview_frame.pack(fill="x", pady=(0, 30))
        
        preview_label = ctk.CTkLabel(
            preview_frame,
            text="Aperçu :",
            font=ModernTheme.FONT_MEDIUM,
            text_color=ModernTheme.TEXT_PRIMARY
        )
        preview_label.pack(anchor="w", padx=20, pady=(15, 5))
        
        self.icon_preview = ctk.CTkLabel(
            preview_frame,
            text="🔧",
            font=("Segoe UI Emoji", 32),
            width=60,
            height=60,
            fg_color=ModernTheme.PRIMARY,
            corner_radius=30
        )
        self.icon_preview.pack(pady=(0, 15))
        
        # Boutons d'action
        buttons_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
        buttons_frame.pack(fill="x", pady=(20, 0))
        buttons_frame.grid_columnconfigure(0, weight=1)
        buttons_frame.grid_columnconfigure(1, weight=1)
        
        cancel_btn = ModernButton(
            buttons_frame,
            text="Annuler",
            style="secondary",
            command=self.destroy
        )
        cancel_btn.grid(row=0, column=0, padx=(0, 10), sticky="ew")
        
        add_btn = ModernButton(
            buttons_frame,
            text="Ajouter",
            style="primary",
            command=self.add_application
        )
        add_btn.grid(row=0, column=1, padx=(10, 0), sticky="ew")
        
        # Bind Enter pour ajouter
        self.bind('<Return>', lambda e: self.add_application())
    
    def browse_file(self):
        """Ouvre le dialogue de sélection de fichier"""
        file_types = [
            ("Tous les fichiers", "*.*"),
            ("Raccourcis", "*.lnk"),
            ("Exécutables", "*.exe"),
            ("Raccourcis URL", "*.url")
        ]
        
        filename = filedialog.askopenfilename(
            title="Sélectionner une application",
            filetypes=file_types,
            initialdir=os.path.expanduser("~/Desktop")
        )
        
        if filename:
            self.selected_path = filename
            self.path_entry.delete(0, 'end')
            self.path_entry.insert(0, filename)
            
            # Auto-remplissage du nom
            if not self.name_entry.get():
                app_name = os.path.splitext(os.path.basename(filename))[0]
                # Nettoie le nom (enlève les mots comme "Shortcut")
                app_name = app_name.replace(" - Shortcut", "").replace(" Shortcut", "")
                self.name_entry.delete(0, 'end')
                self.name_entry.insert(0, app_name)
            
            # Mise à jour de l'aperçu
            self.update_preview()
    
    def update_preview(self):
        """Met à jour l'aperçu de l'icône"""
        if self.selected_path:
            # Détermine le type d'application
            if ".lnk" in self.selected_path.lower():
                self.icon_preview.configure(text="🔗", fg_color="#43a047")
            elif "steam" in self.selected_path.lower():
                self.icon_preview.configure(text="🎮", fg_color="#1e88e5")
            elif ".exe" in self.selected_path.lower():
                self.icon_preview.configure(text="⚙️", fg_color="#fb8c00")
            else:
                self.icon_preview.configure(text="📄", fg_color=ModernTheme.PRIMARY)
    
    def add_application(self):
        """Ajoute l'application"""
        name = self.name_entry.get().strip()
        path = self.path_entry.get().strip()
        
        if not name:
            messagebox.showerror("Erreur", "Veuillez entrer un nom pour l'application")
            return
            
        if not path:
            messagebox.showerror("Erreur", "Veuillez sélectionner un fichier")
            return
        
        if not os.path.exists(path):
            messagebox.showerror("Erreur", "Le fichier sélectionné n'existe pas")
            return
        
        try:
            # Détermine s'il s'agit d'un raccourci
            if path.lower().endswith(('.lnk', '.url')):
                add_application(
                    category_id=self.category_id,
                    name=name,
                    shortcut_path=path
                )
            else:
                add_application(
                    category_id=self.category_id,
                    name=name,
                    path=path
                )
            
            if self.callback:
                self.callback()
            
            self.destroy()
            
        except Exception as e:
            messagebox.showerror("Erreur", f"Erreur lors de l'ajout : {str(e)}")
