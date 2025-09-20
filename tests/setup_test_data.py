#!/usr/bin/env python3
"""Script pour ajouter des données de test à l'application."""

from data import add_category, add_application
import os
import re

def find_steam_shortcuts(directory):
    """Recherche récursivement les raccourcis Steam dans un répertoire"""
    steam_shortcuts = []
    
    try:
        for root, dirs, files in os.walk(directory):
            for file in files:
                if file.endswith('.lnk') or file.endswith('.url'):
                    file_path = os.path.join(root, file)
                    # Vérifier si c'est un raccourci Steam
                    if is_steam_shortcut(file_path, file):
                        steam_shortcuts.append(file_path)
    except PermissionError:
        print(f"Permission refusée pour accéder à: {directory}")
    except Exception as e:
        print(f"Erreur lors de la recherche dans {directory}: {e}")
    
    return steam_shortcuts

def is_steam_shortcut(file_path, filename):
    """Vérifie si un raccourci est lié à Steam"""
    # Patterns pour identifier les raccourcis Steam
    steam_patterns = [
        r'steam://',
        r'steam\.exe',
        r'steamapps',
        r'steam_appid',
    ]
    
    # Vérifier le nom du fichier
    filename_lower = filename.lower()
    if 'steam' in filename_lower:
        return True
    
    try:
        # Pour les fichiers .url, lire le contenu
        if file_path.endswith('.url'):
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
                for pattern in steam_patterns:
                    if re.search(pattern, content, re.IGNORECASE):
                        return True
        
        # Pour les raccourcis .lnk, vérifier via win32com
        elif file_path.endswith('.lnk'):
            try:
                import win32com.client
                shell = win32com.client.Dispatch("WScript.Shell")
                shortcut = shell.CreateShortCut(file_path)
                target = shortcut.Targetpath.lower()
                arguments = shortcut.Arguments.lower()
                
                if 'steam' in target or 'steam://' in arguments:
                    return True
            except:
                pass
                
    except Exception:
        pass
    
    return False

def scan_common_steam_locations():
    """Scanne les emplacements communs pour les applications Steam"""
    steam_locations = [
        # Bureau et sous-dossiers
        os.path.join(os.path.expanduser("~"), "Desktop"),
        
        # Menu démarrer
        os.path.join(os.path.expanduser("~"), "AppData", "Roaming", "Microsoft", "Windows", "Start Menu", "Programs"),
        r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs",
        
        # Dossier Steam par défaut
        r"C:\Program Files (x86)\Steam",
        r"C:\Program Files\Steam",
        
        # Autres emplacements possibles
        os.path.join(os.path.expanduser("~"), "AppData", "Roaming", "Microsoft", "Windows", "Start Menu", "Programs", "Steam"),
    ]
    
    all_steam_shortcuts = []
    
    for location in steam_locations:
        if os.path.exists(location):
            print(f"Recherche Steam dans: {location}")
            steam_shortcuts = find_steam_shortcuts(location)
            all_steam_shortcuts.extend(steam_shortcuts)
            print(f"  Trouvé {len(steam_shortcuts)} raccourcis Steam")
    
    return all_steam_shortcuts

def setup_test_data():
    """Ajoute des catégories et applications de test"""
    
    # Ajouter une catégorie Bureau
    bureau_id = add_category("Bureau", "🖥️", "#4CAF50")
    print(f"Catégorie Bureau créée: {bureau_id}")
    
    # Ajouter une catégorie Outils
    outils_id = add_category("Outils", "🔧", "#FF9800")
    print(f"Catégorie Outils créée: {outils_id}")
    
    # Ajouter une catégorie Jeux Steam
    steam_id = add_category("Jeux Steam", "🎮", "#1B2838")
    print(f"Catégorie Jeux Steam créée: {steam_id}")
    
    # Rechercher les applications normales sur le bureau
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    print(f"\nRecherche de raccourcis normaux dans: {desktop_path}")
    
    if os.path.exists(desktop_path):
        for file in os.listdir(desktop_path):
            if file.endswith('.lnk'):
                file_path = os.path.join(desktop_path, file)
                # Ne pas ajouter les raccourcis Steam ici
                if not is_steam_shortcut(file_path, file):
                    app_name = os.path.splitext(file)[0]
                    app_id = add_application(app_name, "📱", bureau_id, file_path)
                    print(f"Application ajoutée: {app_name}")
    
    # Rechercher et ajouter les applications Steam
    print(f"\n🎮 Recherche des applications Steam...")
    steam_shortcuts = scan_common_steam_locations()
    
    # Éliminer les doublons basés sur le nom de l'application
    unique_steam_apps = {}
    for shortcut_path in steam_shortcuts:
        app_name = os.path.splitext(os.path.basename(shortcut_path))[0]
        # Nettoyer le nom (enlever les préfixes/suffixes courants)
        clean_name = app_name.replace("Steam - ", "").replace(" - Steam", "").strip()
        
        # Éviter les doublons en utilisant le nom nettoyé comme clé
        if clean_name not in unique_steam_apps and clean_name.lower() not in ['steam', 'steam support center']:
            unique_steam_apps[clean_name] = shortcut_path
    
    print(f"\n📂 Ajout des applications Steam trouvées (dédoublonnées):")
    for app_name, shortcut_path in unique_steam_apps.items():
        try:
            app_id = add_application(app_name, "🎮", steam_id, shortcut_path)
            print(f"  Jeu Steam ajouté: {app_name}")
        except Exception as e:
            print(f"  Erreur lors de l'ajout de {app_name}: {e}")
    
    print(f"\n✅ Données de test ajoutées!")
    print(f"   📁 Applications normales: dans la catégorie Bureau")
    print(f"   🎮 Jeux Steam: {len(unique_steam_apps)} uniques trouvés (sur {len(steam_shortcuts)} raccourcis scannés)")

if __name__ == "__main__":
    setup_test_data()
