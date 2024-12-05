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

```

### 2. Instalar o Idioma Português no Tesseract

Certifique-se de que o idioma Português está instalado:

```bash

sudo apt install -y tesseract-ocr-por
```

### 3. Configurar o Ambiente Virtual Python
Crie e ative um ambiente virtual:

```bash
python3 -m venv venv
source venv/bin/activate
```

Instale as dependências Python necessárias:

```bash
pip install PyMuPDF pytesseract pdf2image Pillow
```

## Estrutura do Projeto

Organize os diretórios e arquivos do projeto da seguinte forma:
```bash
OCR-Application/
├── process_pdfs.py    # Script principal da aplicação
├── Scan_in/           # Pasta de entrada para os arquivos PDF
├── Scan_out/          # Pasta de saída para os arquivos processados
├── venv/              # Ambiente virtual Python
└── README.md          # Instruções do projeto
```
## Configuração

### 1. Configurar Pastas de Entrada e Saída:

Atualize as variáveis input_folder e output_folder no arquivo process_pdfs.py:

```bash
input_folder = r'/home/ubuntu/Scan_in'
output_folder = r'/home/ubuntu/Scan_out'
```

### 2. Configurar o Caminho do Tesseract:

Certifique-se de que o caminho do executável Tesseract está configurado no script:
```bash
pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'
```

## Uso

### 1. Adicione os arquivos PDF que deseja processar na pasta Scan_in.
### 2. Execute o script principal

```bash
python process_pdfs.py
```

### 3. Os PDFs processados com OCR serão salvos na pasta Scan_out. Os arquivos originais serão automaticamente removidos.

## Logs e Depuração
### Durante a execução, o script exibe mensagens no terminal indicando quais arquivos estão sendo processados e quais foram removidos.
### Para verificar erros ou problemas, certifique-se de que:
### O caminho para o Tesseract está correto.
### Os arquivos de idioma estão instalados (por.traineddata).
### Você tem permissões de leitura e gravação nas pastas de entrada e saída.


## Contribuições

### Contribuições são bem-vindas! Caso encontre problemas ou tenha sugestões de melhoria, sinta-se à vontade para abrir uma issue ou enviar um pull request.
