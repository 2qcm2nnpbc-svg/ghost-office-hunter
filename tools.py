"""Custom tools for Ghost Office Hunter."""
from typing import List, Dict, Any, Optional
import logging
import time

from crewai.tools import BaseTool
from ddgs import DDGS

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
