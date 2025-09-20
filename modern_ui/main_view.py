import customtkinter as ctk
from .components import ModernCard, ModernButton, ModernHeader, ModernGrid
from .theme import ModernTheme
from .effects import StatusBar, LoadingSpinner
from data import get_categories

class ModernMainView(ctk.CTkFrame):
    """Vue principale moderne avec grille de catégories"""
    
    def __init__(self, parent, **kwargs):
        super().__init__(
            parent,
            fg_color=ModernTheme.BG_PRIMARY,
            **kwargs
        )
        
        self.parent = parent
        self.setup_ui()
        self.refresh_categories()
    
    def setup_ui(self):
        """Configure l'interface utilisateur"""
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        
        # En-tête
        self.header = ModernHeader(
            self,
            title="Lanceur d'Applications",
            subtitle="Organisez et lancez vos applications favorites"
        )
        self.header.grid(row=0, column=0, sticky="ew", padx=0, pady=0)
        
        # Conteneur principal
        main_container = ctk.CTkFrame(self, fg_color="transparent")
        main_container.grid(row=1, column=0, sticky="nsew", padx=20, pady=20)
        main_container.grid_columnconfigure(0, weight=1)
        main_container.grid_rowconfigure(0, weight=1)
        
        # Grille de catégories
        self.categories_grid = ModernGrid(main_container)
        self.categories_grid.grid(row=0, column=0, sticky="nsew")
        
        # Bouton d'ajout
        self.add_button = ModernButton(
            main_container,
            text="+ Nouvelle Catégorie",
            style="primary",
            command=self.open_add_category,
            height=50,
            font=ModernTheme.FONT_MEDIUM
        )
        self.add_button.grid(row=1, column=0, pady=(20, 0), sticky="ew")
        
        # Barre de statut
        self.status_bar = StatusBar(self)
        self.status_bar.grid(row=2, column=0, sticky="ew", padx=0, pady=0)
    
    def refresh_categories(self):
        """Actualise l'affichage des catégories"""
        self.categories_grid.clear_cards()
        
        # Met à jour la barre de statut
        self.status_bar.set_status("Chargement des catégories...", "info")
        
        categories = get_categories()
        if not categories:
            # Message si aucune catégorie
            empty_label = ctk.CTkLabel(
                self.categories_grid,
                text="Aucune catégorie trouvée\nCommencez par créer votre première catégorie !",
                font=ModernTheme.FONT_MEDIUM,
                text_color=ModernTheme.TEXT_MUTED,
                justify="center"
            )
            empty_label.grid(row=0, column=0, pady=50)
            
            self.status_bar.set_status("Aucune catégorie", "warning")
            self.status_bar.set_info("")
            return
        
        # Création des cartes de catégories
        for cat_id, category in categories.items():
            # Comptage des applications
            app_count = len(category.get("applications", {}))
            subtitle = f"{app_count} application{'s' if app_count != 1 else ''}"
            
            card = ModernCard(
                self.categories_grid,
                title=category["name"],
                subtitle=subtitle,
                click_callback=lambda cid=cat_id: self.show_category(cid),
                width=280,
                height=140
            )
            
            # Personnalisation de l'icône avec emoji ou couleur de catégorie
            if category.get("icon"):
                # Remplace l'icône par défaut par l'emoji
                card.icon_label.configure(
                    text=category["icon"],
                    font=("Segoe UI Emoji", 32),
                    fg_color="transparent"
                )
            elif category.get("color"):
                # Utilise la couleur de la catégorie
                card.icon_label.configure(fg_color=category["color"])
            
            self.categories_grid.add_card(card)
        
        # Met à jour la barre de statut
        total_apps = sum(len(cat.get("applications", {})) for cat in categories.values())
        self.status_bar.set_status("Prêt", "success")
        self.status_bar.set_info(f"{len(categories)} catégories • {total_apps} applications")
    
    def open_add_category(self):
        """Ouvre le dialogue d'ajout de catégorie"""
        from .dialogs import ModernAddCategoryDialog
        
        def on_category_added():
            self.refresh_categories()
        
        dialog = ModernAddCategoryDialog(self, callback=on_category_added)
        dialog.grab_set()  # Modal
    
    def show_category(self, category_id):
        """Affiche une catégorie spécifique"""
        from .category_view import ModernCategoryView
        
        # Efface la vue actuelle
        for widget in self.parent.winfo_children():
            widget.destroy()
        
        # Affiche la vue de catégorie
        category_view = ModernCategoryView(
            self.parent,
            category_id=category_id,
            back_callback=self.go_back
        )
        category_view.pack(fill="both", expand=True)
    
    def go_back(self):
        """Retourne à la vue principale"""
        for widget in self.parent.winfo_children():
            widget.destroy()
        
        main_view = ModernMainView(self.parent)
        main_view.pack(fill="both", expand=True)
