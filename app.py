"""Streamlit UI for Ghost Office Hunter."""
import streamlit as st
import sys
from pathlib import Path
from typing import Optional

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent))

from main import run_investigation
from config import Config

# Page configuration
st.set_page_config(
    page_title="Ghost Office Hunter",
    page_icon="👻",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
    <style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 0.5rem;
    }
    .subtitle {
        text-align: center;
        color: #666;
        margin-bottom: 2rem;
    }
    .stButton>button {
        width: 100%;
        background-color: #1f77b4;
        color: white;
        font-weight: bold;
        padding: 0.5rem 1rem;
        border-radius: 0.5rem;
    }
    .stButton>button:hover {
        background-color: #1565a0;
    }
    .info-box {
        padding: 1rem;
        border-radius: 0.5rem;
        background-color: #f0f2f6;
        border-left: 4px solid #1f77b4;
    }
    </style>
    """, unsafe_allow_html=True)


def main():
    """Main Streamlit application."""
    
    # Header
    st.markdown('<h1 class="main-header">👻 Ghost Office Hunter</h1>', unsafe_allow_html=True)
    st.markdown(
        '<p class="subtitle">AI-Powered Compliance Investigation Tool for Detecting Ghost Offices and Shell Companies</p>',
        unsafe_allow_html=True
    )
    
    # Sidebar
    with st.sidebar:
        st.header("⚙️ Configuration")
        
        # Check if API key is configured
        try:
            Config.validate()
            st.success("✅ API Key Configured")
        except ValueError as e:
            st.error(f"❌ Configuration Error: {e}")
            st.info("💡 Please set your OPENAI_API_KEY in the .env file")
            st.stop()
        
        st.divider()
        
        st.subheader("🔍 Search Settings")
        search_max_results = st.slider(
            "Max Search Results",
            min_value=5,
            max_value=20,
            value=Config.SEARCH_MAX_RESULTS,
            help="Maximum number of search results to retrieve"
        )
        
        search_region = st.selectbox(
            "Search Region",
            options=["wt-wt", "sg-en", "us-en", "uk-en"],
            index=0 if Config.SEARCH_REGION == "wt-wt" else 1,
            help="Region for web search"
        )
        
        st.divider()
        
        st.subheader("📊 About")
        st.markdown("""
        **Ghost Office Hunter** is an autonomous AI agent designed to flag 
        high-risk "Ghost Offices" and shell companies.
        
        **Features:**
        - 🔍 Adverse Media Check
        - 🏢 Ghost Office Detection
        - 📋 Corporate Structure Analysis
        - 🕌 Shariah Compliance Check (Optional)
        - 📄 Automated Report Generation
        """)
        
        st.divider()
        
        st.markdown("""
        <div style='text-align: center; color: #666; font-size: 0.8rem;'>
            Version 1.0.0<br>
            Built with CrewAI & Streamlit
        </div>
        """, unsafe_allow_html=True)
    
    # Main content area
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.header("🔎 Company Investigation")
        
        # Company name input
        company_name = st.text_input(
            "Company Name",
            placeholder="Enter company name (e.g., Three Arrows Capital)",
            help="Enter the name of the company you want to investigate"
        )
        
        # Advanced options (collapsible)
        with st.expander("⚙️ Advanced Options"):
            custom_output = st.text_input(
                "Custom Output Path (Optional)",
                placeholder="Leave empty for default location",
                help="Custom path for the report file"
            )
            
            verbose_mode = st.checkbox(
                "Verbose Logging",
                value=False,
                help="Enable detailed logging output"
            )
            
            st.divider()
            
            # Shariah compliance options
            st.subheader("🕌 Shariah Compliance Check")
            include_shariah = st.checkbox(
                "Include Shariah Compliance Check",
                value=False,
                help="Check company against AAOIFI Shariah compliance standards"
            )
            
            ticker_symbol = None
            if include_shariah:
                ticker_symbol = st.text_input(
                    "Stock Ticker Symbol",
                    placeholder="e.g., WTS, AAPL, MSFT",
                    help="Stock ticker symbol required for Shariah compliance check"
                )
                st.info("💡 Shariah compliance checks debt and cash ratios against 33% threshold using AAOIFI standards.")
    
    with col2:
        st.header("📋 Quick Info")
        st.info("""
        **What gets investigated:**
        
        1. **Adverse Media**
        - Fraud, collapse, arrests
        - Regulatory actions
        - Bankruptcy filings
        
        2. **Ghost Office Check**
        - Co-working spaces
        - Virtual offices
        - Entity clustering
        
        3. **Corporate Structure**
        - Shell company indicators
        - Red flags
        
        4. **Shariah Compliance** (Optional)
        - AAOIFI financial ratios
        - Debt and cash ratio checks
        - Compliance status
        """)
    
    # Run investigation button
    st.divider()
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        run_button = st.button(
            "🚀 Start Investigation",
            type="primary",
            use_container_width=True
        )
    
    # Initialize session state
    if "investigation_result" not in st.session_state:
        st.session_state.investigation_result = None
    if "report_path" not in st.session_state:
        st.session_state.report_path = None
    if "report_content" not in st.session_state:
        st.session_state.report_content = None
    
    # Run investigation
    if run_button:
        if not company_name or not company_name.strip():
            st.error("❌ Please enter a company name to investigate")
        else:
            # Store original config values
            original_max_results = Config.SEARCH_MAX_RESULTS
            original_region = Config.SEARCH_REGION
            
            try:
                # Temporarily update config for this investigation
                # Note: This modifies class attributes, which affects all instances
                # In production, consider using a context manager or passing params directly
                Config.SEARCH_MAX_RESULTS = search_max_results
                Config.SEARCH_REGION = search_region
                
                # Show progress
                with st.spinner("🔍 Investigating company... This may take a few minutes."):
                    progress_bar = st.progress(0)
                    status_text = st.empty()
                    
                    status_text.text("Initializing investigation...")
                    progress_bar.progress(10)
                    
                    status_text.text("Setting up search tools...")
                    progress_bar.progress(20)
                    
                    status_text.text("Creating AI agent...")
                    progress_bar.progress(30)
                    
                    status_text.text("Executing investigation...")
                    progress_bar.progress(50)
                    
                    # Run investigation
                    output_path = custom_output.strip() if custom_output.strip() else None
                    ticker = ticker_symbol.strip() if ticker_symbol and ticker_symbol.strip() else None
                    
                    # Validate Shariah compliance arguments
                    shariah_enabled = include_shariah and ticker
                    if include_shariah and not ticker:
                        st.warning("⚠️ Shariah compliance requested but no ticker symbol provided. Proceeding without Shariah check.")
                    
                    report_path = run_investigation(
                        company_name.strip(), 
                        output_path,
                        include_shariah=shariah_enabled,
                        ticker_symbol=ticker
                    )
                    
                    progress_bar.progress(80)
                    status_text.text("Generating report...")
                    
                    # Read report content
                    with open(report_path, "r", encoding="utf-8") as f:
                        report_content = f.read()
                    
                    progress_bar.progress(100)
                    status_text.text("✅ Investigation complete!")
                    
                    # Store in session state
                    st.session_state.investigation_result = "success"
                    st.session_state.report_path = report_path
                    st.session_state.report_content = report_content
                    
                    # Reset progress
                    progress_bar.empty()
                    status_text.empty()
                    
                    st.success(f"✅ Investigation complete! Report saved to: `{report_path}`")
                    
            except ValueError as e:
                st.error(f"❌ Configuration Error: {e}")
                st.session_state.investigation_result = "error"
            except RuntimeError as e:
                st.error(f"❌ Investigation Failed: {e}")
                st.session_state.investigation_result = "error"
            except Exception as e:
                st.error(f"❌ Unexpected Error: {e}")
                st.session_state.investigation_result = "error"
            finally:
                # Restore original config
                Config.SEARCH_MAX_RESULTS = original_max_results
                Config.SEARCH_REGION = original_region
    
    # Display results
    if st.session_state.investigation_result == "success" and st.session_state.report_content:
        st.divider()
        st.header("📄 Investigation Report")
        
        # Report metadata
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Company", company_name if company_name else "N/A")
        with col2:
            st.metric("Report Location", Path(st.session_state.report_path).name)
        
        # Download button
        st.download_button(
            label="📥 Download Report",
            data=st.session_state.report_content,
            file_name=Path(st.session_state.report_path).name,
            mime="text/markdown",
            use_container_width=True
        )
        
        # Display report
        st.markdown("### Report Content")
        with st.expander("📖 View Full Report", expanded=True):
            st.markdown(st.session_state.report_content)
        
        # Report preview in code block
        with st.expander("📋 Raw Markdown"):
            st.code(st.session_state.report_content, language="markdown")


if __name__ == "__main__":
    main()
