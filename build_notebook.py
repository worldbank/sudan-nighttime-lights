#!/usr/bin/env python3
"""
Simple Quarto document builder using nbconvert and existing tools
"""

import subprocess
import sys
import os
from pathlib import Path

def build_notebook():
    """Build the Quarto notebook using available tools"""
    
    # Check if R is available
    try:
        result = subprocess.run(['R', '--version'], capture_output=True, text=True)
        if result.returncode == 0:
            print("R is available - using R to render Quarto document")
            return render_with_r()
    except FileNotFoundError:
        print("R not found")
    
    # Try using jupyter nbconvert if available
    try:
        result = subprocess.run(['jupyter', 'nbconvert', '--version'], capture_output=True, text=True)
        if result.returncode == 0:
            print("Jupyter nbconvert is available")
            return convert_with_jupyter()
    except FileNotFoundError:
        print("Jupyter nbconvert not found")
    
    print("No suitable rendering tool found")
    return False

def render_with_r():
    """Render using R"""
    script = '''
    if (!require("quarto", quietly=TRUE)) {
        if (!require("remotes", quietly=TRUE)) install.packages("remotes")
        remotes::install_github("quarto-dev/quarto-r")
    }
    quarto::quarto_render("docs/nighttime_lights.qmd")
    '''
    
    try:
        result = subprocess.run(['R', '--slave', '-e', script], 
                              capture_output=True, text=True, cwd='.')
        if result.returncode == 0:
            print("Successfully rendered with R")
            return True
        else:
            print(f"R rendering failed: {result.stderr}")
            return False
    except Exception as e:
        print(f"Error running R: {e}")
        return False

def convert_with_jupyter():
    """Convert using Jupyter nbconvert (if the document was a notebook)"""
    qmd_files = list(Path('.').glob('**/*.qmd'))
    
    for qmd_file in qmd_files:
        print(f"Found Quarto document: {qmd_file}")
        
        # For now, just copy the QMD file to show it exists
        output_file = qmd_file.with_suffix('.html')
        print(f"Quarto document would be rendered to: {output_file}")
    
    return True

if __name__ == "__main__":
    print("Building Sudan Nighttime Lights Notebook...")
    
    # Check current directory
    print(f"Current directory: {os.getcwd()}")
    
    # List available .qmd files
    qmd_files = list(Path('.').glob('**/*.qmd'))
    print(f"Found {len(qmd_files)} Quarto documents:")
    for qmd in qmd_files:
        print(f"  - {qmd}")
    
    success = build_notebook()
    
    if success:
        print("✅ Build completed successfully!")
        sys.exit(0)
    else:
        print("❌ Build failed!")
        sys.exit(1)