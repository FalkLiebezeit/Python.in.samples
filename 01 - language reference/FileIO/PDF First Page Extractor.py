"""PDF First Page Extractor.

This script extracts the first page from a PDF file and saves it as a new PDF.
Useful for creating samples, extracting covers, or splitting documents.

Requirements:
    pip install pymupdf

Usage:
    Update input_file and output_file paths, then run:
    python PDF_page1_save.py
"""

import fitz  # PyMuPDF
import sys
from pathlib import Path

# Raw strings for Windows paths (or use forward slashes)
input_file = r".\halle_21_2_original.pdf"
output_file = r".\halle_21_2_cut.pdf"


def extract_first_page(input_path: str, output_path: str) -> None:
    """Extract the first page from a PDF and save it as a new PDF file.
    
    Args:
        input_path: Path to the input PDF file
        output_path: Path where the single-page PDF will be saved
    
    Raises:
        FileNotFoundError: If input file doesn't exist
        RuntimeError: If PDF processing fails
    """
    # Validate input file exists
    if not Path(input_path).exists():
        raise FileNotFoundError(f"Input file not found: {input_path}")
    
    try:
        # Open the original PDF
        doc = fitz.open(input_path)
        
        if len(doc) == 0:
            raise RuntimeError("The input PDF has no pages")
        
        # Create a new empty PDF
        new_doc = fitz.open()
        
        # Insert only the first page (index 0) from the original into the new PDF
        # from_page=0 and to_page=0 means: start at page 1, end at page 1
        new_doc.insert_pdf(doc, from_page=0, to_page=0)
        
        # Save the new PDF
        new_doc.save(output_path)
        
        print(f"✓ Success! First page extracted and saved as: {output_path}")
        print(f"  Original PDF: {len(doc)} pages")
        
        # Close files
        doc.close()
        new_doc.close()
        
    except Exception as e:
        raise RuntimeError(f"Failed to extract page: {e}") from e


if __name__ == "__main__":
    try:
        extract_first_page(input_file, output_file)
    except FileNotFoundError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except RuntimeError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(2)