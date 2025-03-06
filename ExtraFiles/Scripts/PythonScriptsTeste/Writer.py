import pyautogui
import time
from DataTeste import DataReduzidaDiasEspecificos
from datetime import datetime

def DataAtual():
    data_atual = datetime.now()
    return data_atual.strftime("%d/%m/%Y")

if __name__ == "__main__":

    data_atual = DataAtual()
    data_teste = data_atual

    data_especifica = DataReduzidaDiasEspecificos(data_teste)

    resultadoTeste = f"Data de teste: {data_teste}\nData reduzida conforme dia da semana: {data_especifica}"
    resultado = f"{data_especifica}"


try:
  while True:
        #Click Chrome
        pyautogui.moveTo(215, 1049)
        pyautogui.click()

        time.sleep(1)
        
        #Click Button
        pyautogui.moveTo(480, 180)
        pyautogui.click()

        pyautogui.write(resultado, interval=0)

        time.sleep(3)

except KeyboardInterrupt:
    print("interrompido")
    
