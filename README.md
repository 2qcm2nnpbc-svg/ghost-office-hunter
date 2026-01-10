# 👻 Ghost Office Hunter (AI Compliance Agent)

[![Python 3.12](https://img.shields.io/badge/Python-3.12-blue.svg)](https://www.python.org)
[![Framework: CrewAI](https://img.shields.io/badge/Framework-CrewAI-red.svg)](https://crewai.com)
[![Field: AML/KYC](https://img.shields.io/badge/Field-Compliance%20/%20AML-green.svg)](https://en.wikipedia.org/wiki/Anti-money_laundering)
[![Certification: Agentic AI](https://img.shields.io/badge/Certification-Reinvention%20with%20Agentic%20AI-blueviolet.svg)](https://www.credly.com/badges/5cc6097d-a216-42a4-8a26-793f1f8c0e40/public_url)

## 📺 Demo

Version 2: Enhancement - 10 Jan 2026
<p align="center">
  <video src="https://github.com/user-attachments/assets/a394e970-0a26-45df-bc48-09c4deab9c0b" width="100%" controls muted autoplay>
    Your browser does not support the video tag.
  </video>
</p>


Version 1: 
<p align="center">
  <video src="https://github.com/user-attachments/assets/de746eae-35a6-493a-960a-5724a1322ee6" width="100%" controls muted autoplay>
    Your browser does not support the video tag.
  </video>
</p>

> **💡 Watch for Agentic Reasoning:** At **0:12**, the agent encounters a tool syntax error. Instead of crashing, it autonomously analyzes the failure, adjusts its query parameters, and retries the search—demonstrating true self-correction.

---

## 🚀 Project Overview
**Ghost Office Hunter** is an autonomous AI agent designed to flag high-risk "Ghost Offices" and shell companies within the Singapore business ecosystem. 

By automating the tedious process of manual registry cross-referencing and adverse media screening, this tool serves as a force multiplier for **AML (Anti-Money Laundering)** and **KYC (Know Your Customer)** compliance teams.



## 🛠 Tech Stack & Architecture
* **Orchestration:** [CrewAI](https://github.com/joaomdmoura/crewai) for multi-agent role-playing and task delegation.
* **Intelligence:** ReAct (Reason + Act) prompting pattern for complex decision-making.
* **Search Engine:** Custom-built `ddgs` (DuckDuckGo) tool for real-time web scraping without API costs.
* **Environment:** Python 3.12 (Optimized for M4 MacBook Pro execution).

## 🔍 Forensic Capabilities
The agent executes a sophisticated **Search-Verify-Report** loop:
1.  **Physical Presence Audit:** Differentiates between legitimate operational headquarters and "virtual office" hubs or high-density co-working spaces.
2.  **Entity Clustering:** Identifies "Red Flag" patterns where dozens of unrelated entities are registered to a single, unmanned unit.
3.  **Adverse Media Intelligence:** Performs deep-web scans for regulatory actions, bankruptcy filings, and leadership sanctions (e.g., the **Three Arrows Capital** forensic case study shown in the demo).

## 📥 Installation & Usage

> **🚀 New to the project?** Check out the [Quick Start Guide](QUICKSTART.md) for a step-by-step walkthrough!

### Prerequisites
- Python 3.12 or higher
- OpenAI API key (required for CrewAI agents)

### Installation

#### Quick Setup (Recommended)

**On macOS/Linux:**
```bash
git clone https://github.com/your-username/ghost-office-hunter.git
cd ghost-office-hunter
./setup.sh
```

**On Windows:**
```cmd
git clone https://github.com/your-username/ghost-office-hunter.git
cd ghost-office-hunter
setup.bat
```

The setup script will:
- ✅ Check Python version (requires 3.12+)
- ✅ Create virtual environment
- ✅ Install all dependencies
- ✅ Create `.env` file from template
- ✅ Create reports directory

#### Manual Setup

1. **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/ghost-office-hunter.git
    cd ghost-office-hunter
    ```

2. **Create and activate virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Configure environment variables:**
    ```bash
    cp env.example .env
    # Edit .env and add your OPENAI_API_KEY
    ```

### Usage

#### Web UI (Recommended)

Launch the Streamlit web interface:

```bash
streamlit run app.py
```

Then open your browser to `http://localhost:8501` and use the interactive UI to:
- Enter company names
- Configure search settings
- View and download reports
- Monitor investigation progress

#### Command Line Interface

**Basic usage:**
```bash
python main.py "Company Name"
```

**With custom output path:**
```bash
python main.py "Company Name" --output custom_report.md
```

**With verbose logging:**
```bash
python main.py "Company Name" --verbose
```

**Get help:**
```bash
python main.py --help
```

### Configuration

Edit `.env` file to customize configuration:

```env
# Required
OPENAI_API_KEY=your_openai_api_key_here

# Optional: Model Configuration
OPENAI_MODEL_NAME=gpt-4
OPENAI_TEMPERATURE=0.7

# Optional: Search Configuration
SEARCH_MAX_RESULTS=10
SEARCH_REGION=wt-wt
SEARCH_SAFESEARCH=moderate

# Optional: Logging
LOG_LEVEL=INFO
LOG_FILE=ghost_office_hunter.log

# Optional: Output
OUTPUT_DIR=reports
```

### Output

Reports are saved to the `reports/` directory by default (configurable via `OUTPUT_DIR` environment variable). Each report is named `{Company_Name}_Forensic_Report.md`.

## 🏗️ Project Structure

```
ghost-office-hunter/
├── app.py               # Streamlit web UI
├── main.py              # Main entry point and CLI
├── agents.py            # Agent definitions
├── tasks.py             # Task definitions
├── tools.py             # Custom tools (search, etc.)
├── config.py            # Configuration management
├── logger.py            # Logging setup
├── requirements.txt     # Python dependencies
├── env.example          # Environment variables template
├── setup.sh             # Setup script (macOS/Linux)
├── setup.bat            # Setup script (Windows)
├── Makefile             # Make commands
├── .gitignore          # Git ignore rules
└── README.md           # This file
```

## 🔧 Development

### Code Quality
- Type hints throughout the codebase
- Comprehensive error handling
- Structured logging system
- Configuration management via environment variables

### Adding New Features
1. **New Agents**: Add to `agents.py`
2. **New Tasks**: Add to `tasks.py`
3. **New Tools**: Add to `tools.py`
4. **Configuration**: Update `config.py` and `env.example`

## 📝 License

This project is provided as-is for educational and demonstration purposes.

## ⚠️ Disclaimer
This project is a proof-of-concept developed for the **Agentic AI** course completion (Dec 2025). It is intended for educational and portfolio demonstration purposes only. 

**Important Notes:**
- Always verify AI-generated reports with human experts
- This tool is not a substitute for professional compliance review
- Results should be validated through official channels
- Use responsibly and in accordance with applicable laws and regulations
