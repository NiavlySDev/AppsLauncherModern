import uuid
import json
import os

# Fichier de sauvegarde
DATA_FILE = "launcher_data.json"

categories = {}
applications = {}

def save_data():
    """Sauvegarde les données dans un fichier JSON"""
    data = {
        "categories": categories,
        "applications": applications
    }
    try:
        with open(DATA_FILE, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        return True
    except Exception as e:
        print(f"Erreur lors de la sauvegarde: {e}")
        return False

def load_data():
    """Charge les données depuis le fichier JSON"""
    global categories, applications
    
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, 'r', encoding='utf-8') as f:
                data = json.load(f)
                categories = data.get("categories", {})
                applications = data.get("applications", {})
            print(f"Données chargées: {len(categories)} catégories, {len(applications)} applications")
            return True
        except Exception as e:
            print(f"Erreur lors du chargement: {e}")
            return False
    return False

def add_category(name, icon, color, parent=None):
    cat_id = str(uuid.uuid4())
    categories[cat_id] = {
        "name": name,
        "icon": icon,
        "color": color,
        "parent": parent,
    }
    save_data()  # Sauvegarder automatiquement
    return cat_id

def get_categories(parent=None):
    return {k: v for k, v in categories.items() if v["parent"] == parent}

def get_category(category_id):
    """Récupère une catégorie par son ID"""
    return categories.get(category_id)

def get_applications(category):
    return {k: v for k, v in applications.items() if v["category"] == category}

def get_applications_for_category(category_id):
    """Récupère toutes les applications d'une catégorie"""
    return {k: v for k, v in applications.items() if v["category"] == category_id}

def add_application(category_id, name, path=None, shortcut_path=None, icon=None):
    """Ajoute une application à une catégorie"""
    import uuid
    app_id = str(uuid.uuid4())
    applications[app_id] = {
        "name": name,
        "category": category_id,
        "path": path,
        "shortcut_path": shortcut_path,
        "icon": icon,
    }
    save_data()  # Sauvegarder automatiquement
    return app_id

def launch_application(category_id, app_id):
    """Lance une application par son ID"""
    if app_id in applications:
        app = applications[app_id]
        shortcut_path = app.get("shortcut_path")
        path = app.get("path")
        
        if shortcut_path:
            import os
            import subprocess
            try:
                # Utilise start pour lancer le raccourci sous Windows
                subprocess.run(['start', '', shortcut_path], shell=True, check=True)
                return True
            except subprocess.CalledProcessError:
                return False
        elif path:
            import os
            import subprocess
            try:
                # Lance l'exécutable directement
                subprocess.run([path], shell=True, check=True)
                return True
            except subprocess.CalledProcessError:
                return False
    return False