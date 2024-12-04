import os
import fitz  # PyMuPDF
import pytesseract
from pdf2image import convert_from_path
from PIL import Image
from datetime import datetime

# Configuração do caminho do executável Tesseract no Linux
pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'

def ocr_pdf_folder(input_folder, output_folder):
    """
    Processa todos os PDFs na pasta de entrada, aplica OCR e salva na pasta de saída.
    """
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    for file_name in os.listdir(input_folder):
        if file_name.endswith('.pdf'):
            input_path = os.path.join(input_folder, file_name)
            output_path = os.path.join(output_folder, file_name)
            
            # Renomeia o arquivo se já existir na pasta de saída
            if os.path.exists(output_path):
                timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
                base_name, ext = os.path.splitext(file_name)
                new_file_name = f"{base_name}_{timestamp}{ext}"
                output_path = os.path.join(output_folder, new_file_name)
            
            ocr_pdf(input_path, output_path)
            os.remove(input_path)
            print(f"Arquivo processado e removido: {file_name}")

def ocr_pdf(input_path, output_path):
    """
    Realiza OCR em um único PDF e salva o resultado.
    """
    pdf_document = fitz.open(input_path)
    pdf_writer = fitz.open()

    for page_num in range(len(pdf_document)):
        page = pdf_document[page_num]
        pix = page.get_pixmap()
        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
        ocr_text = pytesseract.image_to_pdf_or_hocr(img, extension='pdf')
        new_page = pdf_writer.new_page(width=page.rect.width, height=page.rect.height)
        new_page.show_pdf_page(page.rect, fitz.open("pdf", ocr_text), 0)

    pdf_writer.save(output_path)

if __name__ == "__main__":
    # Configure as pastas de entrada e saída
    input_folder = r'/home/ubuntu/Scan_in'
    output_folder = r'/home/ubuntu/Scan_out'
    ocr_pdf_folder(input_folder, output_folder)
