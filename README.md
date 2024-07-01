# PDF OCR Application (Python)

This Python application processes PDF files, extracts text using Tesseract OCR, and saves the result in new PDFs while preserving the original structure.

## Features

- **PDF Processing:** The application reads PDF files from a specific folder, applies OCR to each page using Tesseract, and generates new PDFs with the extracted text.
- **Preservation of Original Structure:** The generated PDFs maintain the original structure, preserving images and layout of the pages.
- **Removal of Processed Files:** After successful processing, the original files are automatically removed.

## Requirements

- **Python 3.6** or higher
- **Tesseract OCR:** Must be properly configured with the necessary language data files (e.g., `por.traineddata` for Portuguese).
- **PyMuPDF:** Used for PDF handling and page extraction.

## Installation and Setup

1. **Environment Setup:**
   - Ensure you have Python 3.6 or higher installed.
   - Download and set up Tesseract OCR with the required language data files (refer to the requirements section).

2. **Install Dependencies:**
   - Use pip to install the following libraries:
     ```
     pip install pytesseract
     pip install PyMuPDF
     ```

3. **Project Configuration:**
   - Clone or download the repository.
   - Configure the input folder path for PDF files in `pdf_ocr.py`:
     ```python
     input_folder = r'C:\Scan_in'
     ```
   - Configure the output folder path for processed PDFs in `pdf_ocr.py`:
     ```python
     output_folder = r'path\to\output\folder'
     ```

4. **Running the Application:**
   - Run the script. The application will process the PDF files in the specified input folder, apply OCR using Tesseract, and save the processed PDFs in the output folder.

## Usage Example

```python
# Example code snippet to start the processing
if __name__ == '__main__':
    input_folder = r'C:\Scan_in'
    output_folder = r'path\to\output\folder'

    process_pdf_folder(input_folder, output_folder)
