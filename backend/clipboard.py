import os
from PIL import Image
import io
import win32clipboard

def imageToClipboard(folder_path):
    # Lista todos os arquivos da pasta
    files = os.listdir(folder_path)

    # Filtra apenas arquivos de imagem
    images = [f for f in files]

    if not images:
        print("Nenhuma imagem encontrada na pasta!")
        return

    # Pega a primeira imagem da lista
    image_path = os.path.join(folder_path, images[0])

    # Abre e converte para BMP/DIB
    img = Image.open(image_path)
    output = io.BytesIO()
    img.convert("RGB").save(output, "BMP")
    data = output.getvalue()[14:]
    output.close()

    # Copia para a área de transferência
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardData(win32clipboard.CF_DIB, data)
    win32clipboard.CloseClipboard()

    print(f"Imagem '{images[0]}' copiada para a área de transferência!")
