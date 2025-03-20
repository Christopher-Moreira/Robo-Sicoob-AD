from python_imagesearch.imagesearch import imagesearch


imagem_referencia_erro = "Images/NoErrorPath/NoError.png"

# Verificar a tela

def NoErrorPath():
    pos = imagesearch(imagem_referencia_erro)   # Procura a imagem de referência
    if pos[0] != -1:
       return True
    else:
        print("Nenhum erro Registrado")