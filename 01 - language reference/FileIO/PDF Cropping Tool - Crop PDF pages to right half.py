"""PDF Cropping Tool - Crop PDF pages to right half.

This script opens a PDF file and crops all pages to show only the right half.
Useful for splitting double-page layouts or removing left margins.

Requirements:
    pip install pymupdf

Usage:
    Update input_file and output_file paths, then run:
    python PDF_cut.py
"""

import fitz  # Package name: pymupdf (pip install pymupdf)
import sys
from pathlib import Path

# Raw strings for Windows paths (or use forward slashes)
input_file = r".\halle_21_2_original.pdf"
output_file = r".\halle_21_2_cut.pdf"


def crop_pdf_to_right_half(input_path: str, output_path: str) -> None:
    """Crop all pages in a PDF to show only the right half.
    
    Args:
        input_path: Path to the input PDF file
        output_path: Path where the cropped PDF will be saved
    
    Raises:
        FileNotFoundError: If input file doesn't exist
        RuntimeError: If PDF processing fails
    """
    # Validate input file exists
    if not Path(input_path).exists():
        raise FileNotFoundError(f"Input file not found: {input_path}")
    
    try:
        doc = fitz.open(input_path)
        
        for page in doc:
            # Get the full page dimensions
            rect = page.rect
            
            # Define the crop area (right half):
            # - Start X: half of the page width (middle)
            # - Start Y: 0 (top)
            # - End X: full width (right edge)
            # - End Y: full height (bottom)
            crop_area = fitz.Rect(rect.width / 2, 0, rect.width, rect.height)
            
            # Apply the crop box to the page
            page.set_cropbox(crop_area)
        
        # Save the modified PDF
        doc.save(output_path)
        doc.close()
        
        print(f"✓ Success! Cropped PDF saved as: {output_path}")
        print(f"  Pages processed: {len(doc)}")
        
    except Exception as e:
        raise RuntimeError(f"Failed to process PDF: {e}") from e


if __name__ == "__main__":
    try:
        crop_pdf_to_right_half(input_file, output_file)
    except FileNotFoundError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except RuntimeError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(2)