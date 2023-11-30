from PIL import Image
import pytesseract
import os

pytesseract.pytesseract.tesseract_cmd = r'C:\Tesseract-OCR\tesseract.exe'

os.environ['TESSDATA_PREFIX'] = r'C:\Tesseract-OCR\tessdata'

def extrairTexto(caminho_imagem):
    imagem = Image.open(caminho_imagem)
    texto = pytesseract.image_to_string(imagem, config='--psm 6') 
    return texto

def extrairImagensPasta(caminho_pasta):
    textos = []
    for arquivo in os.listdir(caminho_pasta):
        caminho_imagem = os.path.join(caminho_pasta, arquivo)
        if os.path.isfile(caminho_imagem) and arquivo.lower().endswith(('.png', '.jpg', '.jpeg')):
            texto = extrairTexto(caminho_imagem)
            print(f'Imagem: {caminho_imagem}\nTexto Extraído: {texto}\n')
            textos.append(texto)

    return textos

def salvarTXT(textos, nome_arquivo='textos_extraidos.txt'):
    with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
        for texto in textos:
            arquivo.write(f'Texto Extraído: {texto}\n\n')
    print(f'Texto extraído de: {nome_arquivo}')

caminho_da_sua_pasta = r'C:\folder'
textos_extraidos = extrairImagensPasta(caminho_da_sua_pasta)
salvarTXT(textos_extraidos)
