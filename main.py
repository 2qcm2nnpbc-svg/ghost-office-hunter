"""Main entry point for Ghost Office Hunter."""
import argparse
import logging
import sys
from pathlib import Path
from typing import Optional

from crewai import Crew, Process

from agents import registry_researcher_agent
from tasks import investigation_task
from tools import GhostHunterSearchTool
from config import Config
from logger import setup_logger

# Initialize logger
logger = setup_logger()


def run_investigation(company_name: str, output_path: Optional[str] = None) -> str:
    """
    Run a forensic investigation on a company.
    
    Args:
        company_name: Name of the company to investigate
        output_path: Optional custom path for output file
        
    Returns:
        Path to the generated report file
        
    Raises:
        ValueError: If company name is empty
        RuntimeError: If investigation fails
    """
    if not company_name or not company_name.strip():
        raise ValueError("Company name cannot be empty")
    
    company_name = company_name.strip()
    logger.info(f"Starting investigation into: {company_name}")
    
    try:
        # Setup tools
        search_tool = GhostHunterSearchTool()
        logger.debug("Search tool initialized")
        
        # Setup agent
        investigator = registry_researcher_agent(tools=[search_tool], verbose=True)
        logger.debug("Investigator agent created")
        
        # Create task
        task = investigation_task(investigator, company_name)
        logger.debug("Investigation task created")
        
        # Assemble crew
        crew = Crew(
            agents=[investigator],
            tasks=[task],
            verbose=True,
            process=Process.sequential
        )
        logger.debug("Crew assembled")
        
        # Execute investigation
        logger.info("Executing investigation...")
        result = crew.kickoff()
        
        # Determine output path
        if not output_path:
            output_path = Config.get_output_path(company_name)
        
        # Save report
        output_file = Path(output_path)
        output_file.parent.mkdir(parents=True, exist_ok=True)
        
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(str(result))
        
        logger.info(f"Report generated successfully: {output_file}")
        return str(output_file)
        
    except Exception as e:
        logger.error(f"Investigation failed: {e}", exc_info=True)
        raise RuntimeError(f"Investigation failed: {str(e)}") from e


def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        description="Ghost Office Hunter - AI-powered compliance investigation tool",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python main.py "Three Arrows Capital"
  python main.py "Company Name" --output custom_report.md
  python main.py "Company Name" --verbose
        """
    )
    
    parser.add_argument(
        "company",
        type=str,
        help="Name of the company to investigate"
    )
    
    parser.add_argument(
        "--output", "-o",
        type=str,
        default=None,
        help="Custom output file path (default: reports/{company_name}_Forensic_Report.md)"
    )
    
    parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="Enable verbose logging"
    )
    
    args = parser.parse_args()
    
    # Configure logging level
    if args.verbose:
        logger.setLevel(logging.DEBUG)
        logger.debug("Verbose logging enabled")
    
    try:
        # Validate configuration
        Config.validate()
        
        # Run investigation
        output_file = run_investigation(args.company, args.output)
        
        # Print success message
        print("\n" + "=" * 60)
        print(f"✅ INVESTIGATION COMPLETE")
        print(f"📄 Report saved to: {output_file}")
        print("=" * 60)
        
        return 0
        
    except ValueError as e:
        logger.error(f"Configuration error: {e}")
        print(f"❌ Error: {e}", file=sys.stderr)
        return 1
        
    except RuntimeError as e:
        logger.error(f"Investigation error: {e}")
        print(f"❌ Investigation failed: {e}", file=sys.stderr)
        return 1
        
    except KeyboardInterrupt:
        logger.warning("Investigation interrupted by user")
        print("\n⚠️  Investigation interrupted by user", file=sys.stderr)
        return 130
        
    except Exception as e:
        logger.error(f"Unexpected error: {e}", exc_info=True)
        print(f"❌ Unexpected error: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())