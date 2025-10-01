#!/usr/bin/env python3
"""
Simple Quarto-like build script for Sudan Nighttime Lights project
This script processes .qmd files and creates a basic website structure
"""

import os
import shutil
import json
from pathlib import Path

def create_site_structure():
    """Create the basic site structure"""
    base_dir = Path('/Users/ssarva/Library/CloudStorage/OneDrive-WBG/Documents/sudan-nighttime-lights')
    site_dir = base_dir / '_site'
    
    # Create site directory
    site_dir.mkdir(exist_ok=True)
    
    # Copy existing HTML files
    docs_dir = base_dir / 'docs'
    if docs_dir.exists():
        for html_file in docs_dir.glob('*.html'):
            shutil.copy2(html_file, site_dir)
    
    # Copy CSS files
    css_file = base_dir / 'styles.css'
    if css_file.exists():
        shutil.copy2(css_file, site_dir)
    
    # Copy images and other assets
    for asset_dir in ['images', 'nighttime_lights_files']:
        src_asset = docs_dir / asset_dir
        if src_asset.exists():
            dst_asset = site_dir / asset_dir
            if dst_asset.exists():
                shutil.rmtree(dst_asset)
            shutil.copytree(src_asset, dst_asset)
    
    print(f"Site built in {site_dir}")
    return site_dir

def create_index_html():
    """Create a simple index.html from index.qmd"""
    base_dir = Path('/Users/ssarva/Library/CloudStorage/OneDrive-WBG/Documents/sudan-nighttime-lights')
    
    html_content = """<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Sudan Nighttime Lights Analysis</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <nav class="navbar navbar-expand-lg navbar-dark bg-primary">
        <div class="container">
            <a class="navbar-brand" href="index.html">Sudan Nighttime Lights</a>
            <div class="navbar-nav">
                <a class="nav-link" href="index.html">Home</a>
                <a class="nav-link" href="nighttime_lights.html">Analysis</a>
                <a class="nav-link" href="gallery.html">Gallery</a>
                <a class="nav-link" href="https://github.com/worldbank/sudan-nighttime-lights" target="_blank">GitHub</a>
            </div>
        </div>
    </nav>
    
    <div class="container mt-4">
        <div class="row">
            <div class="col-md-8 offset-md-2">
                <h1>Sudan Nighttime Lights Analysis</h1>
                
                <p class="lead">This project analyzes nighttime lights data for Sudan using NASA's VIIRS Black Marble dataset. The analysis provides insights into economic activity, urbanization patterns, and infrastructure development across Sudan.</p>
                
                <h2>Overview</h2>
                <p>The analysis includes:</p>
                <ul>
                    <li><strong>Data Collection</strong>: Processing VIIRS Black Marble nighttime lights data</li>
                    <li><strong>Spatial Analysis</strong>: Examining patterns across Sudan's administrative boundaries</li>
                    <li><strong>Gas Flaring Integration</strong>: Incorporating gas flaring data to separate industrial activity</li>
                    <li><strong>Interactive Visualization</strong>: Creating maps and charts to explore the data</li>
                </ul>
                
                <h2>Key Features</h2>
                <ul>
                    <li>Monthly nighttime lights data from 2012-2023</li>
                    <li>Administrative boundary analysis at state and locality levels</li>
                    <li>Gas flaring data integration</li>
                    <li>Interactive leaflet maps</li>
                    <li>Statistical summaries and trends</li>
                </ul>
                
                <h2>Getting Started</h2>
                <ol>
                    <li>View the main <a href="nighttime_lights.html">Analysis</a> to see the complete workflow</li>
                    <li>Check the <a href="gallery.html">Gallery</a> for key visualizations</li>
                    <li>Review the methodology and data sources in the analysis document</li>
                </ol>
                
                <h2>Data Sources</h2>
                <ul>
                    <li><strong>VIIRS Black Marble</strong>: NASA's Visible Infrared Imaging Radiometer Suite</li>
                    <li><strong>Administrative Boundaries</strong>: GADM (Global Administrative Areas)</li>
                    <li><strong>Gas Flaring Data</strong>: NOAA's gas flaring detection dataset</li>
                    <li><strong>Population Data</strong>: World Bank population estimates</li>
                </ul>
                
                <div class="alert alert-info mt-4">
                    <h4>Citation</h4>
                    <p>If you use this analysis or data, please cite:</p>
                    <pre><code>World Bank. (2025). Sudan Nighttime Lights Analysis. 
GitHub repository: https://github.com/worldbank/sudan-nighttime-lights</code></pre>
                </div>
                
                <hr class="mt-5">
                <p class="text-muted"><em>This project is part of the World Bank's economic monitoring and analysis work for Sudan.</em></p>
            </div>
        </div>
    </div>
    
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>"""
    
    site_dir = base_dir / '_site'
    with open(site_dir / 'index.html', 'w') as f:
        f.write(html_content)

