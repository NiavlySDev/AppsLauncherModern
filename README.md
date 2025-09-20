# AppsLauncher Modern 🚀

Un lanceur d'applications moderne avec interface CustomTkinter, gestionnaire d'icônes intelligent et support Steam.

![Interface Moderne](https://img.shields.io/badge/Interface-Moderne-blue)
![Python](https://img.shields.io/badge/Python-3.13-green)
![CustomTkinter](https://img.shields.io/badge/CustomTkinter-Moderne-orange)
![Icônes](https://img.shields.io/badge/Ic%C3%B4nes-HD-purple)

## ✨ Fonctionnalités

### 🎨 Interface Moderne
- **CustomTkinter** : Design moderne et fluide
- **Thème sombre/clair** : Basculement facile entre modes
- **Cartes interactives** : Effets hover et animations
- **Design responsive** : S'adapte à toutes tailles d'écran
- **Splash screen** : Écran de chargement professionnel

### 🎮 Intégration Steam
- **Détection automatique** : Scanne tous les jeux Steam installés
- **Icônes officielles** : Via API SteamDB et Steam Store
- **Support sous-dossiers** : Recherche récursive dans steamapps/common

### � Système d'Icônes Intelligent
- **6 sources d'icônes** : SteamDB, Icons8, Simple Icons, Favicons, GitHub
- **Cache haute résolution** : Stockage 128x128, affichage optimisé
- **Amélioration qualité** : Algorithmes de netteté et anti-aliasing
- **Fallback intelligent** : Génération d'icônes personnalisées

### 🔗 Support Raccourcis Windows
- **Raccourcis .lnk** : Ajout direct depuis le bureau
- **Extraction d'icônes** : Depuis exécutables et raccourcis
- **Amélioration locale** : Algorithmes d'amélioration qualité

## 🚀 Installation & Lancement

### 📦 Installation Automatique (Recommandée)

#### 🖥️ Windows
1. **Téléchargez l'installateur** depuis les [Releases GitHub](https://github.com/NiavlySDev/AppsLauncherModern/releases)
2. **Exécutez** `AppsLauncherModern-Setup-v*.exe`
3. **Suivez l'assistant** d'installation
4. **Lancez** depuis le raccourci bureau ou le menu démarrer

#### 🐧 Linux

**Option 1: AppImage (Portable)**
```bash
# Télécharger depuis GitHub Releases
wget https://github.com/NiavlySDev/AppsLauncherModern/releases/latest/download/AppsLauncherModern-v*-x86_64.AppImage

# Rendre exécutable et lancer
chmod +x AppsLauncherModern-v*-x86_64.AppImage
./AppsLauncherModern-v*-x86_64.AppImage
```

**Option 2: Package Debian/Ubuntu**
```bash
# Télécharger le package .deb
wget https://github.com/NiavlySDev/AppsLauncherModern/releases/latest/download/appslauncher-modern_*_amd64.deb

# Installer
sudo dpkg -i appslauncher-modern_*_amd64.deb

# Lancer depuis le menu applications ou:
appslauncher-modern
```

### 🛠️ Installation Développeur (Source)

#### Installation Automatique Windows
```bash
# Cloner et installer
git clone https://github.com/NiavlySDev/AppsLauncherModern.git
cd AppsLauncherModern
install.bat
start.bat
```

#### Installation Manuelle
```bash
# Cloner le repository
git clone https://github.com/NiavlySDev/AppsLauncherModern.git
cd AppsLauncherModern

# Installer les dépendances Python
pip install -r requirements.txt

# Lancer l'application
python main.py
```

## 📁 Structure du Projet

```
AppsLauncherModern/
├── 📁 src/                    # 🧠 Code source principal
│   ├── 📁 core/              # ⚙️ Composants principaux
│   │   ├── data.py           # Gestion données et persistance
│   │   ├── icon_manager.py   # Gestionnaire d'icônes intelligent
│   │   └── config.py         # Configuration application
│   ├── 📁 ui/                # 🎨 Interface utilisateur
│   │   └── 📁 modern_ui/     # CustomTkinter moderne
│   │       ├── main_view.py      # Vue principale avec grille
│   │       ├── category_view.py  # Vue catégories
│   │       ├── components.py     # Composants réutilisables
│   │       ├── dialogs.py        # Dialogues modernes
│   │       ├── theme.py          # Thèmes et couleurs
│   │       └── effects.py        # Animations et effets
│   └── 📁 utils/             # 🔧 Utilitaires
│       └── icon_api.py       # APIs d'icônes en ligne
├── 📁 tests/                 # 🧪 Tests et validation
├── 📁 scripts/               # 📜 Scripts utilitaires
├── 📁 docs/                  # 📚 Documentation
│   └── 📁 template/          # Captures d'écran référence
├── 📁 icons/                 # � Cache icônes téléchargées
├── main.py                   # 🚀 Point d'entrée principal
├── launcher.py               # � Lanceur interface moderne
├── launcher_with_splash.py   # ✨ Lanceur avec splash screen
├── start.bat                 # 🖥️ Script Windows lancement
├── install.bat               # 📦 Script Windows installation
└── requirements.txt          # 📋 Dépendances Python
```

## 🎯 Nouveautés v2.0

### 🎨 Interface Révolutionnée
- **Migration CustomTkinter** : Abandon de Tkinter pour un design moderne
- **Cartes élégantes** : Coins arrondis, ombres, effets hover
- **Thème cohérent** : Couleurs harmonieuses, typographie Segoe UI
- **Responsive design** : Grille adaptative 4 colonnes

### 🔧 Architecture Moderne
- **Composants modulaires** : ModernCard, ModernButton, ModernHeader
- **Gestionnaire de thèmes** : Basculement sombre/clair
- **Grille intelligente** : Organisation automatique avec scroll
- **Barre de statut** : Informations temps réel

### 🎮 Améliorations Steam
- **API SteamDB intégrée** : Recherche icônes officielles par App ID
- **Détection étendue** : Scan récursif tous dossiers Steam
- **Qualité optimale** : Icônes haute résolution garanties

### 🌟 Expérience Utilisateur
- **Splash screen** : Chargement professionnel avec progression
- **Animations fluides** : Transitions et effets visuels
- **Messages contextuels** : Feedback utilisateur permanent
- **Fallback intelligent** : Initiales colorées si pas d'icône

## 📊 Comparaison des Versions

| Fonctionnalité | v1.x (Classique) | v2.0 (Moderne) |
|---|---|---|
| **Interface** | Tkinter standard | CustomTkinter moderne |
| **Design** | Basique | Élégant avec animations |
| **Thèmes** | Fixe | Sombre/Clair + basculement |
| **Icônes** | Locales uniquement | 6 sources online + cache |
| **Steam** | Détection simple | API SteamDB + scan complet |
| **UX** | Fonctionnel | Professionnel avec feedback |

## 🛠️ Développement

### Technologies
- **Python 3.13** : Langage principal
- **CustomTkinter** : Framework UI moderne
- **Pillow (PIL)** : Traitement d'images
- **Requests** : API calls et téléchargements
- **BeautifulSoup4** : Web scraping pour icônes
- **PyWin32** : Intégration Windows (raccourcis)

### APIs Intégrées
- **Steam Store API** : Données officielles jeux Steam
- **SteamDB** : Métadonnées et icônes jeux
- **Icons8** : Icônes professionnelles haute qualité
- **Simple Icons** : Logos marques et services
- **GitHub API** : Icônes projets open source

## 📄 Licence

MIT License - Voir [LICENSE](LICENSE) pour détails

## 🤝 Contribution

Les contributions sont bienvenues ! N'hésitez pas à :
- 🐛 Signaler des bugs
- 💡 Proposer des fonctionnalités
- 🔧 Améliorer le code
- 📚 Améliorer la documentation

## 📞 Support

- **Issues** : [GitHub Issues](https://github.com/NiavlySDev/AppsLauncherModern/issues)
- **Discussions** : [GitHub Discussions](https://github.com/NiavlySDev/AppsLauncherModern/discussions)

---

**Transformez votre expérience de lancement d'applications avec AppsLauncher Modern !** 🚀✨

### 🔗 Support des Raccourcis
- **Ajout de raccourcis** : Vous pouvez maintenant ajouter des raccourcis (.lnk) ou des exécutables (.exe) à vos catégories
- **Lancement direct** : Cliquez sur une application pour la lancer directement

### 🎨 Système d'Icônes Haute Qualité ⭐ NOUVEAU
- **Recherche automatique intelligente** : Système en cascade pour trouver les meilleures icônes
- **Sources multiples prioritaires** :
  1. **SteamDB/Steam API** : Icônes officielles Steam de haute qualité pour les jeux
  2. **Icons8 Enhanced** : Icônes professionnelles en 256x256, 128x128, 96x96 pixels
  3. **Icons8 Standard** : Icônes colorées de qualité
  4. **Simple Icons** : Logos de marques officiels
  5. **Favicons** : Icônes officielles des sites web des applications
  6. **GitHub** : Logos pour les projets open source
- **Amélioration d'icônes locales** : Si aucune icône n'est trouvée en ligne, extrait et améliore les icônes des raccourcis locaux avec :
  - Extraction multi-tailles (256x256 → 32x32)
  - Algorithmes d'agrandissement haute qualité (Lanczos)
  - Amélioration de netteté, contraste et couleurs
  - Filtres anti-aliasing
- **Cache intelligent** : Icônes sauvegardées en 128x128 pixels, affichées en 32x32
- **Qualité garantie** : Fini les icônes pixélisées comme American Truck Simulator !
- **Fallback créatif** : Génération d'icônes personnalisées avec initiales si tout échoue

### � Support Steam Intégré
- **Détection automatique des jeux Steam** : Le script `setup_test_data.py` détecte et ajoute automatiquement tous vos jeux Steam
- **Recherche dans les sous-dossiers** : Scan récursif du bureau et autres emplacements pour trouver les raccourcis Steam
- **Catégorie dédiée** : Création automatique d'une catégorie "Jeux Steam" avec l'icône 🎮
- **Déduplication intelligente** : Évite les doublons même si les raccourcis existent à plusieurs endroits
- **Support des fichiers .url** : Compatible avec les raccourcis Steam au format .url

### �🎨 Interface Améliorée
- **Aperçu d'icône** : Voir l'icône extraite dans le dialogue d'ajout d'application
- **Sélection de fichiers** : Interface intuitive pour sélectionner des raccourcis depuis le bureau ou d'autres emplacements
- **Auto-remplissage** : Le nom de l'application est automatiquement rempli basé sur le fichier sélectionné

### 💾 Persistance des Données
- **Sauvegarde automatique** : Toutes les données sont automatiquement sauvegardées dans `launcher_data.json`
- **Chargement au démarrage** : Les données sont automatiquement rechargées à chaque démarrage

## Comment Utiliser

### Ajouter une Application Manuellement
1. Naviguer vers une catégorie
2. Cliquer sur "Nouvelle Appli"
3. Donner un nom à l'application
4. Cliquer sur "Choisir un raccourci" et sélectionner :
   - Un raccourci (.lnk) depuis le bureau
   - Un fichier exécutable (.exe)
   - Un raccourci Steam (.url)
   - Ou tout autre type de fichier
5. L'icône sera automatiquement extraite et affichée
6. Optionnellement, ajouter une icône texte
7. Cliquer sur "Créer"

### Ajouter Automatiquement vos Jeux Steam
1. Exécuter le script : `python setup_test_data.py`
2. Le script va :
   - Scanner votre bureau et ses sous-dossiers
   - Chercher dans les menus démarrer Windows
   - Détecter automatiquement tous les raccourcis Steam
   - Créer une catégorie "Jeux Steam" dédiée
   - Ajouter tous vos jeux sans doublons

### Lancer une Application
- Simplement cliquer sur la carte de l'application dans la vue de catégorie
- L'application/raccourci sera lancé directement (y compris les jeux Steam)

## Dépendances

L'application utilise les packages Python suivants :
- `tkinter` : Interface graphique (inclus avec Python)
- `pywin32` : Manipulation des raccourcis et extraction d'icônes Windows
- `Pillow (PIL)` : Traitement d'images pour les icônes

## Structure des Fichiers

```
├── main.py                     # Point d'entrée principal
├── data.py                     # Gestion des données et persistance
├── theme.py                    # Thème et couleurs
├── launcher_data.json          # Données sauvegardées (généré automatiquement)
├── setup_test_data.py         # Script pour ajouter des données de test
└── ui/
    ├── main_view.py           # Vue principale
    ├── category_view.py       # Vue des catégories (avec support des icônes)
    ├── add_application_dialog.py # Dialogue d'ajout d'application (amélioré)
    └── add_category_dialog.py # Dialogue d'ajout de catégorie
```

## Notes Techniques

- Les icônes sont extraites à la volée lors de l'affichage
- Support des raccourcis Windows (.lnk) avec résolution du fichier cible
- Gestion des erreurs pour les icônes non extractibles
- Fallback sur l'icône texte si l'extraction échoue
