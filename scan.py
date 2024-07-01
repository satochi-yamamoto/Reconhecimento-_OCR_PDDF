import os
import fitz  # PyMuPDF
import pytesseract
from pdf2image import convert_from_path
from PIL import Image
from datetime import datetime

# Configurar o caminho do executável Tesseract
# Para Windows (ajuste conforme necessário)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Função para realizar OCR em todos os PDFs em uma pasta
def ocr_pdf_folder(input_folder, output_folder):
    # Verificar se a pasta de saída existe, caso contrário, criar
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    for file_name in os.listdir(input_folder):
        if file_name.endswith('.pdf'):
            input_path = os.path.join(input_folder, file_name)
            output_path = os.path.join(output_folder, file_name)
            
            # Verificar se o arquivo já existe na pasta de saída
            if os.path.exists(output_path):
                # Adicionar data e hora ao nome do arquivo
                timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
                base_name, ext = os.path.splitext(file_name)
                new_file_name = f"{base_name}_{timestamp}{ext}"
                output_path = os.path.join(output_folder, new_file_name)
            
            ocr_pdf(input_path, output_path)
            
            # Remover o arquivo original após o processamento
            os.remove(input_path)
            print(f"Arquivo processado e removido: {file_name}")

# Função para realizar OCR em um único PDF
def ocr_pdf(input_path, output_path):
    # Abrir o PDF
    pdf_document = fitz.open(input_path)
    pdf_writer = fitz.open()

    for page_num in range(len(pdf_document)):
        page = pdf_document.load_page(page_num)
        
        # Converter a página em imagem
        pix = page.get_pixmap()
        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)

        # Realizar OCR na imagem
        ocr_text = pytesseract.image_to_pdf_or_hocr(img, extension='pdf')

        # Criar uma nova página no PDF de saída
        new_page = pdf_writer.new_page(width=page.rect.width, height=page.rect.height)
        
        # Inserir o OCR no PDF
        new_page.show_pdf_page(page.rect, fitz.open("pdf", ocr_text), 0)

    # Salvar o PDF de saída
    pdf_writer.save(output_path)

# Definir as pastas de entrada e saída
input_folder = r'caminho\para\pasta\de\entrada'
output_folder = r'caminho\para\pasta\de\saída'

# Executar o OCR nos PDFs na pasta de entrada
ocr_pdf_folder(input_folder, output_folder)
