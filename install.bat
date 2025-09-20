@echo off
echo 🚀 Installation d'AppsLauncher Modern
echo.

echo 📦 Installation des dépendances Python...
pip install -r requirements.txt

if %ERRORLEVEL% EQU 0 (
    echo.
    echo ✅ Installation réussie !
    echo.
    echo 🎯 Pour lancer l'application :
    echo    python main.py
    echo.
    echo 🎨 Ou avec splash screen :
    echo    python launcher_with_splash.py
    echo.
    pause
) else (
    echo.
    echo ❌ Erreur lors de l'installation
    echo 💡 Vérifiez que Python et pip sont installés
    echo.
    pause
)
