@echo off
REM Run script for Ghost Office Hunter (Windows)

echo 👻 Ghost Office Hunter - Starting Application
echo ==============================================
echo.

REM Check if venv exists
if not exist "venv" (
    echo ❌ Virtual environment not found!
    echo Please run setup first:
    echo   setup.bat
    exit /b 1
)

REM Check if .env exists
if not exist ".env" (
    echo ⚠️  .env file not found!
    echo Creating from template...
    if exist "env.example" (
        copy env.example .env >nul
        echo ⚠️  Please edit .env and add your OPENAI_API_KEY
    ) else (
        echo ❌ env.example not found!
        exit /b 1
    )
)

echo 📦 Checking dependencies...
call venv\Scripts\activate.bat

REM Check if streamlit is installed
python -c "import streamlit" >nul 2>&1
if errorlevel 1 (
    echo 📥 Installing missing dependencies...
    pip install -r requirements.txt --quiet
)

echo.
echo ✅ Starting Streamlit UI...
echo.
echo 🌐 The app will open in your browser at: http://localhost:8501
echo.
echo Press Ctrl+C to stop the server
echo.

REM Run streamlit
streamlit run app.py
