from python_imagesearch.imagesearch import imagesearch


imagem_referencia_erro = "image.png"

# Verificar a tela
pos = imagesearch(imagem_referencia_erro)  # Procura a imagem de referência
if pos[0] != -1:
    print("A tela corresponde à imagem de referência.")
else:
    print("A tela não corresponde à imagem de referência.")
