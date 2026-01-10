"""Setup script for Ghost Office Hunter."""
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="ghost-office-hunter",
    version="1.0.0",
    author="Ghost Office Hunter Team",
    description="AI-powered compliance investigation tool for detecting ghost offices and shell companies",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/your-username/ghost-office-hunter",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Financial and Insurance Industry",
        "Topic :: Office/Business :: Financial",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.12",
    ],
    python_requires=">=3.12",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "ghost-hunter=main:main",
        ],
    },
)
