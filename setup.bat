@echo off
REM Setup script for Ghost Office Hunter (Windows)
REM This script automates the initial setup process

echo 👻 Ghost Office Hunter - Setup Script
echo ======================================
echo.

REM Check Python version
echo 📋 Checking Python version...
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Error: Python is not installed or not in PATH
    exit /b 1
)

echo ✅ Python found
echo.

REM Create virtual environment if it doesn't exist
if not exist "venv" (
    echo 📦 Creating virtual environment...
    python -m venv venv
    echo ✅ Virtual environment created
) else (
    echo ⚠️  Virtual environment already exists
)

echo.

REM Activate virtual environment and upgrade pip
echo ⬆️  Upgrading pip...
call venv\Scripts\activate.bat
python -m pip install --upgrade pip --quiet

echo.

REM Install dependencies
echo 📥 Installing dependencies...
pip install -r requirements.txt

echo.
echo ✅ Dependencies installed
echo.

REM Setup .env file
if not exist ".env" (
    if exist "env.example" (
        echo 📝 Creating .env file from env.example...
        copy env.example .env >nul
        echo ✅ .env file created
        echo.
        echo ⚠️  IMPORTANT: Please edit .env and add your OPENAI_API_KEY
        echo    You can do this by running: notepad .env
    ) else (
        echo ⚠️  env.example not found. Please create .env manually
    )
) else (
    echo ⚠️  .env file already exists
)

echo.

REM Create reports directory
if not exist "reports" (
    echo 📁 Creating reports directory...
    mkdir reports
    echo ✅ Reports directory created
) else (
    echo ⚠️  Reports directory already exists
)

echo.
echo ======================================
echo ✅ Setup complete!
echo.
echo Next steps:
echo 1. Edit .env file and add your OPENAI_API_KEY:
echo    notepad .env
echo.
echo 2. Activate the virtual environment:
echo    venv\Scripts\activate.bat
echo.
echo 3. Run the application:
echo.
echo    Option A - Web UI (Recommended):
echo    streamlit run app.py
echo.
echo    Option B - Command Line:
echo    python main.py "Company Name"
echo.
