#!/usr/bin/env python3
"""API simplifiée pour rechercher des icônes de haute qualité."""

import requests
import json
import os
from urllib.parse import quote
import time

class IconAPIManager:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
    
    def search_icon_iconify(self, app_name):
        """Recherche une icône via l'API Iconify (gratuite)"""
        try:
            # Nettoyer le nom pour la recherche
            clean_name = app_name.lower().replace(' ', '-')
            
            # Essayer plusieurs recherches
            search_terms = [
                clean_name,
                app_name.split()[0].lower() if ' ' in app_name else app_name.lower(),
                f"{clean_name}-icon",
                f"logos-{clean_name}",
            ]
            
            for term in search_terms:
                # API Iconify pour rechercher des icônes
                api_url = f"https://api.iconify.design/search?query={quote(term)}&limit=10"
                
                try:
                    response = self.session.get(api_url, timeout=10)
                    if response.status_code == 200:
                        data = response.json()
                        icons = data.get('icons', [])
                        
                        if icons:
                            # Prendre la première icône trouvée
                            icon_name = icons[0]
                            
                            # Obtenir l'URL de l'icône en PNG plutôt qu'en SVG
                            icon_url = f"https://api.iconify.design/{icon_name}.png?width=64&height=64"
                            return icon_url
                            
                except Exception as e:
                    print(f"Erreur Iconify pour {term}: {e}")
                    continue
                
                time.sleep(0.1)  # Éviter de surcharger l'API
            
        except Exception as e:
            print(f"Erreur générale Iconify: {e}")
        
        return None
    
    def search_icons8(self, app_name):
        """Recherche sur Icons8 (API gratuite limitée)"""
        try:
            # Icons8 a une API pour les icônes gratuites
            clean_name = app_name.lower().replace(' ', '%20')
            
            # URL de l'API Icons8 pour des icônes gratuites
            api_url = f"https://img.icons8.com/color/64/{clean_name}.png"
            
            # Tester si l'icône existe
            response = self.session.head(api_url, timeout=10)
            if response.status_code == 200:
                return api_url
            
            # Essayer avec des variantes
            variants = [
                f"https://img.icons8.com/fluency/64/{clean_name}.png",
                f"https://img.icons8.com/color/48/{clean_name}.png",
                f"https://img.icons8.com/ios-filled/64/{clean_name}.png",
            ]
            
            for variant_url in variants:
                try:
                    response = self.session.head(variant_url, timeout=5)
                    if response.status_code == 200:
                        return variant_url
                except:
                    continue
                    
        except Exception as e:
            print(f"Erreur Icons8: {e}")
        
        return None
    
    def search_steamdb(self, app_name):
        """Recherche des icônes de jeux sur SteamDB"""
        try:
            # Recherche d'abord dans l'API Steam publique
            steam_api_url = f"https://store.steampowered.com/api/storesearch/?term={quote(app_name)}&l=english&cc=US"
            
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            }
            
            response = self.session.get(steam_api_url, headers=headers, timeout=10)
            if response.status_code == 200:
                data = response.json()
                items = data.get('items', [])
                
                if items:
                    # Prendre le premier résultat (le plus pertinent)
                    steam_app = items[0]
                    steam_app_id = steam_app.get('id')
                    
                    if steam_app_id:
                        # URLs des images Steam de haute qualité
                        steam_icon_urls = [
                            f"https://cdn.akamai.steamstatic.com/steam/apps/{steam_app_id}/header.jpg",
                            f"https://cdn.akamai.steamstatic.com/steam/apps/{steam_app_id}/library_600x900.jpg", 
                            f"https://cdn.akamai.steamstatic.com/steam/apps/{steam_app_id}/library_hero.jpg",
                            f"https://cdn.akamai.steamstatic.com/steam/apps/{steam_app_id}/capsule_616x353.jpg",
                            f"https://cdn.akamai.steamstatic.com/steam/apps/{steam_app_id}/capsule_231x87.jpg",
                        ]
                        
                        # Tester chaque URL
                        for icon_url in steam_icon_urls:
                            try:
                                test_response = self.session.head(icon_url, timeout=5)
                                if test_response.status_code == 200:
                                    print(f"    🎮 Steam App ID trouvé: {steam_app_id}")
                                    return icon_url
                            except:
                                continue
                                
        except Exception as e:
            print(f"Erreur SteamDB: {e}")
        
        return None
    
    def search_enhanced_icons8(self, app_name):
        """Recherche améliorée sur Icons8 avec différentes tailles"""
        try:
            clean_name = app_name.lower().replace(' ', '%20')
            
            # Essayer différentes tailles (plus grandes d'abord)
            sizes = [256, 128, 96, 64, 48]
            styles = ['color', 'fluency', 'ios-filled', 'material-rounded', 'carbon']
            
            for size in sizes:
                for style in styles:
                    icon_url = f"https://img.icons8.com/{style}/{size}/{clean_name}.png"
                    
                    try:
                        response = self.session.head(icon_url, timeout=5)
                        if response.status_code == 200:
                            return icon_url
                    except:
                        continue
                        
        except Exception as e:
            print(f"Erreur Icons8 Enhanced: {e}")
        
        return None
    
    def search_favicon(self, app_name):
        """Recherche le favicon officiel de l'application"""
        try:
            # Essayer de deviner l'URL officielle
            possible_domains = [
                f"{app_name.lower().replace(' ', '')}.com",
                f"{app_name.lower().replace(' ', '')}.org",
                f"{app_name.lower().replace(' ', '')}.io",
            ]
            
            for domain in possible_domains:
                favicon_urls = [
                    f"https://{domain}/favicon.ico",
                    f"https://{domain}/favicon.png",
                    f"https://{domain}/assets/favicon.ico",
                    f"https://{domain}/static/favicon.ico",
                ]
                
                for favicon_url in favicon_urls:
                    try:
                        response = self.session.head(favicon_url, timeout=5)
                        if response.status_code == 200:
                            # Vérifier la taille du contenu
                            content_length = response.headers.get('content-length')
                            if content_length and int(content_length) > 1000:  # Au moins 1KB
                                return favicon_url
                    except:
                        continue
                        
        except Exception as e:
            print(f"Erreur favicon: {e}")
        
        return None
    
    def search_github_logo(self, app_name):
        """Recherche le logo sur GitHub (pour les projets open source)"""
        try:
            # Rechercher le projet sur GitHub
            github_api = f"https://api.github.com/search/repositories?q={quote(app_name)}&sort=stars&order=desc"
            
            response = self.session.get(github_api, timeout=10)
            if response.status_code == 200:
                data = response.json()
                repos = data.get('items', [])
                
                if repos:
                    # Prendre le premier repo (le plus populaire)
                    repo = repos[0]
                    owner = repo['owner']['login']
                    repo_name = repo['name']
                    
                    # Essayer de trouver un logo dans le repo
                    logo_urls = [
                        f"https://raw.githubusercontent.com/{owner}/{repo_name}/main/logo.png",
                        f"https://raw.githubusercontent.com/{owner}/{repo_name}/master/logo.png",
                        f"https://raw.githubusercontent.com/{owner}/{repo_name}/main/assets/logo.png",
                        f"https://raw.githubusercontent.com/{owner}/{repo_name}/master/assets/logo.png",
                        f"https://raw.githubusercontent.com/{owner}/{repo_name}/main/icon.png",
                        f"https://raw.githubusercontent.com/{owner}/{repo_name}/master/icon.png",
                    ]
                    
                    for logo_url in logo_urls:
                        try:
                            response = self.session.head(logo_url, timeout=5)
                            if response.status_code == 200:
                                return logo_url
                        except:
                            continue
                            
        except Exception as e:
            print(f"Erreur GitHub: {e}")
        
        return None
    
    def search_simple_icons(self, app_name):
        """Recherche dans Simple Icons (logos de marques)"""
        try:
            # Simple Icons CDN pour les logos de marques
            clean_name = app_name.lower().replace(' ', '').replace('-', '')
            
            # URLs possibles
            urls = [
                f"https://cdn.jsdelivr.net/npm/simple-icons@v9/icons/{clean_name}.svg",
                f"https://raw.githubusercontent.com/simple-icons/simple-icons/develop/icons/{clean_name}.svg",
            ]
            
            for url in urls:
                try:
                    response = self.session.head(url, timeout=5)
                    if response.status_code == 200:
                        return url
                except:
                    continue
                    
        except Exception as e:
            print(f"Erreur Simple Icons: {e}")
        
        return None
    
    def find_best_icon(self, app_name):
        """Trouve la meilleure icône disponible pour une application"""
        print(f"🔍 Recherche d'icône pour: {app_name}")
        
        # Essayer différentes sources dans l'ordre de préférence
        sources = [
            ("SteamDB", self.search_steamdb),
            ("Enhanced Icons8", self.search_enhanced_icons8),
            ("Icons8", self.search_icons8),
            ("Simple Icons", self.search_simple_icons),
            ("Favicon", self.search_favicon),
            ("GitHub", self.search_github_logo),
        ]
        
        for source_name, search_func in sources:
            try:
                print(f"  🔎 Essai {source_name}...")
                icon_url = search_func(app_name)
                if icon_url:
                    print(f"  ✅ Trouvé sur {source_name}: {icon_url}")
                    return icon_url
                else:
                    print(f"  ❌ Rien trouvé sur {source_name}")
            except Exception as e:
                print(f"  ❌ Erreur sur {source_name}: {e}")
        
        print(f"  🤷 Aucune icône trouvée pour {app_name}")
        return None

# Instance globale
icon_api = IconAPIManager()
