import pyautogui
import time
import pyperclip

from UsedFiles.RequestsDB.GetLogin import LoginPuxa
from UsedFiles.RequestsDB.GetSenha import SenhaPuxa


login = LoginPuxa()
senha = SenhaPuxa()

def acao(x, y, delay=1):
    time.sleep(delay)
    pyautogui.moveTo(x, y)
    pyautogui.click()

#Abre o navegador
acao(195, 1033, 2)
time.sleep(3)

#Clica na barra de pesquisa
time.sleep(5)
acao(1024, 88, 2)

#Copia
pyperclip.copy("https://sisbranalitico.sisbr.coop.br/sisbranalitico")

#Entra no Analitico
pyautogui.hotkey('ctrl', 'v')
time.sleep(1)
pyautogui.hotkey('enter')

#Clica em Login
acao(937, 434, 2)

#Cola Login
pyperclip.copy(login)
pyautogui.hotkey('ctrl', 'v')
time.sleep(1)
pyautogui.hotkey('tab')
#ColaSenha
pyperclip.copy(senha)
pyautogui.hotkey('ctrl', 'v')

#Loga
acao(950, 641, 2)
time.sleep(45)

#Favoritos
acao(318, 947, 2)
time.sleep(3)
pyautogui.scroll(-1000)

#Gera Relatorio
acao(425, 433, 2)
time.sleep(10)

#Executar como
acao(529, 451, 2)
time.sleep(10)

#Dados do Excel
acao(231, 742, 3)

#Salva Relatório
acao(1783, 915, 2)
time.sleep(120)

#acessa caminho
pyperclip.copy('R:\T.I\Relatorios BI\Arquivos de Origem\Cota')
pyautogui.hotkey('enter')

#nomeia file
time.sleep(2)
acao(406, 266, 3)


#salva
acao(754, 550, 2)
time.sleep(3)
acao(1026, 520, 3)


 #abre pasta de Origem
time.sleep(2)
pyautogui.moveTo(426,876)
pyautogui.click()
for _ in range(50):
        pyautogui.press('backspace')
time.sleep(3)
pyperclip.copy('R:\T.I\Relatorios BI\Relatorios.pbix')
pyautogui.hotkey('ctrl', 'v')
time.sleep(2)
pyautogui.press('enter')

#Atualizar
acao(927, 117, 2)

time.sleep(45)

#publicar
acao(1600,113, 2)
time.sleep(3)
#salvar
acao(1050, 568, 2)
time.sleep(10)

#Publicar 2
acao(700, 488, 2)
time.sleep(3)

#Selecionar 
acao(1112, 742, 2)
time.sleep(15)

#Subistituir
acao(1025, 684, 3)

#Fechar BI
acao(1891, 20, 2)
