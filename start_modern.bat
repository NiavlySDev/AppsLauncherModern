@echo off
title Lanceur d'Applications - Interface Moderne
color 0A

echo.
echo ================================================
echo    LANCEUR D'APPLICATIONS - INTERFACE MODERNE
echo ================================================
echo.
echo Initialisation...
echo.

REM Vérification de Python
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Python n'est pas installé ou accessible
    echo Installez Python depuis https://python.org
    pause
    exit /b 1
)

echo ✅ Python détecté
echo.

REM Vérification des dépendances
echo Vérification des dépendances...
python -c "import customtkinter, PIL" >nul 2>&1
if %errorlevel% neq 0 (
    echo ⚠️  Installation des dépendances manquantes...
    pip install customtkinter pillow
    if %errorlevel% neq 0 (
        echo ❌ Erreur lors de l'installation des dépendances
        pause
        exit /b 1
    )
)

echo ✅ Dépendances OK
echo.

REM Lancement de l'application
echo 🚀 Lancement de l'interface moderne...
echo.
python modern_launcher.py

if %errorlevel% neq 0 (
    echo.
    echo ❌ Erreur lors du lancement
    pause
)

echo.
echo Application fermée.
pause
