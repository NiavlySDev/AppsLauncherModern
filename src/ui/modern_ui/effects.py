import customtkinter as ctk
from .theme import ModernTheme
import tkinter as tk

class AnimatedButton(ctk.CTkButton):
    """Bouton avec animations fluides"""
    
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        self.original_fg_color = self._fg_color
        self.animation_running = False
        
        # Bind des événements
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)
        self.bind("<Button-1>", self.on_click)
    
    def on_enter(self, event):
        """Animation d'entrée"""
        if not self.animation_running:
            self.animate_color(self._fg_color, self._hover_color, duration=150)
    
    def on_leave(self, event):
        """Animation de sortie"""
        if not self.animation_running:
            self.animate_color(self._fg_color, self.original_fg_color, duration=150)
    
    def on_click(self, event):
        """Animation de clic"""
        self.animate_scale(0.95, duration=100)
    
    def animate_color(self, start_color, end_color, duration=200):
        """Anime la transition de couleur"""
        # Simplification : changement direct pour customtkinter
        if hasattr(self, '_hover_color'):
            self.configure(fg_color=end_color)
    
    def animate_scale(self, scale, duration=100):
        """Anime l'échelle du bouton"""
        # Note: customtkinter ne supporte pas facilement les animations d'échelle
        # On peut simuler avec un effet de couleur
        original_color = self._fg_color
        darker_color = self.darken_color(original_color)
        
        self.configure(fg_color=darker_color)
        self.after(duration, lambda: self.configure(fg_color=original_color))
    
    def darken_color(self, color, factor=0.8):
        """Assombrit une couleur"""
        if isinstance(color, str) and color.startswith('#'):
            # Conversion hex vers RGB
            r = int(color[1:3], 16)
            g = int(color[3:5], 16)
            b = int(color[5:7], 16)
            
            # Assombrissement
            r = int(r * factor)
            g = int(g * factor)
            b = int(b * factor)
            
            return f"#{r:02x}{g:02x}{b:02x}"
        return color

class GradientFrame(ctk.CTkFrame):
    """Frame avec effet de dégradé simulé"""
    
    def __init__(self, parent, start_color, end_color, **kwargs):
        super().__init__(parent, **kwargs)
        self.start_color = start_color
        self.end_color = end_color
        
        # Pour customtkinter, on simule avec une couleur intermédiaire
        self.configure(fg_color=self.blend_colors(start_color, end_color, 0.5))
    
    def blend_colors(self, color1, color2, ratio):
        """Mélange deux couleurs"""
        if color1.startswith('#') and color2.startswith('#'):
            # Conversion et mélange
            r1, g1, b1 = int(color1[1:3], 16), int(color1[3:5], 16), int(color1[5:7], 16)
            r2, g2, b2 = int(color2[1:3], 16), int(color2[3:5], 16), int(color2[5:7], 16)
            
            r = int(r1 * (1 - ratio) + r2 * ratio)
            g = int(g1 * (1 - ratio) + g2 * ratio)
            b = int(b1 * (1 - ratio) + b2 * ratio)
            
            return f"#{r:02x}{g:02x}{b:02x}"
        return color1

class ModernScrollbar(ctk.CTkScrollbar):
    """Scrollbar moderne personnalisée"""
    
    def __init__(self, parent, **kwargs):
        super().__init__(
            parent,
            button_color=ModernTheme.PRIMARY,
            button_hover_color=ModernTheme.PRIMARY_HOVER,
            **kwargs
        )

class StatusBar(ctk.CTkFrame):
    """Barre de statut moderne"""
    
    def __init__(self, parent, **kwargs):
        super().__init__(
            parent,
            height=30,
            fg_color=ModernTheme.BG_SECONDARY,
            **kwargs
        )
        
        self.grid_columnconfigure(1, weight=1)
        
        # Indicateur de statut
        self.status_label = ctk.CTkLabel(
            self,
            text="Prêt",
            font=ModernTheme.FONT_SMALL,
            text_color=ModernTheme.TEXT_SECONDARY
        )
        self.status_label.grid(row=0, column=0, padx=10, sticky="w")
        
        # Espace flexible
        spacer = ctk.CTkFrame(self, fg_color="transparent")
        spacer.grid(row=0, column=1, sticky="ew")
        
        # Informations supplémentaires
        self.info_label = ctk.CTkLabel(
            self,
            text="",
            font=ModernTheme.FONT_SMALL,
            text_color=ModernTheme.TEXT_MUTED
        )
        self.info_label.grid(row=0, column=2, padx=10, sticky="e")
    
    def set_status(self, message, status_type="info"):
        """Met à jour le statut"""
        colors = {
            "info": ModernTheme.TEXT_SECONDARY,
            "success": ModernTheme.SUCCESS,
            "warning": ModernTheme.WARNING,
            "error": ModernTheme.ERROR
        }
        
        self.status_label.configure(
            text=message,
            text_color=colors.get(status_type, ModernTheme.TEXT_SECONDARY)
        )
    
    def set_info(self, message):
        """Met à jour les informations"""
        self.info_label.configure(text=message)

class LoadingSpinner(ctk.CTkFrame):
    """Indicateur de chargement moderne"""
    
    def __init__(self, parent, **kwargs):
        super().__init__(
            parent,
            fg_color="transparent",
            **kwargs
        )
        
        self.is_spinning = False
        self.angle = 0
        
        # Texte de chargement
        self.loading_label = ctk.CTkLabel(
            self,
            text="Chargement...",
            font=ModernTheme.FONT_MEDIUM,
            text_color=ModernTheme.TEXT_SECONDARY
        )
        self.loading_label.pack(pady=20)
        
        # Indicateur visuel simple
        self.spinner_label = ctk.CTkLabel(
            self,
            text="⟳",
            font=("Segoe UI", 24),
            text_color=ModernTheme.PRIMARY
        )
        self.spinner_label.pack()
    
    def start_spinning(self):
        """Démarre l'animation de chargement"""
        self.is_spinning = True
        self.spin()
    
    def stop_spinning(self):
        """Arrête l'animation"""
        self.is_spinning = False
    
    def spin(self):
        """Animation de rotation"""
        if self.is_spinning:
            # Rotation des caractères de spinner
            spinners = ["⟳", "⟲", "⟳", "⟲"]
            current = spinners[self.angle % len(spinners)]
            self.spinner_label.configure(text=current)
            self.angle += 1
            
            # Continue l'animation
            self.after(200, self.spin)
