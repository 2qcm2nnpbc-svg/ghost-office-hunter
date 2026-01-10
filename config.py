"""Configuration management for Ghost Office Hunter."""
import os
from typing import Optional
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


class Config:
    """Application configuration."""
    
    # OpenAI Configuration
    OPENAI_API_KEY: Optional[str] = os.getenv("OPENAI_API_KEY")
    OPENAI_MODEL_NAME: str = os.getenv("OPENAI_MODEL_NAME", "gpt-4")
    OPENAI_TEMPERATURE: float = float(os.getenv("OPENAI_TEMPERATURE", "0.7"))
    
    # Search Configuration
    SEARCH_MAX_RESULTS: int = int(os.getenv("SEARCH_MAX_RESULTS", "10"))
    SEARCH_REGION: str = os.getenv("SEARCH_REGION", "wt-wt")
    SEARCH_SAFESEARCH: str = os.getenv("SEARCH_SAFESEARCH", "moderate")
    
    # Logging Configuration
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")
    LOG_FILE: Optional[str] = os.getenv("LOG_FILE")
    
    # Output Configuration
    OUTPUT_DIR: str = os.getenv("OUTPUT_DIR", "reports")
    
    @classmethod
    def validate(cls) -> None:
        """Validate required configuration."""
        if not cls.OPENAI_API_KEY:
            raise ValueError(
                "OPENAI_API_KEY is required. Please set it in your .env file or environment variables."
            )
    
    @classmethod
    def get_output_path(cls, company_name: str) -> str:
        """Generate output file path for a company report."""
        os.makedirs(cls.OUTPUT_DIR, exist_ok=True)
        # Sanitize company name for filename
        safe_name = "".join(c for c in company_name if c.isalnum() or c in (' ', '-', '_')).strip()
        safe_name = safe_name.replace(' ', '_')
        return os.path.join(cls.OUTPUT_DIR, f"{safe_name}_Forensic_Report.md")
