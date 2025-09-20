@echo off
title AppsLauncher Modern

echo 🚀 Lancement d'AppsLauncher Modern...
echo.

cd /d "%~dp0"

python main.py

if %ERRORLEVEL% NEQ 0 (
    echo.
    echo ❌ Erreur lors du lancement
    echo 💡 Lancez install.bat pour installer les dépendances
    echo.
    pause
)
