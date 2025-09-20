import customtkinter as ctk
from PIL import Image
from .theme import ModernTheme
from typing import Callable, Optional

class ModernCard(ctk.CTkFrame):
    """Carte moderne avec effet hover et animation"""
    
    def __init__(self, parent, title: str, subtitle: str = "", icon_path: Optional[str] = None, 
                 click_callback: Optional[Callable] = None, **kwargs):
        
        super().__init__(
            parent,
            fg_color=ModernTheme.BG_CARD,
            corner_radius=ModernTheme.CORNER_RADIUS,
            border_width=1,
            border_color=ModernTheme.BORDER,
            **kwargs
        )
        
        self.title = title
        self.subtitle = subtitle
        self.click_callback = click_callback
        self.setup_ui()
        self.setup_bindings()
    
    def setup_ui(self):
        # Configuration de la grille
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(2, weight=1)
        
        # Icône (si fournie)
        if hasattr(self, 'icon_path') and self.icon_path:
            try:
                icon_image = ctk.CTkImage(
                    light_image=Image.open(self.icon_path),
                    dark_image=Image.open(self.icon_path),
                    size=(48, 48)
                )
                self.icon_label = ctk.CTkLabel(
                    self,
                    image=icon_image,
                    text="",
                    fg_color="transparent"
                )
                self.icon_label.grid(row=0, column=0, pady=(20, 10), sticky="n")
            except:
                self.create_fallback_icon()
        else:
            self.create_fallback_icon()
        
        # Titre
        self.title_label = ctk.CTkLabel(
            self,
            text=self.title,
            font=ModernTheme.FONT_MEDIUM,
            text_color=ModernTheme.TEXT_PRIMARY
        )
        self.title_label.grid(row=1, column=0, pady=(0, 5), sticky="ew", padx=20)
        
        # Sous-titre (si fourni)
        if self.subtitle:
            self.subtitle_label = ctk.CTkLabel(
                self,
                text=self.subtitle,
                font=ModernTheme.FONT_SMALL,
                text_color=ModernTheme.TEXT_SECONDARY
            )
            self.subtitle_label.grid(row=2, column=0, pady=(0, 20), sticky="ew", padx=20)
    
    def create_fallback_icon(self):
        """Crée une icône par défaut avec les initiales"""
        if not hasattr(self, 'title'):
            return
            
        initials = "".join([word[0].upper() for word in self.title.split()[:2]])
        
        self.icon_label = ctk.CTkLabel(
            self,
            text=initials,
            font=("Segoe UI", 18, "bold"),
            text_color=ModernTheme.TEXT_PRIMARY,
            fg_color=ModernTheme.PRIMARY,
            corner_radius=24,
            width=48,
            height=48
        )
        self.icon_label.grid(row=0, column=0, pady=(20, 10), sticky="n")
    
    def setup_bindings(self):
        """Configure les événements de clic et hover"""
        if self.click_callback:
            widgets_to_bind = [self, self.icon_label, self.title_label]
            if hasattr(self, 'subtitle_label'):
                widgets_to_bind.append(self.subtitle_label)
            
            for widget in widgets_to_bind:
                widget.bind("<Button-1>", lambda e: self.click_callback())
                widget.configure(cursor="hand2")
                
                # Effets hover
                widget.bind("<Enter>", self.on_enter)
                widget.bind("<Leave>", self.on_leave)
    
    def on_enter(self, event):
        """Effet hover à l'entrée"""
        self.configure(fg_color=ModernTheme.BG_CARD_HOVER)
    
    def on_leave(self, event):
        """Effet hover à la sortie"""
        self.configure(fg_color=ModernTheme.BG_CARD)

class ModernButton(ctk.CTkButton):
    """Bouton moderne avec styles prédéfinis"""
    
    def __init__(self, parent, text: str, style: str = "primary", **kwargs):
        
        styles = {
            "primary": {
                "fg_color": ModernTheme.PRIMARY,
                "hover_color": ModernTheme.PRIMARY_HOVER,
                "text_color": ModernTheme.TEXT_PRIMARY,
                "corner_radius": ModernTheme.CORNER_RADIUS_SMALL,
                "font": ModernTheme.FONT_NORMAL,
                "height": 40
            },
            "secondary": {
                "fg_color": ModernTheme.BG_SECONDARY,
                "hover_color": ModernTheme.BG_CARD,
                "text_color": ModernTheme.TEXT_PRIMARY,
                "border_width": 1,
                "border_color": ModernTheme.BORDER,
                "corner_radius": ModernTheme.CORNER_RADIUS_SMALL,
                "font": ModernTheme.FONT_NORMAL,
                "height": 40
            },
            "success": {
                "fg_color": ModernTheme.SUCCESS,
                "hover_color": "#45a049",
                "text_color": ModernTheme.TEXT_PRIMARY,
                "corner_radius": ModernTheme.CORNER_RADIUS_SMALL,
                "font": ModernTheme.FONT_NORMAL,
                "height": 40
            }
        }
        
        button_style = styles.get(style, styles["primary"])
        button_style.update(kwargs)
        
        super().__init__(parent, text=text, **button_style)

