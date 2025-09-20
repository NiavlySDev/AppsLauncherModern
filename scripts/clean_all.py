#!/usr/bin/env python3
"""Script pour nettoyer aussi le cache d'icônes."""

import os
import shutil

def clean_all():
    """Nettoie toutes les données et icônes"""
    
    # Nettoyer le fichier de données
    data_file = "launcher_data.json"
    if os.path.exists(data_file):
        try:
            os.remove(data_file)
            print(f"✅ Fichier de données '{data_file}' supprimé")
        except Exception as e:
            print(f"❌ Erreur lors de la suppression des données: {e}")
    else:
        print(f"ℹ️  Fichier de données '{data_file}' n'existe pas")
    
    # Nettoyer le cache d'icônes
    cache_file = "icon_cache.json"
    if os.path.exists(cache_file):
        try:
            os.remove(cache_file)
            print(f"✅ Cache d'icônes '{cache_file}' supprimé")
        except Exception as e:
            print(f"❌ Erreur lors de la suppression du cache: {e}")
    else:
        print(f"ℹ️  Cache d'icônes '{cache_file}' n'existe pas")
    
    # Nettoyer le dossier d'icônes
    icons_dir = "icons"
    if os.path.exists(icons_dir):
        try:
            shutil.rmtree(icons_dir)
            print(f"✅ Dossier d'icônes '{icons_dir}' supprimé")
        except Exception as e:
            print(f"❌ Erreur lors de la suppression du dossier d'icônes: {e}")
    else:
        print(f"ℹ️  Dossier d'icônes '{icons_dir}' n'existe pas")
    
    print("🧹 Nettoyage complet terminé!")

if __name__ == "__main__":
    clean_all()
