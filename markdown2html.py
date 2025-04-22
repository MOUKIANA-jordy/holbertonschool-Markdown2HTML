#!/usr/bin/env python3
"""Markdown to HTML conversion script"""

import sys
import os

if __name__ == "__main__":
    # Check for the correct number of arguments
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # Check if input file exists
    if not os.path.isfile(input_file):
        print(f"Missing {input_file}", file=sys.stderr)
        exit(1)

    # Read from Markdown and write to HTML
    try:
        with open(input_file, 'r') as md_file:
            content = md_file.read()

        # For now, this script just copies text. Actual parsing comes in next tasks.
        with open(output_file, 'w') as html_file:
            html_file.write(content)

        exit(0)

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        exit(1)

