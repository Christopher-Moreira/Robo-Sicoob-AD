import pyautogui
import pyperclip
import time
from UsedFiles.GetDatas import DataHoje, DataReduzidaFinsDeSemana, DataHojeMenosUm, DataHojeMenusDois, DataMenosSeis, DatahojeComTraco, obter_hora_atual
from UsedFiles.RequestsDB.getLogin import LoginPuxa
from UsedFiles.RequestsDB.getSenha import SenhaPuxa
 
login = LoginPuxa()
senha = SenhaPuxa()

hora = obter_hora_atual()

dataFinsDeSemana = DataReduzidaFinsDeSemana()

dataHoje = DataHoje()

dataMenusUm = DataHojeMenosUm()

dataHojeMenusDois = DataHojeMenusDois()

dataSeisDias = DataMenosSeis()

DataTraco = DatahojeComTraco()

time.sleep(3)
pyperclip.copy(f"Confirmado, AD publicado às {hora}, sem erros registrados.")
pyautogui.hotkey('ctrl', 'v')

