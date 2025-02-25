import cv2
import numpy as np
import pyautogui
import os

def capturar_tela():
    screenshot = pyautogui.screenshot()
    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
    return screenshot

def comparar_imagens(img1, img2):
    # Converter para escala de cinza
    img1_gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    img2_gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

    # Calcular a diferença absoluta entre as duas imagens
    diff = cv2.absdiff(img1_gray, img2_gray)

    # Calcular a média da diferença
    media_diff = np.mean(diff)
    
    return media_diff

def main():
    # Capturar a tela
    tela = capturar_tela()

    # Obter o caminho do diretório onde o script está localizado
    diretorio_script = os.path.dirname(os.path.abspath(__file__))

    # Carregar a imagem de referência (screenshot) do mesmo diretório
    img_ref_path = os.path.join(diretorio_script, 'sua_imagem_de_referencia.png')
    img_ref = cv2.imread(img_ref_path)

    if img_ref is None:
        print("Erro ao carregar a imagem de referência.")
        return

    # Comparar as imagens
    similaridade = comparar_imagens(tela, img_ref)

    print(f"A média da diferença entre as imagens é: {similaridade:.2f}")

if __name__ == "__main__":
    main()
