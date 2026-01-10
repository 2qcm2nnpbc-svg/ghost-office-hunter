# 🚀 Quick Start Guide

Get up and running with Ghost Office Hunter in under 5 minutes!

## Prerequisites

- Python 3.12 or higher
- OpenAI API key ([Get one here](https://platform.openai.com/api-keys))

## Step 1: Clone and Setup

**macOS/Linux:**
```bash
git clone https://github.com/your-username/ghost-office-hunter.git
cd ghost-office-hunter
./setup.sh
```

**Windows:**
```cmd
git clone https://github.com/your-username/ghost-office-hunter.git
cd ghost-office-hunter
setup.bat
```

The setup script will automatically:
- ✅ Check Python version
- ✅ Create virtual environment
- ✅ Install all dependencies
- ✅ Create `.env` file
- ✅ Create reports directory

## Step 2: Configure API Key

Edit the `.env` file and add your OpenAI API key:

```bash
# macOS/Linux
nano .env

# Windows
notepad .env
```

Set your API key:
```env
OPENAI_API_KEY=sk-your-actual-api-key-here
```

## Step 3: Run Your First Investigation

**Activate virtual environment (if not already active):**

```bash
# macOS/Linux
source venv/bin/activate

# Windows
venv\Scripts\activate
```

### Option A: Web UI (Recommended) 🎨

Launch the Streamlit web interface:

```bash
streamlit run app.py
```

Or using Makefile:
```bash
make streamlit
```

Then open your browser to `http://localhost:8501` and use the interactive interface!

### Option B: Command Line 💻

**Run the investigation:**
```bash
python main.py "Three Arrows Capital"
```

Or use the Makefile:
```bash
make run COMPANY="Three Arrows Capital"
```

## Step 4: View Results

Your report will be saved to:
```
reports/Three_Arrows_Capital_Forensic_Report.md
```

## Common Commands

### Web UI
```bash
# Launch Streamlit UI
streamlit run app.py

# Or using Makefile
make streamlit
```

### Command Line
```bash
# Run with verbose logging
python main.py "Company Name" --verbose

# Custom output location
python main.py "Company Name" --output my_report.md

# Get help
python main.py --help

# Using Makefile
make run COMPANY="Company Name"
make run-verbose COMPANY="Company Name"
make streamlit
make help
```

## Troubleshooting

### "ModuleNotFoundError: No module named 'crewai'"
- Make sure you've activated the virtual environment: `source venv/bin/activate`
- Reinstall dependencies: `pip install -r requirements.txt`

### "OPENAI_API_KEY is required"
- Check that your `.env` file exists and contains `OPENAI_API_KEY=your-key-here`
- Make sure you're in the project root directory

### "Permission denied" on setup.sh
- Make it executable: `chmod +x setup.sh`

## Next Steps

- Read the full [README.md](README.md) for detailed documentation
- Check [CHANGELOG.md](CHANGELOG.md) for version history
- Customize configuration in `.env` file

Happy hunting! 👻
