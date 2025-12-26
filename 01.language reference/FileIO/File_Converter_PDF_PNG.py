"""PDF to PNG Converter.

This script converts all pages of a PDF file into separate PNG image files.
Each page is saved as a high-quality PNG image with a sequential filename.

Requirements:
    pip install pymupdf

Usage:
    Update input_file and output_folder paths, then run:
    python File_Converter_PDF_PNG.py
"""

import fitz  # PyMuPDF
import sys
from pathlib import Path


def convert_pdf_to_png(
    input_path: str,
    output_folder: str,
    dpi: int = 300,
    prefix: str = "page"
) -> None:
    """Convert all pages of a PDF to PNG images.
    
    Args:
        input_path: Path to the input PDF file
        output_folder: Directory where PNG files will be saved
        dpi: Resolution in dots per inch (default: 300 for high quality)
        prefix: Prefix for output filenames (default: "page")
    
    Raises:
        FileNotFoundError: If input file doesn't exist
        RuntimeError: If PDF processing fails
    """
    # Validate input file exists
    input_file = Path(input_path)
    if not input_file.exists():
        raise FileNotFoundError(f"Input file not found: {input_path}")
    
    # Create output folder if it doesn't exist
    output_dir = Path(output_folder)
    output_dir.mkdir(parents=True, exist_ok=True)
    
    try:
        # Open the PDF
        doc = fitz.open(input_path)
        
        if len(doc) == 0:
            raise RuntimeError("The PDF has no pages")
        
        print(f"Converting PDF: {input_file.name}")
        print(f"Total pages: {len(doc)}")
        print(f"Output folder: {output_dir}")
        print(f"Resolution: {dpi} DPI\n")
        
        # Calculate zoom factor for desired DPI (72 is default PDF DPI)
        zoom = dpi / 72
        mat = fitz.Matrix(zoom, zoom)
        
        # Convert each page
        for page_num in range(len(doc)):
            page = doc[page_num]
            
            # Render page to a pixmap (raster image)
            pix = page.get_pixmap(matrix=mat)
            
            # Generate output filename: page_001.png, page_002.png, etc.
            output_file = output_dir / f"{prefix}_{page_num + 1:03d}.png"
            
            # Save as PNG
            pix.save(output_file)
            
            print(f"  ✓ Page {page_num + 1}/{len(doc)} → {output_file.name}")
        
        doc.close()
        
        print(f"\n✓ Success! {len(doc)} pages converted to PNG")
        
    except Exception as e:
        raise RuntimeError(f"Failed to convert PDF: {e}") from e


if __name__ == "__main__":
    # Configuration - Update these paths
    input_file = r"C:\Users\Falk\OneDrive\Desktop\Ausleuchtung\Hallenpläne\Hallen\Halle 22_cropped_first_page.pdf"
    output_folder = r"C:\Users\Falk\OneDrive\Desktop\Ausleuchtung\Hallenpläne\pdf_2_png_output"
    
    # Optional: Change DPI (higher = better quality but larger files)
    # 150 = screen quality, 300 = print quality, 600 = high resolution
    dpi_setting = 300
    
    try:
        convert_pdf_to_png(input_file, output_folder, dpi=dpi_setting)
    except FileNotFoundError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except RuntimeError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(2)
