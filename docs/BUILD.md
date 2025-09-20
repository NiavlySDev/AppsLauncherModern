# 🏗️ Guide de Build - AppsLauncher Modern

Ce guide explique comment créer des installateurs pour Windows et Linux.

## 🎯 Méthodes de Build

### 🚀 Build Automatique (Recommandé)

```bash
# Build universel (détecte l'OS automatiquement)
python build_all.py

# Ou selon votre OS:
# Windows: build/windows/build_windows.bat
# Linux: build/linux/build_linux.sh
```

### 🔧 Build Manuel

#### Prérequis
```bash
# Dépendances Python
pip install pyinstaller

# Windows: NSIS (pour l'installateur)
# Télécharger: https://nsis.sourceforge.io/Download

# Linux: outils système
sudo apt-get install dpkg-dev
```

## 🖥️ Build Windows

### Étapes automatiques

1. **Création de l'exécutable**
   ```bash
   pyinstaller build/windows/app.spec --clean
   ```

2. **Création de l'installateur NSIS**
   ```bash
   makensis build/windows/installer.nsi
   ```

### Fichiers générés
- `build/windows/dist/AppsLauncherModern/` - Application portable
- `build/windows/AppsLauncherModern-Setup-v2.1.0.exe` - Installateur

### Fonctionnalités de l'installateur
- ✅ Installation dans Program Files
- ✅ Création raccourci bureau
- ✅ Ajout au menu démarrer
- ✅ Désinstallateur automatique
- ✅ Vérification version existante

## 🐧 Build Linux

### Étapes automatiques

1. **Création de l'exécutable**
   ```bash
   pyinstaller build/linux/app.spec --clean
   ```

2. **Création AppImage**
   - Application portable
   - Compatible toutes distributions
   - Aucune installation requise

3. **Création package .deb**
   - Installation système Ubuntu/Debian
   - Intégration menu applications
   - Gestion dépendances

### Fichiers générés
- `build/linux/AppsLauncherModern-v2.1.0-x86_64.AppImage` - Portable
- `build/linux/deb/appslauncher-modern_2.1.0_amd64.deb` - Package système

## 🤖 Build Automatique GitHub Actions

### Déclenchement
- Push d'un tag `v*` (ex: `v2.1.0`)
- Déclenchement manuel via GitHub UI

### Processus
1. **Build Windows** - Windows Server
2. **Build Linux** - Ubuntu Latest
3. **Création Release** - Upload automatique des binaires

### Commandes Git pour release
```bash
# Créer et pousser un tag
git tag -a v2.1.0 -m "Release v2.1.0"
git push origin v2.1.0

# GitHub Actions se déclenchera automatiquement
```

## 📦 Structure des Builds

```
build/
├── windows/
│   ├── app.spec              # Configuration PyInstaller
│   ├── installer.nsi         # Script NSIS
│   ├── version_info.txt      # Infos version Windows
│   ├── build_windows.bat     # Script de build
│   └── dist/                 # Exécutable généré
├── linux/
│   ├── app.spec              # Configuration PyInstaller
│   ├── appslauncher-modern.desktop  # Fichier .desktop
│   ├── build_linux.sh        # Script de build
│   ├── appimage/             # Structure AppImage
│   └── deb/                  # Package Debian
└── assets/
    ├── app_icon.ico          # Icône Windows
    ├── app_icon.png          # Icône Linux
    └── icon_*.png            # Icônes multi-résolution
```

## 🔍 Dépannage

### Windows

**Erreur: "NSIS non trouvé"**
```bash
# Installer NSIS et ajouter au PATH
# Ou compiler manuellement avec NSIS GUI
```

**Erreur: "PyInstaller failed"**
```bash
# Vérifier les dépendances
pip install -r requirements.txt
pip install pyinstaller
```

### Linux

**Erreur: "AppImage non créée"**
```bash
# Vérifier appimagetool
wget https://github.com/AppImage/AppImageKit/releases/download/continuous/appimagetool-x86_64.AppImage
chmod +x appimagetool-x86_64.AppImage
```

**Erreur: "Package .deb failed"**
```bash
# Installer dpkg-dev
sudo apt-get install dpkg-dev
```

## 📊 Tailles Approximatives

- **Windows EXE**: ~150MB (compressé avec UPX)
- **Windows Installateur**: ~80MB (compression NSIS)
- **Linux AppImage**: ~160MB
- **Linux .deb**: ~150MB

## 🎯 Distribution

### GitHub Releases
- Téléchargement direct des binaires
- Notes de version automatiques
- Statistiques de téléchargement

### Alternatives
- **Windows**: Microsoft Store, Chocolatey
- **Linux**: Snap Store, Flatpak, AUR (Arch)

---

**💡 Conseil**: Utilisez `python build_all.py` pour un build simple et automatique !
