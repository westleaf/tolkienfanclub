#!/bin/bash
# Build the site for production for GitHub Pages
echo "Building site for GitHub Pages..."
python3 src/main.py "/tolkienfanclub/"
echo "Build complete. Output in ./docs"
