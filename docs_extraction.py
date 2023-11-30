from docx import Document
import os

def extract_non_alphabetic_from_docx(docx_path):
    doc = Document(docx_path)
    non_alphabetic_text = []

    for paragraph in doc.paragraphs:
        for char in paragraph.text:
            if not char.isalpha():
                if char == '+':
                    non_alphabetic_text.append('\n')
                else:
                    non_alphabetic_text.append(char)

    return ''.join(non_alphabetic_text)

# Pasta contendo os arquivos .docx
pasta_documentos = r'C:\Users\voice\Downloads\a'

# Loop através de todos os arquivos .docx na pasta
for arquivo in os.listdir(pasta_documentos):
    if arquivo.endswith('.docx'):
        caminho_arquivo = os.path.join(pasta_documentos, arquivo)

        # Extrair caracteres não alfabéticos do arquivo .docx
        non_alphabetic_text = extract_non_alphabetic_from_docx(caminho_arquivo)

        # Escrever caracteres não alfabéticos em um novo arquivo .txt com codificação 'utf-8'
        caminho_novo_arquivo = os.path.join(pasta_documentos, 'non_alphabetic_output_' + os.path.splitext(arquivo)[0] + '.txt')
        with open(caminho_novo_arquivo, 'w', encoding='utf-8') as output_file:
            output_file.write(non_alphabetic_text)
