#!/bin/bash
# Setup script for Ghost Office Hunter
# This script automates the initial setup process

set -e  # Exit on error

echo "👻 Ghost Office Hunter - Setup Script"
echo "======================================"
echo ""

# Colors for output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Check Python version
echo "📋 Checking Python version..."
PYTHON_VERSION=$(python3 --version 2>&1 | awk '{print $2}')
PYTHON_MAJOR=$(echo $PYTHON_VERSION | cut -d. -f1)
PYTHON_MINOR=$(echo $PYTHON_VERSION | cut -d. -f2)

if [ "$PYTHON_MAJOR" -lt 3 ] || ([ "$PYTHON_MAJOR" -eq 3 ] && [ "$PYTHON_MINOR" -lt 12 ]); then
    echo -e "${RED}❌ Error: Python 3.12 or higher is required. Found: Python $PYTHON_VERSION${NC}"
    exit 1
fi

echo -e "${GREEN}✅ Python $PYTHON_VERSION found${NC}"
echo ""

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
    echo -e "${GREEN}✅ Virtual environment created${NC}"
else
    echo -e "${YELLOW}⚠️  Virtual environment already exists${NC}"
fi

echo ""

# Activate virtual environment and upgrade pip
echo "⬆️  Upgrading pip..."
source venv/bin/activate
pip install --upgrade pip --quiet

echo ""

# Install dependencies
echo "📥 Installing dependencies..."
pip install -r requirements.txt

echo ""
echo -e "${GREEN}✅ Dependencies installed${NC}"
echo ""

# Setup .env file
if [ ! -f ".env" ]; then
    if [ -f "env.example" ]; then
        echo "📝 Creating .env file from env.example..."
        cp env.example .env
        echo -e "${GREEN}✅ .env file created${NC}"
        echo ""
        echo -e "${YELLOW}⚠️  IMPORTANT: Please edit .env and add your OPENAI_API_KEY${NC}"
        echo "   You can do this by running: nano .env  or  vim .env"
    else
        echo -e "${YELLOW}⚠️  env.example not found. Please create .env manually${NC}"
    fi
else
    echo -e "${YELLOW}⚠️  .env file already exists${NC}"
fi

echo ""

# Create reports directory
if [ ! -d "reports" ]; then
    echo "📁 Creating reports directory..."
    mkdir -p reports
    echo -e "${GREEN}✅ Reports directory created${NC}"
else
    echo -e "${YELLOW}⚠️  Reports directory already exists${NC}"
fi

echo ""
echo "======================================"
echo -e "${GREEN}✅ Setup complete!${NC}"
echo ""
echo "Next steps:"
echo "1. Edit .env file and add your OPENAI_API_KEY:"
echo "   ${YELLOW}nano .env${NC}  or  ${YELLOW}vim .env${NC}"
echo ""
echo "2. Activate the virtual environment (if not already active):"
echo "   ${YELLOW}source venv/bin/activate${NC}"
echo ""
echo "3. Run the application:"
echo ""
echo "   Option A - Web UI (Recommended):"
echo "   ${YELLOW}streamlit run app.py${NC}"
echo "   Or: ${YELLOW}make streamlit${NC}"
echo ""
echo "   Option B - Command Line:"
echo "   ${YELLOW}python main.py \"Company Name\"${NC}"
echo "   Or: ${YELLOW}make run COMPANY=\"Company Name\"${NC}"
echo ""
