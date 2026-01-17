"""Custom tools for Ghost Office Hunter."""
from typing import List, Dict, Any, Optional
import logging
import time

from crewai.tools import BaseTool
from ddgs import DDGS
import yfinance as yf

from config import Config
from logger import setup_logger

logger = setup_logger()


class GhostHunterSearchTool(BaseTool):
    """Custom search tool for web-based company investigation."""
    
    name: str = "Ghost Hunter Search"
    description: str = (
        "Search the web for company addresses, news, directors, and regulatory actions. "
        "Useful for finding red flags, adverse media, and ghost office indicators. "
        "Returns relevant search results that can be analyzed for compliance risks."
    )

    def _run(self, query: str) -> str:
        """
        Execute web search query using DuckDuckGo.
        
        Args:
            query: Search query string
            
        Returns:
            Search results as string, or error message if search fails
        """
        max_retries = 3
        retry_delay = 2  # seconds
        
        for attempt in range(max_retries):
            try:
                logger.debug(f"Executing search query: {query} (attempt {attempt + 1}/{max_retries})")
                
                # DDGS API uses 'query' parameter (not 'keywords') in newer versions
                # Also, DDGS().text() returns an iterator, so we need to convert it to a list
                ddgs = DDGS()
                results_iterator = ddgs.text(
                    query=query,
                    region=Config.SEARCH_REGION,
                    safesearch=Config.SEARCH_SAFESEARCH,
                    max_results=Config.SEARCH_MAX_RESULTS
                )
                
                # Convert iterator to list
                results: List[Dict[str, Any]] = list(results_iterator) if results_iterator else []
                
                if not results:
                    logger.warning(f"No results found for query: {query}")
                    return "No results found for this search query. Try different search terms or check if the company name is spelled correctly."
                
                # Format results for better readability
                formatted_results = []
                for i, result in enumerate(results, 1):
                    if isinstance(result, dict):
                        title = result.get('title', 'No title')
                        body = result.get('body', 'No description')
                        href = result.get('href', 'No URL')
                        formatted_results.append(
                            f"Result {i}:\n"
                            f"Title: {title}\n"
                            f"Description: {body}\n"
                            f"URL: {href}\n"
                        )
                    else:
                        # Handle case where result might be a string
                        formatted_results.append(f"Result {i}: {str(result)}\n")
                
                result_str = "\n".join(formatted_results)
                logger.debug(f"Search returned {len(results)} results")
                return result_str if result_str else "No results found."
                
            except TypeError as e:
                # API signature error - this shouldn't happen with the fix, but handle it
                error_msg = (
                    f"Search API error: The DuckDuckGo search API may have changed. "
                    f"Technical details: {str(e)}. Please check the ddgs library version."
                )
                logger.error(f"Search API error for query '{query}': {e}", exc_info=True)
                if attempt < max_retries - 1:
                    logger.info(f"Retrying in {retry_delay} seconds...")
                    time.sleep(retry_delay)
                    continue
                return error_msg
                
            except ConnectionError as e:
                # Network connectivity issue
                error_msg = (
                    f"Network connection error: Unable to reach DuckDuckGo search service. "
                    f"This may be due to network connectivity issues, firewall restrictions, or service unavailability. "
                    f"Please check your internet connection and try again."
                )
                logger.error(f"Network error for query '{query}': {e}", exc_info=True)
                if attempt < max_retries - 1:
                    logger.info(f"Retrying in {retry_delay} seconds...")
                    time.sleep(retry_delay)
                    continue
                return error_msg
                
            except Exception as e:
                error_type = type(e).__name__
                error_msg = (
                    f"Search failed due to technical constraint: {error_type}. "
                    f"Error details: {str(e)}. "
                    f"This may be due to DuckDuckGo rate limiting, service changes, or network issues. "
                    f"Please try again later or use alternative search methods."
                )
                logger.error(f"Search error for query '{query}': {e}", exc_info=True)
                if attempt < max_retries - 1:
                    logger.info(f"Retrying in {retry_delay} seconds...")
                    time.sleep(retry_delay)
                    continue
                return error_msg
        
        # If all retries failed
        return (
            f"Search failed after {max_retries} attempts. "
            f"Technical constraints may include: DuckDuckGo rate limiting, network connectivity issues, "
            f"or service unavailability. Please try again later."
        )


