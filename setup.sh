#!/bin/bash

# 1. Polite Greeting & Status
echo "----------------------------------------------------------------"
echo "Initializing Ghost Office Hunter Environment: MacBook Pro M4"
echo "----------------------------------------------------------------"

# 2. Check Xcode Command Line Tools
if ! xcode-select -p &> /dev/null; then
    echo "Installing Xcode Command Line Tools..."
    xcode-select --install
    read -p "Press [Enter] once the Xcode tools installation is complete..."
else
    echo "✅ Xcode Command Line Tools detected."
fi

# 3. Check Homebrew (Essential for M4 Apple Silicon)
if ! command -v brew &> /dev/null; then
    echo "Installing Homebrew..."
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    
    # M4/Apple Silicon Path Setup
    echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> ~/.zprofile
    eval "$(/opt/homebrew/bin/brew shellenv)"
else
    echo "✅ Homebrew detected. Updating..."
    brew update
fi

# 4. Install Core Development Stack
echo "Installing Git, Python 3.12 (Stable), and Cursor..."
brew install git 
# FORCE Python 3.12 to avoid 3.14 compilation errors
brew install python@3.12 
brew install --cask cursor
brew install --cask lm-studio

# 5. Project-Specific Setup (The Agentic AI Layer)
echo "Setting up Python Virtual Environment..."
# We remove old venv if it exists to ensure a clean slate
if [ -d "venv" ]; then
    echo "Refreshing existing venv..."
    rm -rf venv
fi

# CRITICAL: We point directly to the 3.12 binary
/opt/homebrew/bin/python3.12 -m venv venv
echo "✅ Virtual environment created using Python 3.12."

# 6. Install Key AI Libraries (Targeting the venv directly)
echo "Installing CrewAI and Agentic dependencies..."

# CRITICAL M4 FIX: Use the full path to pip to guarantee venv installation
./venv/bin/pip install --upgrade pip
./venv/bin/pip install crewai crewai-tools langchain-community python-dotenv duckduckgo-search

# 7. Create Project Structure (Modular for Compliance Standards)
touch .env main.py tasks.py agents.py
# Add a robust gitignore so you don't leak API keys
echo ".env" >> .gitignore
echo "venv/" >> .gitignore
echo "__pycache__/" >> .gitignore

# Set up a dummy key
if [ ! -s .env ]; then
    echo "OPENAI_API_KEY=sk-proj-your_key_here_placeholder"
fi

# 8. Final Polish
echo "----------------------------------------------------------------"
echo "🎉 Setup Complete! Ghost Office Hunter is ready."
echo "IMPORTANT: In Cursor, press Cmd+Shift+P and select 'Python: Select Interpreter' -> point it to './venv/bin/python'"
echo "----------------------------------------------------------------"