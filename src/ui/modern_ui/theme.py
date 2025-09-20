import customtkinter as ctk
from typing import Dict, Any, Callable

# Configuration du thème moderne
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class ModernTheme:
    # Couleurs principales
    PRIMARY = "#1f538d"
    PRIMARY_HOVER = "#14375e"
    SECONDARY = "#2b2b2b"
    ACCENT = "#00d4ff"
    
    # Arrière-plans
    BG_PRIMARY = "#212121"
    BG_SECONDARY = "#2b2b2b"
    BG_CARD = "#363636"
    BG_CARD_HOVER = "#404040"
    
    # Textes
    TEXT_PRIMARY = "#ffffff"
    TEXT_SECONDARY = "#b0b0b0"
    TEXT_MUTED = "#808080"
    
    # Bordures et ombres
    BORDER = "#404040"
    SHADOW = "#00000030"
    
    # Statuts
    SUCCESS = "#4caf50"
    WARNING = "#ff9800"
    ERROR = "#f44336"
    
    # Polices
    FONT_LARGE = ("Segoe UI", 24, "bold")
    FONT_MEDIUM = ("Segoe UI", 16)
    FONT_NORMAL = ("Segoe UI", 12)
    FONT_SMALL = ("Segoe UI", 10)
    
    # Espacements
    PADDING_LARGE = 24
    PADDING_MEDIUM = 16
    PADDING_SMALL = 8
    
    # Bordures arrondies
    CORNER_RADIUS = 12
    CORNER_RADIUS_SMALL = 8