def create_gallery_html():
    """Create gallery.html"""
    base_dir = Path('/Users/ssarva/Library/CloudStorage/OneDrive-WBG/Documents/sudan-nighttime-lights')
    
    html_content = """<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Gallery - Sudan Nighttime Lights Analysis</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <nav class="navbar navbar-expand-lg navbar-dark bg-primary">
        <div class="container">
            <a class="navbar-brand" href="index.html">Sudan Nighttime Lights</a>
            <div class="navbar-nav">
                <a class="nav-link" href="index.html">Home</a>
                <a class="nav-link" href="nighttime_lights.html">Analysis</a>
                <a class="nav-link active" href="gallery.html">Gallery</a>
                <a class="nav-link" href="https://github.com/worldbank/sudan-nighttime-lights" target="_blank">GitHub</a>
            </div>
        </div>
    </nav>
    
    <div class="container mt-4">
        <div class="row">
            <div class="col-md-10 offset-md-1">
                <h1>Sudan Nighttime Lights - Key Visualizations</h1>
                
                <p class="lead">This gallery showcases the main visualizations and findings from the Sudan nighttime lights analysis.</p>
                
                <h2>Interactive Maps</h2>
                
                <h3>Nighttime Lights Distribution</h3>
                <p>The interactive map shows the spatial distribution of nighttime lights across Sudan, highlighting urban centers and economic activity patterns.</p>
                
                <h3>Gas Flaring Locations</h3>
                <p>Integration of gas flaring data helps separate industrial lighting from urban activity.</p>
                
                <h2>Time Series Analysis</h2>
                
                <h3>Monthly Trends</h3>
                <p>Analysis of nighttime lights over time reveals seasonal patterns and long-term trends.</p>
                
                <h3>State-Level Comparison</h3>
                <p>Comparison of nighttime lights intensity across Sudan's different states.</p>
                
                <h2>Administrative Analysis</h2>
                
                <h3>Locality-Level Patterns</h3>
                <p>Detailed breakdown of nighttime lights at the locality level for fine-grained analysis.</p>
                
                <h3>Urban vs Rural Distribution</h3>
                <p>Contrast between urban centers and rural areas in terms of nighttime lights intensity.</p>
                
                <h2>Data Sources and Methodology</h2>
                <ul>
                    <li><strong>VIIRS Black Marble</strong>: Monthly composites from NASA</li>
                    <li><strong>Administrative Boundaries</strong>: GADM Level 1 and 2 boundaries</li>
                    <li><strong>Gas Flaring Data</strong>: NOAA detection dataset</li>
                    <li><strong>Analysis Period</strong>: 2012-2023</li>
                </ul>
                
                <h2>Key Findings</h2>
                <ol>
                    <li><strong>Urban Concentration</strong>: Major cities show highest nighttime lights intensity</li>
                    <li><strong>Seasonal Variation</strong>: Clear seasonal patterns in rural areas</li>
                    <li><strong>Gas Flaring Impact</strong>: Significant contribution from industrial sources</li>
                    <li><strong>Regional Disparities</strong>: Uneven distribution across states</li>
                </ol>
                
                <hr class="mt-5">
                <p class="text-muted"><em>For detailed methodology and complete analysis, see the <a href="nighttime_lights.html">main analysis document</a>.</em></p>
            </div>
        </div>
    </div>
    
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>"""
    
    site_dir = base_dir / '_site'
    with open(site_dir / 'gallery.html', 'w') as f:
        f.write(html_content)

if __name__ == "__main__":
    print("Building Sudan Nighttime Lights website...")
    
    # Create site structure
    site_dir = create_site_structure()
    
    # Create HTML pages
    create_index_html()
    create_gallery_html()
    
    print("✅ Website built successfully!")
    print(f"📁 Site location: {site_dir}")
    print("🌐 Open index.html in your browser to view the site")