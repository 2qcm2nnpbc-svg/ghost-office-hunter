# Quick Fix: Install Dependencies

The app isn't running because dependencies aren't installed. Here's how to fix it:

## Quick Fix (Choose One)

### Option 1: Use the run script (auto-installs)
```bash
./run.sh
```

### Option 2: Manual installation

**Step 1: Activate virtual environment**
```bash
source venv/bin/activate
```

**Step 2: Install dependencies**
```bash
pip install -r requirements.txt
```

**Step 3: Run the app**
```bash
streamlit run app.py
```

### Option 3: Re-run setup
```bash
./setup.sh
```

Then run:
```bash
streamlit run app.py
```

## Verify Installation

Run the diagnostic script:
```bash
python3 check_setup.py
```

It will tell you what's missing.

## Expected Output

After installation, you should see:
```
✅ streamlit is installed
✅ crewai is installed
✅ ddgs is installed
✅ dotenv is installed
```

Then the app will start and open at `http://localhost:8501`
