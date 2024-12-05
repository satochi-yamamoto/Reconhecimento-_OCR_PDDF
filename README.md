# PDF OCR Application

Esta aplicação em Python foi desenvolvida para processar arquivos PDF, aplicar OCR (Reconhecimento Óptico de Caracteres) utilizando Tesseract e salvar o resultado em novos PDFs mantendo a estrutura original. O script está otimizado para rodar em sistemas Linux, como o Ubuntu 24.02.

## Funcionalidades

- **Processamento Automático de PDFs:**
  - Lê arquivos PDF de uma pasta especificada (`Scan_in`).
  - Aplica OCR em cada página utilizando o Tesseract.
  - Gera novos PDFs com o texto extraído e mantém a estrutura original.
- **Evita Conflitos de Nomes:**
  - Arquivos com nomes duplicados na pasta de saída são renomeados automaticamente com um timestamp.
- **Gerenciamento Automático:**
  - Remove os arquivos processados da pasta de entrada (`Scan_in`) após o sucesso do processamento.

---

## Requisitos

1. **Sistema Operacional:**
   - Ubuntu 24.02 ou superior.
   
2. **Dependências do Sistema:**
   - **Tesseract OCR** com o idioma `Português (por)` instalado.
   - **Poppler-utils** para manipulação de PDFs.

3. **Dependências Python:**
   - Python 3.6 ou superior.
   - Bibliotecas: `PyMuPDF`, `pytesseract`, `pdf2image`, `Pillow`.

---

## Instalação

### 1. Configurar o Ambiente Linux

Execute os seguintes comandos para instalar as dependências do sistema:

```bash
sudo apt update
sudo apt install -y tesseract-ocr libtesseract-dev poppler-utils python3-pip
