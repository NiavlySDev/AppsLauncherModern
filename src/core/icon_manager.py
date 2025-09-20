#!/usr/bin/env python3
"""Module pour la gestion des icônes d'applications."""

import os
import requests
import hashlib
import json
from PIL import Image, ImageTk
from urllib.parse import urlparse, quote
import tkinter as tk

# Dossier pour stocker les icônes
ICONS_DIR = "icons"
ICON_CACHE_FILE = "icon_cache.json"
# Augmenter la taille des icônes pour une meilleure qualité
ICON_SIZE = (128, 128)  # Taille standard des icônes (augmentée)
DISPLAY_SIZE = (32, 32)  # Taille d'affichage dans l'interface

class IconManager:
    def __init__(self):
        self.ensure_icons_dir()
        self.cache = self.load_cache()
    
    def ensure_icons_dir(self):
        """Crée le dossier d'icônes s'il n'existe pas"""
        if not os.path.exists(ICONS_DIR):
            os.makedirs(ICONS_DIR)
    
    def load_cache(self):
        """Charge le cache des icônes"""
        if os.path.exists(ICON_CACHE_FILE):
            try:
                with open(ICON_CACHE_FILE, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except:
                return {}
        return {}
    
    def save_cache(self):
        """Sauvegarde le cache des icônes"""
        try:
            with open(ICON_CACHE_FILE, 'w', encoding='utf-8') as f:
                json.dump(self.cache, f, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f"Erreur lors de la sauvegarde du cache: {e}")
    
    def get_app_icon_hash(self, app_name):
        """Génère un hash unique pour le nom de l'application"""
        return hashlib.md5(app_name.lower().encode('utf-8')).hexdigest()
    
    def search_icon_online(self, app_name):
        """Recherche une icône de haute qualité en ligne"""
        try:
            # Utiliser notre nouvelle API améliorée
            from ..utils.icon_api import icon_api
            return icon_api.find_best_icon(app_name)
            
        except Exception as e:
            print(f"Erreur lors de la recherche d'icône pour {app_name}: {e}")
            return None
    
    def clean_app_name(self, app_name):
        """Nettoie le nom de l'application pour améliorer la recherche"""
        # Supprimer les caractères spéciaux et les mots inutiles
        import re
        
        # Supprimer les versions, éditions, etc.
        clean_name = re.sub(r'\s*(v\d+|\d+\.\d+|edition|ultimate|professional|community|free).*$', '', app_name, flags=re.IGNORECASE)
        
        # Supprimer les caractères spéciaux
        clean_name = re.sub(r'[^\w\s]', '', clean_name)
        
        # Nettoyer les espaces
        clean_name = ' '.join(clean_name.split())
        
        return clean_name.strip()
    
    def download_and_process_icon(self, url, app_name):
        """Télécharge et traite une icône depuis une URL"""
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            }
            
            response = requests.get(url, headers=headers, timeout=30)
            response.raise_for_status()
            
            # Sauvegarder l'image temporairement
            app_hash = self.get_app_icon_hash(app_name)
            temp_path = os.path.join(ICONS_DIR, f"temp_{app_hash}")
            
            with open(temp_path, 'wb') as f:
                f.write(response.content)
            
            # Traiter l'image avec PIL
            final_path = self.process_icon_image(temp_path, app_name)
            
            # Supprimer le fichier temporaire
            if os.path.exists(temp_path):
                os.remove(temp_path)
            
            return final_path
            
        except Exception as e:
            print(f"Erreur lors du téléchargement: {e}")
            return None
    
    def process_icon_image(self, image_path, app_name):
        """Traite et améliore la qualité d'une image d'icône"""
        try:
            app_hash = self.get_app_icon_hash(app_name)
            final_path = os.path.join(ICONS_DIR, f"{app_hash}.png")
            
            # Détecter le type de fichier
            if image_path.lower().endswith('.svg') or self.is_svg_content(image_path):
                # Traiter les fichiers SVG
                img = self.convert_svg_to_png(image_path)
            else:
                # Ouvrir l'image normalement
                img = Image.open(image_path)
            
            if not img:
                return None
            
            # Convertir en RGBA si nécessaire
            if img.mode != 'RGBA':
                img = img.convert('RGBA')
            
            # Redimensionner avec un algorithme de haute qualité
            img = img.resize(ICON_SIZE, Image.Resampling.LANCZOS)
            
            # Améliorer la netteté si nécessaire
            from PIL import ImageEnhance
            enhancer = ImageEnhance.Sharpness(img)
            img = enhancer.enhance(1.2)
            
            # Sauvegarder en PNG de haute qualité
            img.save(final_path, 'PNG', optimize=True)
            
            # Mettre à jour le cache
            self.cache[app_name.lower()] = final_path
            self.save_cache()
            
            return final_path
            
        except Exception as e:
            print(f"Erreur lors du traitement de l'image: {e}")
            return None
    
    def is_svg_content(self, file_path):
        """Vérifie si un fichier contient du SVG"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read(1000)  # Lire les premiers 1000 caractères
                return '<svg' in content.lower()
        except:
            return False
    
    def convert_svg_to_png(self, svg_path):
        """Convertit un SVG en PNG"""
        try:
            # Essayer d'utiliser cairosvg si disponible
            try:
                import cairosvg
                from io import BytesIO
                
                # Convertir SVG en PNG
                png_data = cairosvg.svg2png(url=svg_path, output_width=ICON_SIZE[0], output_height=ICON_SIZE[1])
                
                # Charger en tant qu'image PIL
                img = Image.open(BytesIO(png_data))
                return img
                
            except ImportError:
                print("cairosvg non disponible, utilisation d'une méthode alternative")
                
            # Méthode alternative: créer une icône par défaut pour les SVG
            return self.create_default_svg_icon()
            
        except Exception as e:
            print(f"Erreur lors de la conversion SVG: {e}")
            return None
    
    def create_default_svg_icon(self):
        """Crée une icône par défaut pour les SVG non convertibles"""
        img = Image.new('RGBA', ICON_SIZE, (70, 130, 180, 255))  # Bleu acier
        
        from PIL import ImageDraw
        draw = ImageDraw.Draw(img)
        
        # Dessiner un symbole SVG simple
        center_x, center_y = ICON_SIZE[0] // 2, ICON_SIZE[1] // 2
        radius = min(ICON_SIZE) // 3
        
        # Cercle extérieur
        draw.ellipse([center_x - radius, center_y - radius, 
                     center_x + radius, center_y + radius], 
                     fill=(255, 255, 255, 255), outline=(0, 0, 0, 255), width=2)
        
        # Texte SVG
        try:
            from PIL import ImageFont
            font = ImageFont.truetype("arial.ttf", 12)
        except:
            font = ImageFont.load_default()
        
        draw.text((center_x, center_y), "SVG", fill=(0, 0, 0, 255), font=font, anchor="mm")
        
        return img
    
    def get_icon_for_app(self, app_name, shortcut_path=None):
        """Obtient l'icône pour une application (cache ou téléchargement)"""
        # Vérifier le cache d'abord
        cache_key = app_name.lower()
        if cache_key in self.cache:
            cached_path = self.cache[cache_key]
            if os.path.exists(cached_path):
                return cached_path
        
        print(f"🔍 Recherche d'icône pour: {app_name}")
        
        # 1. Essayer de rechercher en ligne d'abord (meilleure qualité)
        icon_url = self.search_icon_online(app_name)
        if icon_url:
            downloaded_path = self.download_and_process_icon(icon_url, app_name)
            if downloaded_path:
                print(f"  ✅ Icône en ligne téléchargée avec succès")
                return downloaded_path
        
        # 2. Si pas trouvé en ligne, essayer d'extraire et améliorer l'icône locale
        if shortcut_path:
            print(f"  🔄 Tentative d'extraction et amélioration de l'icône locale...")
            local_icon = self.extract_and_enhance_local_icon(shortcut_path, app_name)
            if local_icon:
                print(f"  ✅ Icône locale améliorée avec succès")
                return local_icon
        
        # 3. Si tout échoue, créer une icône par défaut
        print(f"  🎨 Création d'une icône par défaut...")
        return self.create_default_icon(app_name)
    
    def extract_and_enhance_local_icon(self, shortcut_path, app_name):
        """Extrait l'icône locale et l'améliore avec des techniques avancées"""
        try:
            import win32com.client
            import win32gui
            import win32ui
            
            file_path = shortcut_path
            
            # Pour les raccourcis, obtenir le fichier cible
            if file_path.lower().endswith('.lnk'):
                shell = win32com.client.Dispatch("WScript.Shell")
                shortcut = shell.CreateShortCut(file_path)
                target_path = shortcut.Targetpath
                if target_path and os.path.exists(target_path):
                    file_path = target_path
            
            # Extraire l'icône en plusieurs tailles
            large, small = win32gui.ExtractIconEx(file_path, 0)
            if large:
                # Utiliser la plus grande icône disponible
                win32gui.DestroyIcon(small[0])
                
                # Essayer d'extraire en 256x256 puis 128x128
                for size in [256, 128, 64, 32]:
                    try:
                        hdc = win32ui.CreateDCFromHandle(win32gui.GetDC(0))
                        hbmp = win32ui.CreateBitmap()
                        hbmp.CreateCompatibleBitmap(hdc, size, size)
                        hdc = hdc.CreateCompatibleDC()
                        hdc.SelectObject(hbmp)
                        hdc.DrawIcon((0, 0), large[0])
                        
                        # Convertir en PIL Image
                        bmpstr = hbmp.GetBitmapBits(True)
                        img = Image.frombuffer('RGB', (size, size), bmpstr, 'raw', 'BGRX', 0, 1)
                        
                        # Améliorer l'icône avec des techniques avancées
                        enhanced_img = self.enhance_icon_quality(img)
                        
                        # Sauvegarder l'icône améliorée
                        app_hash = self.get_app_icon_hash(app_name)
                        final_path = os.path.join(ICONS_DIR, f"{app_hash}_enhanced.png")
                        
                        enhanced_img.save(final_path, 'PNG', optimize=True)
                        
                        # Mettre à jour le cache
                        self.cache[app_name.lower()] = final_path
                        self.save_cache()
                        
                        win32gui.DestroyIcon(large[0])
                        return final_path
                        
                    except Exception as e:
                        print(f"  Erreur taille {size}x{size}: {e}")
                        continue
                
                win32gui.DestroyIcon(large[0])
                
        except Exception as e:
            print(f"Erreur lors de l'extraction locale: {e}")
        
        return None
    
    def enhance_icon_quality(self, img):
        """Améliore la qualité d'une icône avec des techniques avancées"""
        try:
            from PIL import ImageEnhance, ImageFilter
            
            # Convertir en RGBA si nécessaire
            if img.mode != 'RGBA':
                img = img.convert('RGBA')
            
            # Si l'image est plus petite que notre taille cible, l'agrandir intelligemment
            if img.size[0] < ICON_SIZE[0] or img.size[1] < ICON_SIZE[1]:
                # Utiliser Lanczos pour un agrandissement de haute qualité
                img = img.resize(ICON_SIZE, Image.Resampling.LANCZOS)
            else:
                # Redimensionner normalement
                img = img.resize(ICON_SIZE, Image.Resampling.LANCZOS)
            
            # Améliorer la netteté
            enhancer = ImageEnhance.Sharpness(img)
            img = enhancer.enhance(1.3)
            
            # Améliorer le contraste légèrement
            enhancer = ImageEnhance.Contrast(img)
            img = enhancer.enhance(1.1)
            
            # Améliorer la couleur
            enhancer = ImageEnhance.Color(img)
            img = enhancer.enhance(1.05)
            
            # Appliquer un filtre anti-aliasing léger
            img = img.filter(ImageFilter.SMOOTH_MORE)
            
            return img
            
        except Exception as e:
            print(f"Erreur lors de l'amélioration: {e}")
            # Retourner l'image originale redimensionnée
            return img.resize(ICON_SIZE, Image.Resampling.LANCZOS)
    
    def create_default_icon(self, app_name):
        """Crée une icône par défaut personnalisée"""
        try:
            app_hash = self.get_app_icon_hash(app_name)
            default_path = os.path.join(ICONS_DIR, f"{app_hash}_default.png")
            
            # Créer une icône avec les initiales de l'application
            img = Image.new('RGBA', ICON_SIZE, (100, 100, 100, 255))
            
            from PIL import ImageDraw, ImageFont
            draw = ImageDraw.Draw(img)
            
            # Obtenir les initiales
            words = app_name.split()
            initials = ''.join([word[0].upper() for word in words[:2] if word])
            if not initials:
                initials = app_name[0].upper() if app_name else '?'
            
            # Essayer d'utiliser une police système
            try:
                font = ImageFont.truetype("arial.ttf", 24)
            except:
                font = ImageFont.load_default()
            
            # Centrer le texte
            bbox = draw.textbbox((0, 0), initials, font=font)
            text_width = bbox[2] - bbox[0]
            text_height = bbox[3] - bbox[1]
            x = (ICON_SIZE[0] - text_width) // 2
            y = (ICON_SIZE[1] - text_height) // 2
            
            draw.text((x, y), initials, fill=(255, 255, 255, 255), font=font)
            
            img.save(default_path, 'PNG')
            
            # Mettre à jour le cache
            self.cache[app_name.lower()] = default_path
            self.save_cache()
            
            return default_path
            
        except Exception as e:
            print(f"Erreur lors de la création de l'icône par défaut: {e}")
            return None
    
    def get_icon_widget(self, parent, app_name, shortcut_path=None):
        """Crée un widget Tkinter avec l'icône de l'application"""
        icon_path = self.get_icon_for_app(app_name, shortcut_path)
        
        if icon_path and os.path.exists(icon_path):
            try:
                # Charger l'image pour Tkinter
                img = Image.open(icon_path)
                # Redimensionner pour l'affichage (plus petit que la taille stockée)
                img = img.resize(DISPLAY_SIZE, Image.Resampling.LANCZOS)
                photo = ImageTk.PhotoImage(img)
                
                # Créer le widget
                icon_widget = tk.Label(parent, image=photo, bg=parent.cget('bg'))
                icon_widget.image = photo  # Garder une référence
                
                return icon_widget
                
            except Exception as e:
                print(f"Erreur lors de la création du widget: {e}")
        
        # Fallback sur un label texte
        return tk.Label(parent, text="[App]", bg=parent.cget('bg'), fg="#333", font=("Arial", 10))

# Instance globale
icon_manager = IconManager()
