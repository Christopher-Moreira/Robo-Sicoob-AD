from python_imagesearch.imagesearch import imagesearch
import time

#PATHS
Caminho_NoErrorPath = "Images/NoErrorPath/NoError.png"
Caminho_ErrorRename = "Images/ErrorRename.png"
Caminho_ErrorAdCSV  = "Images/Erro_AD_ADcsv.png"



# Verificar a tela
def NoErrorPath():
    pos = imagesearch(Caminho_NoErrorPath)   # Procura a imagem de referência
    if pos[0] != -1:
       print("Nenhum erro Registrado - ErrorPath")
       return True
    else:
        print("Erro Registrado - ErrorPath")

def ErrorRename():
    pos = imagesearch(Caminho_ErrorRename)
    if pos[0] != -1:
        return True
    else:
        print("Nenhum erro Registrado - ErrorRename")

def ErrorAtualizar_ADcsv():
    pos = imagesearch(Caminho_ErrorAdCSV)
    if pos[0] != -1:
        return True
    else:
        print("Nenhum erro Registrado - ErrorAtualizar_ADcsv")