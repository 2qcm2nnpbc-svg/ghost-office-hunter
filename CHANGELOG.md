# Changelog

## [1.1.1] - Search Tool Fix

### Fixed
- **Critical Bug**: Fixed DuckDuckGo search API compatibility issue
  - Changed `keywords` parameter to `query` parameter (API update)
  - Added iterator-to-list conversion for search results
  - This fixes the "technical constraints" error that prevented searches

### Improved
- **Error Handling**: Enhanced search tool error handling with:
  - Retry logic (3 attempts with 2-second delays)
  - Specific error messages for different failure types
  - Better user guidance when searches fail
- **Error Messages**: More informative error messages explaining technical constraints

### Documentation
- Added `TECHNICAL_CONSTRAINTS.md` documenting the issue and fix

## [1.1.0] - Streamlit UI Release

### Added
- **Streamlit Web UI**: Beautiful, interactive web interface for running investigations
- **Real-time Progress**: Progress bars and status updates during investigations
- **Report Viewer**: Built-in markdown viewer for generated reports
- **Download Functionality**: Download reports directly from the UI
- **Configuration Sidebar**: Adjustable search settings (max results, region)
- **Streamlit Configuration**: Custom theme and server settings
- **Makefile Command**: `make streamlit` for easy UI launch

### Improved
- Better user experience with visual interface
- No need to use command line for basic operations
- Real-time feedback during investigations

## [1.0.0] - Production Ready Release

### Added
- **Logging System**: Comprehensive logging with file and console handlers
- **Configuration Management**: Centralized config via `config.py` with environment variable support
- **CLI Interface**: Professional command-line interface with argparse
- **Error Handling**: Robust error handling with proper exception types
- **Type Hints**: Full type annotations throughout the codebase
- **Code Documentation**: Comprehensive docstrings for all modules and functions
- **Project Structure**: Better separation of concerns (tools, agents, tasks, config)
- **Environment Template**: `env.example` file for easy setup
- **Package Setup**: `setup.py` and `pyproject.toml` for proper package distribution
- **Development Tools**: 
  - Makefile for common tasks
  - Pre-commit hooks configuration
  - Improved `.gitignore`
- **Enhanced README**: Updated with comprehensive usage instructions

### Changed
- **Main Entry Point**: Refactored `main.py` with proper CLI and error handling
- **Tool Definition**: Moved to separate `tools.py` module
- **Agent Creation**: Enhanced with type hints and better parameter handling
- **Task Definition**: Improved task descriptions and expected outputs
- **Output Management**: Reports now saved to configurable `reports/` directory

### Improved
- **Code Quality**: Type hints, docstrings, and better structure
- **User Experience**: Better CLI with help text and examples
- **Maintainability**: Modular design with clear separation of concerns
- **Production Readiness**: Error handling, logging, and configuration management

### Security
- Environment variables for sensitive data (API keys)
- Proper `.gitignore` to prevent committing secrets
- Input validation and sanitization

### Documentation
- Comprehensive README with installation and usage instructions
- Inline code documentation
- Configuration examples
