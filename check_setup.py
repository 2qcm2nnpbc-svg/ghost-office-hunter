#!/usr/bin/env python3
"""Check setup and diagnose issues."""
import sys
import os
from pathlib import Path

def check_file(filepath, description):
    """Check if a file exists."""
    exists = Path(filepath).exists()
    status = "✅" if exists else "❌"
    print(f"{status} {description}: {filepath}")
    return exists

def check_module(module_name):
    """Check if a Python module is installed."""
    try:
        __import__(module_name)
        print(f"✅ {module_name} is installed")
        return True
    except ImportError:
        print(f"❌ {module_name} is NOT installed")
        return False

print("🔍 Ghost Office Hunter - Setup Diagnostic")
print("=" * 50)
print()

# Check files
print("📁 Checking files...")
files_ok = True
files_ok &= check_file("app.py", "Streamlit app")
files_ok &= check_file("main.py", "Main module")
files_ok &= check_file("config.py", "Config module")
files_ok &= check_file("requirements.txt", "Requirements file")
files_ok &= check_file(".env", "Environment file")
files_ok &= check_file("venv", "Virtual environment")

print()

# Check Python modules
print("📦 Checking Python modules...")
modules_ok = True
modules_ok &= check_module("streamlit")
modules_ok &= check_module("crewai")
modules_ok &= check_module("ddgs")
modules_ok &= check_module("dotenv")

print()

# Check environment variables
print("🔐 Checking environment variables...")
try:
    from dotenv import load_dotenv
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")
    if api_key:
        masked_key = api_key[:8] + "..." + api_key[-4:] if len(api_key) > 12 else "***"
        print(f"✅ OPENAI_API_KEY is set: {masked_key}")
    else:
        print("❌ OPENAI_API_KEY is NOT set")
except Exception as e:
    print(f"⚠️  Could not check environment: {e}")

print()
print("=" * 50)

if not files_ok or not modules_ok:
    print()
    print("❌ Setup incomplete!")
    print()
    print("To fix:")
    print("1. Run: ./setup.sh (macOS/Linux) or setup.bat (Windows)")
    print("2. Or manually:")
    print("   - source venv/bin/activate")
    print("   - pip install -r requirements.txt")
    print("   - cp env.example .env")
    print("   - Edit .env and add OPENAI_API_KEY")
    sys.exit(1)
else:
    print()
    print("✅ Setup looks good!")
    print()
    print("To run the app:")
    print("  streamlit run app.py")
    print("Or:")
    print("  ./run.sh (macOS/Linux) or run.bat (Windows)")
