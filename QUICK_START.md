# Guide de Démarrage Rapide - AppsLauncher Modern

## 🚀 Installation Rapide

### Option 1: Installation Automatique (Recommandée)
```bash
# Télécharger le projet et exécuter:
install.bat
```

### Option 2: Installation Manuelle
```bash
# Installer les dépendances Python
pip install -r requirements.txt
```

## 🎯 Lancement de l'Application

### Méthodes de Lancement

1. **Script Windows Simple** (Recommandé)
   ```bash
   start.bat
   ```

2. **Point d'entrée principal**
   ```bash
   python main.py
   ```

3. **Interface moderne directe**
   ```bash
   python launcher.py
   ```

4. **Avec splash screen**
   ```bash
   python launcher_with_splash.py
   ```

## 🔧 Dépannage

### Problème: "No module named 'customtkinter'"
**Solution:** Installer les dépendances
```bash
pip install customtkinter pillow requests beautifulsoup4
```

### Problème: Application ne se lance pas
**Solution:** Vérifier Python 3.7+
```bash
python --version
```

### Problème: Icônes ne se chargent pas
**Solution:** Vérifier connexion internet pour téléchargement automatique

## 📂 Structure Simple

```
AppsLauncherModern/
├── main.py              # 🚀 Lancez-moi !
├── start.bat            # 🖥️ Ou moi sur Windows !
├── install.bat          # 📦 Installation automatique
└── requirements.txt     # 📋 Dépendances Python
```

## 🎮 Utilisation

1. **Lancer l'application** avec `start.bat` ou `python main.py`
2. **Parcourir les catégories** d'applications
3. **Cliquer sur une catégorie** pour voir les applications
4. **Cliquer sur une application** pour la lancer
5. **Ajouter des applications** avec le bouton "+"

## 💡 Fonctionnalités

- ✅ Interface moderne CustomTkinter
- ✅ Détection automatique Steam
- ✅ Icônes haute qualité automatiques
- ✅ Support raccourcis Windows
- ✅ Thème sombre/clair
- ✅ Grille responsive

**Besoin d'aide ?** Consultez le README.md complet ou créez une issue sur GitHub.
