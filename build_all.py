#!/usr/bin/env python3
"""
Script de build universel pour AppsLauncher Modern
Détecte automatiquement l'OS et lance le build approprié
"""

import os
import sys
import platform
import subprocess

def main():
    print("🚀 AppsLauncher Modern - Build Universel")
    print("=" * 50)
    
    # Détecter l'OS
    system = platform.system().lower()
    print(f"🖥️  Système détecté: {platform.system()} {platform.machine()}")
    print()
    
    if system == "windows":
        print("🔨 Lancement du build Windows...")
        script_path = os.path.join("build", "windows", "build_windows.bat")
        
        if os.path.exists(script_path):
            try:
                subprocess.run([script_path], shell=True, check=True)
                print("✅ Build Windows terminé avec succès !")
            except subprocess.CalledProcessError as e:
                print(f"❌ Erreur lors du build Windows: {e}")
                return 1
        else:
            print(f"❌ Script de build Windows non trouvé: {script_path}")
            return 1
            
    elif system == "linux":
        print("🔨 Lancement du build Linux...")
        script_path = os.path.join("build", "linux", "build_linux.sh")
        
        if os.path.exists(script_path):
            try:
                # Rendre le script exécutable
                os.chmod(script_path, 0o755)
                subprocess.run(["/bin/bash", script_path], check=True)
                print("✅ Build Linux terminé avec succès !")
            except subprocess.CalledProcessError as e:
                print(f"❌ Erreur lors du build Linux: {e}")
                return 1
        else:
            print(f"❌ Script de build Linux non trouvé: {script_path}")
            return 1
            
    elif system == "darwin":
        print("🍎 macOS détecté")
        print("⚠️  Le build macOS n'est pas encore supporté")
        print("💡 Vous pouvez utiliser l'installation Python standard:")
        print("   pip install -r requirements.txt")
        print("   python main.py")
        return 1
        
    else:
        print(f"❌ Système non supporté: {system}")
        print("💡 Systèmes supportés: Windows, Linux")
        return 1
    
    print()
    print("🎉 Build terminé ! Vérifiez le dossier build/ pour les fichiers générés.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