class ModernHeader(ctk.CTkFrame):
    """En-tête moderne avec titre et boutons d'action"""
    
    def __init__(self, parent, title: str, subtitle: str = "", back_callback: Optional[Callable] = None, show_theme_button: bool = True):
        super().__init__(
            parent,
            fg_color=ModernTheme.BG_SECONDARY,
            corner_radius=0,
            height=100
        )
        
        self.title = title
        self.subtitle = subtitle
        self.back_callback = back_callback
        self.show_theme_button = show_theme_button
        self.setup_ui()
    
    def setup_ui(self):
        self.grid_columnconfigure(1, weight=1)
        
        # Bouton retour (si callback fourni)
        if self.back_callback:
            self.back_btn = ModernButton(
                self,
                text="← Retour",
                style="secondary",
                command=self.back_callback,
                width=100
            )
            self.back_btn.grid(row=0, column=0, padx=20, pady=20, sticky="w")
        
        # Conteneur titre
        title_frame = ctk.CTkFrame(self, fg_color="transparent")
        title_frame.grid(row=0, column=1, sticky="ew", padx=20, pady=20)
        
        # Titre principal
        self.title_label = ctk.CTkLabel(
            title_frame,
            text=self.title,
            font=ModernTheme.FONT_LARGE,
            text_color=ModernTheme.TEXT_PRIMARY
        )
        self.title_label.pack(anchor="w")
        
        # Sous-titre (si fourni)
        if self.subtitle:
            self.subtitle_label = ctk.CTkLabel(
                title_frame,
                text=self.subtitle,
                font=ModernTheme.FONT_NORMAL,
                text_color=ModernTheme.TEXT_SECONDARY
            )
            self.subtitle_label.pack(anchor="w", pady=(5, 0))
        
        # Bouton de thème (si activé)
        if self.show_theme_button:
            self.theme_btn = ModernButton(
                self,
                text="🌙/☀️",
                style="secondary",
                command=self.toggle_theme,
                width=60,
                height=40
            )
            self.theme_btn.grid(row=0, column=2, padx=20, pady=20, sticky="e")
    
    def toggle_theme(self):
        """Bascule le thème"""
        from .theme_manager import theme_manager
        new_theme = theme_manager.toggle_dark_light()
        
        # Met à jour le texte du bouton
        if new_theme == "dark":
            self.theme_btn.configure(text="🌙")
        else:
            self.theme_btn.configure(text="☀️")

class ModernGrid(ctk.CTkScrollableFrame):
    """Grille responsive pour les cartes"""
    
    def __init__(self, parent, **kwargs):
        super().__init__(
            parent,
            fg_color=ModernTheme.BG_PRIMARY,
            **kwargs
        )
        
        self.cards = []
        self.columns = 4  # Nombre de colonnes par défaut
    
    def add_card(self, card: ModernCard):
        """Ajoute une carte à la grille"""
        row = len(self.cards) // self.columns
        col = len(self.cards) % self.columns
        
        card.grid(
            row=row, 
            column=col, 
            padx=ModernTheme.PADDING_MEDIUM,
            pady=ModernTheme.PADDING_MEDIUM,
            sticky="ew"
        )
        
        # Configuration responsive
        self.grid_columnconfigure(col, weight=1, minsize=250)
        
        self.cards.append(card)
    
    def clear_cards(self):
        """Supprime toutes les cartes"""
        for card in self.cards:
            card.destroy()
        self.cards.clear()
    
    def set_columns(self, columns: int):
        """Change le nombre de colonnes"""
        self.columns = columns
        self.refresh_layout()
    
    def refresh_layout(self):
        """Réorganise les cartes selon le nouveau nombre de colonnes"""
        for i, card in enumerate(self.cards):
            row = i // self.columns
            col = i % self.columns
            card.grid(row=row, column=col)
            self.grid_columnconfigure(col, weight=1, minsize=250)
