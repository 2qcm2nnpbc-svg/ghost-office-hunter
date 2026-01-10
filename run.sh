#!/bin/bash
# Run script for Ghost Office Hunter

set -e

# Colors
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m'

echo "👻 Ghost Office Hunter - Starting Application"
echo "=============================================="
echo ""

# Check if venv exists
if [ ! -d "venv" ]; then
    echo -e "${RED}❌ Virtual environment not found!${NC}"
    echo "Please run setup first:"
    echo "  ./setup.sh"
    exit 1
fi

# Check if .env exists
if [ ! -f ".env" ]; then
    echo -e "${YELLOW}⚠️  .env file not found!${NC}"
    echo "Creating from template..."
    if [ -f "env.example" ]; then
        cp env.example .env
        echo -e "${YELLOW}⚠️  Please edit .env and add your OPENAI_API_KEY${NC}"
    else
        echo -e "${RED}❌ env.example not found!${NC}"
        exit 1
    fi
fi

# Use venv's Python directly
VENV_PYTHON="venv/bin/python"
VENV_PIP="venv/bin/pip"

# Check if venv Python exists
if [ ! -f "$VENV_PYTHON" ]; then
    echo -e "${RED}❌ Virtual environment Python not found!${NC}"
    echo "Please run setup first:"
    echo "  ./setup.sh"
    exit 1
fi

# Check if streamlit is installed
echo "🔍 Checking dependencies..."
if ! $VENV_PYTHON -c "import streamlit" 2>/dev/null; then
    echo "📥 Installing dependencies (this may take a minute)..."
    $VENV_PIP install -r requirements.txt
    echo "✅ Dependencies installed!"
else
    echo "✅ All dependencies are installed"
fi

echo ""
echo -e "${GREEN}✅ Starting Streamlit UI...${NC}"
echo ""
echo "🌐 The app will open in your browser at: http://localhost:8501"
echo ""
echo "Press Ctrl+C to stop the server"
echo ""

# Run streamlit using venv's Python
$VENV_PYTHON -m streamlit run app.py
