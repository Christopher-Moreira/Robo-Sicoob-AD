import pyautogui
import pyperclip
import time
from Datas import DataHoje, DataReduzidaFinsDeSemana, DataHojeMenosUm, DataHojeMenusDois, DataMenosSeis, DatahojeComTraco, obter_hora_atual
from RequestsDB.getLogin import LoginPuxa
from RequestsDB.getSenha import SenhaPuxa
 
login = LoginPuxa()
senha = SenhaPuxa()

hora = obter_hora_atual()

dataFinsDeSemana = DataReduzidaFinsDeSemana()

dataHoje = DataHoje()

dataMenusUm = DataHojeMenosUm()

dataHojeMenusDois = DataHojeMenusDois()

dataSeisDias = DataMenosSeis()

DataTraco = DatahojeComTraco()

time.sleep(5)
#data referencia
pyautogui.moveTo(501,214)


#time.sleep(2)
pyautogui.doubleClick()

#abre o Excel
pyautogui.doubleClick()

#espera o Excel abrir
time.sleep(30)

#Clica para baixo para selecionar celula de baixo
pyautogui.hotkey('Down')

#escreve data de referencia (Data reduzida de acordo com o dia da semana)
pyperclip.copy(dataFinsDeSemana)
pyautogui.hotkey('ctrl', 'v')

#Vai para celula do lado
pyautogui.hotkey('Left')

#escreve data de hoje
pyperclip.copy(dataHoje)
pyautogui.hotkey('ctrl', 'v')


#Fecha o Excel
time.sleep(3)
acao(1889,26,2)


#Salva
acao(937,918,2)
time.sleep(20)