class ShariahComplianceTool(BaseTool):
    """Tool for checking Shariah compliance of stocks using AAOIFI financial ratios."""
    
    name: str = "Shariah Compliance Checker"
    description: str = (
        "Checks a stock ticker symbol against AAOIFI Shariah compliance standards. "
        "Evaluates debt ratio and cash ratio against the 33% threshold. "
        "Returns PASS/FAIL status with detailed financial ratios. "
        "Use this tool when you need to verify if a publicly traded company complies with Shariah principles."
    )

    def _run(self, ticker_symbol: str) -> str:
        """
        Check a stock against AAOIFI Shariah compliance standards.
        
        Args:
            ticker_symbol: Stock ticker symbol (e.g., "WTS", "AAPL", "MSFT")
            
        Returns:
            Formatted string with compliance status and financial ratios
        """
        try:
            logger.info(f"Checking Shariah compliance for ticker: {ticker_symbol}")
            
            # Fetch stock data
            stock = yf.Ticker(ticker_symbol)
            info = stock.info
            
            # Extract financial data
            market_cap = info.get('marketCap')
            total_debt = info.get('totalDebt', 0)
            total_cash = info.get('totalCash', 0)
            
            # Validate market cap
            if not market_cap or market_cap == 0:
                error_msg = f"Market Cap data missing or zero for {ticker_symbol}. This may indicate the ticker is invalid or the company is not publicly traded."
                logger.warning(error_msg)
                return error_msg
            
            # Calculate ratios
            debt_ratio = (total_debt / market_cap) * 100 if market_cap > 0 else 0
            cash_ratio = (total_cash / market_cap) * 100 if market_cap > 0 else 0
            
            # Apply AAOIFI thresholds (<33%)
            debt_pass = debt_ratio < 33.0
            cash_pass = cash_ratio < 33.0
            overall_status = "PASS" if (debt_pass and cash_pass) else "FAIL"
            
            # Format results
            result = {
                "Ticker": ticker_symbol,
                "Status": overall_status,
                "Debt_Ratio": f"{debt_ratio:.2f}%",
                "Debt_Threshold": "<33%",
                "Debt_Pass": "✓" if debt_pass else "✗",
                "Cash_Ratio": f"{cash_ratio:.2f}%",
                "Cash_Threshold": "<33%",
                "Cash_Pass": "✓" if cash_pass else "✗",
                "Market_Cap": f"${market_cap:,.0f}"
            }
            
            # Format output string
            output_lines = [
                f"=== Shariah Compliance Check for {ticker_symbol} ===",
                f"Overall Status: {overall_status}",
                "",
                "Financial Ratios (AAOIFI Standards):",
                f"  Debt Ratio: {result['Debt_Ratio']} (Threshold: {result['Debt_Threshold']}) {result['Debt_Pass']}",
                f"  Cash Ratio: {result['Cash_Ratio']} (Threshold: {result['Cash_Threshold']}) {result['Cash_Pass']}",
                "",
                f"Market Capitalization: {result['Market_Cap']}",
                "",
                "Note: Both ratios must be below 33% to PASS Shariah compliance."
            ]
            
            output = "\n".join(output_lines)
            logger.info(f"Shariah compliance check completed for {ticker_symbol}: {overall_status}")
            return output
            
        except Exception as e:
            error_msg = f"Error checking Shariah compliance for {ticker_symbol}: {str(e)}. The ticker symbol may be invalid or financial data may not be available."
            logger.error(error_msg, exc_info=True)
            return error_msg


class ShariahBusinessActivityTool(BaseTool):
    """Tool for fetching and analyzing company business summary for Shariah compliance."""
    
    name: str = "Shariah Business Activity Analyzer"
    description: str = (
        "Fetches a company's business summary from financial data and provides it for analysis. "
        "The business summary should be analyzed for prohibited activities such as alcohol, gambling, "
        "pork products, adult entertainment, and interest-based income. "
        "Use this tool to get the business description that needs to be checked against Shariah principles."
    )

    def _run(self, ticker_symbol: str) -> str:
        """
        Fetch business summary from yfinance for Shariah compliance analysis.
        
        Args:
            ticker_symbol: Stock ticker symbol (e.g., "WTS", "AAPL", "MSFT")
            
        Returns:
            Formatted string with business summary and company information
        """
        try:
            logger.info(f"Fetching business summary for ticker: {ticker_symbol}")
            
            # Fetch stock data
            stock = yf.Ticker(ticker_symbol)
            info = stock.info
            
            # Extract business information
            company_name = info.get('longName') or info.get('shortName', ticker_symbol)
            business_summary = info.get('longBusinessSummary') or info.get('businessSummary', '')
            industry = info.get('industry', 'N/A')
            sector = info.get('sector', 'N/A')
            
            if not business_summary:
                warning_msg = (
                    f"Business summary not available for {ticker_symbol} ({company_name}). "
                    f"This may indicate the company data is incomplete or the ticker is invalid."
                )
                logger.warning(warning_msg)
                return warning_msg
            
            # Format output for LLM analysis
            output_lines = [
                f"=== Business Summary for {company_name} ({ticker_symbol}) ===",
                "",
                f"Industry: {industry}",
                f"Sector: {sector}",
                "",
                "Business Summary:",
                business_summary,
                "",
                "=== Analysis Required ===",
                "Please analyze this business summary for Shariah compliance. Look for:",
                "- Alcohol-related activities (brewing, distilling, wine, spirits, etc.)",
                "- Gambling activities (casinos, betting, lottery, gaming, etc.)",
                "- Pork products (pork, bacon, ham, etc.)",
                "- Adult entertainment (pornography, adult content, etc.)",
                "- Interest-based income (riba, usury, conventional banking interest, etc.)",
                "- Other prohibited activities according to Islamic principles",
                "",
                "Flag the company as NON-COMPLIANT if any prohibited activities are found in the business description."
            ]
            
            output = "\n".join(output_lines)
            logger.info(f"Business summary fetched for {ticker_symbol}")
            return output
            
        except Exception as e:
            error_msg = (
                f"Error fetching business summary for {ticker_symbol}: {str(e)}. "
                f"The ticker symbol may be invalid or business data may not be available."
            )
            logger.error(error_msg, exc_info=True)
            return error_msg
