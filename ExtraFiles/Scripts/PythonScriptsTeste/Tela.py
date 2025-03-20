import time
from python_imagesearch.imagesearch import imagesearch

# Função para verificar constantemente a tela
def monitorar_tela_erro():
    while True:
        pos = imagesearch("Images/Erro_Cobraca_Administrativa_Salvar_Relatorio.png")  
        if pos[0] != -1:
            print(f"Imagem encontrada nas coordenadas: {pos}")
        else:
            print("Imagem não encontrada.")
        
        time.sleep(1)

# Inicia o monitoramento
monitorar_tela_erro()