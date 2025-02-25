import pyautogui
import pyperclip
import time
from Datas import DataHoje, DataReduzidaFinsDeSemana, DataHojeMenosUm, DataHojeMenusDois, DataMenosSeis, DatahojeComTraco, obter_hora_atual

hora = obter_hora_atual()

data = DataReduzidaFinsDeSemana()

dataHoje = DataHoje()

dataMenusUm = DataHojeMenosUm()

dataHojeMenusDois = DataHojeMenusDois()

dataSeisDias = DataMenosSeis()

DataTraco = DatahojeComTraco()



def acao(x, y, delay=1):
    time.sleep(delay)
    pyautogui.moveTo(x, y)
    pyautogui.click()

# Clicar 
acao(300, 1053)

# Clicar na barra de pesquisa
acao(197, 968)

# Esperar segundos
time.sleep(3)

# Digitar 'Conta Corrente'
pyautogui.write("Conta Corrente")

# Esperar para clicar em 'Conta Corrente'
acao(104, 279, 3)

# Clicar nos relatórios
acao(484, 126, 3)

# Clicar em relatório saldos
time.sleep(2)
acao(591,332,3)

# Clicar em saldos
acao(858, 335, 3)

# Clicar no devedor
acao(700, 508, 3)

# Clicar no ok
acao(961, 736, 1)

# Clicar na barra
acao(1111, 520, 1)

# Clicar em csv
acao(943, 639, 1)

# Clicar no imprimir
acao(925, 575, 1)

# Clicar em Saldo Fechado
acao(1028, 511, 1)

# Clicar no ok
acao(961, 736, 1)

# Clicar na barra
acao(1111, 520, 1)

# Clicar em csv
acao(943, 639, 1)

# Clicar no imprimir
acao(925, 575, 1)

# Clicar no fechar
acao(1187, 732, 1)

# Fechar o Conta Corrente
acao(1886, 11, 1)

#Clicar na barra de Pesqusia
acao(197, 968)

#Cobrança Administrativa
for _ in range(22):
    pyautogui.press('backspace')

time.sleep(1)
pyautogui.write("Cobranca Administrativa")

#Clicar na Cobrança
acao(104, 279, 2)

time.sleep(5)
#Clicar em Relatorios
acao(278,127,5)

#Clicar em Fichas de Cobrança
acao(334,314,2)

#Data de Vencimento da operação
acao(640,589,2)

#>>>
acao(937,494,2)

#Proximo
acao(1018,727,2)

#Clica Data
acao(731,388,2)
for _ in range(6):
    pyautogui.press('backspace')
time.sleep(3)
pyautogui.write(dataSeisDias, 0.25)

#Data Menos Seis Dias
acao(899, 389, 2)
for i in range(6):
    pyautogui.press('backspace')
time.sleep(3)
pyautogui.write(dataSeisDias, 0.25)

#Vizualizar
acao(1014,489,2)

#Selecionar CSV
acao(1111,520,2)

#CSV
acao(819,635,2)

#Imprimir
acao(950,572,2)

#Fechar
acao(1420,296,2)

#Relatorios
acao(1851,127,2)

#Imprimir File 1
acao(1221, 545, 2)


#Processo para Salvar arquivo
#ScrollDown
time.sleep(3)
pyautogui.moveTo(250,264)
time.sleep(2)
pyautogui.scroll(-500)

#Clica em SicoobCruzAlta
time.sleep(3)
acao(277,414)

#Vai até T.I
time.sleep(3)
pyautogui.moveTo(544,497)
pyautogui.scroll(-300)
time.sleep(2)
pyautogui.doubleClick()

#Vai ate Relatorios BI
time.sleep(3)
pyautogui.hotkey('r', 'e')
time.sleep(2)
pyautogui.moveTo(555, 350)
pyautogui.doubleClick()

#Vai ate Arquivos de Origem
time.sleep(3)
pyautogui.moveTo(518,280)
pyautogui.doubleClick()

#Vai até AD
time.sleep(3)
pyautogui.moveTo(529,249)
pyautogui.doubleClick()

#Vai ate AD 2
time.sleep(3)
pyautogui.moveTo(529,249)
pyautogui.doubleClick()

#Salva File1
acao(869, 600, 2)

#Escolhe File 2
acao(1224,512,3)

#Volta no AD
time.sleep(3)
pyautogui.moveTo(559,118)
pyautogui.click()

#Clica em Consolidado
time.sleep(3)
pyautogui.moveTo(484,385)
pyautogui.doubleClick()

#Salva File 2
acao(869, 600, 2)

#Abre File 3
acao(1222,480,2)

#Volta para AD
acao(398,118,2)

#volta para Origem
acao(420,118,3)


#Move para cobranca 
time.sleep(3)
pyautogui.moveTo(483,321)
time.sleep(2)
pyautogui.doubleClick()

#salva file 3
acao(869, 600, 2)

#win + r
time.sleep(3)
pyautogui.hotkey('win', 'r')

#abre pasta de Origem
time.sleep(2)
pyautogui.moveTo(426,876)
pyautogui.click()
for _ in range(50):
    pyautogui.press('backspace')
time.sleep(3)
pyperclip.copy('R:\T.I\Relatorios BI\Arquivos de Origem')
pyautogui.hotkey('ctrl', 'v')
time.sleep(2)
pyautogui.press('enter')

time.sleep(5)

#Clica no AD
pyautogui.moveTo(755, 351)
pyautogui.doubleClick()

time.sleep(2)

#Abre AD
pyautogui.doubleClick()

#ScrollDown
time.sleep(3)
pyautogui.scroll(-3000)
pyautogui.scroll(-3000)
pyautogui.scroll(-3000)
pyautogui.scroll(-3000)
pyautogui.scroll(-3000)
pyautogui.scroll(-3000)
pyautogui.scroll(-3000)
pyautogui.scroll(-3000)
pyautogui.scroll(-3000)


#Renomeia
pyautogui.moveTo(867, 821)
time.sleep(5)
pyautogui.click()
pyautogui.press('f2')
pyautogui.write(DataTraco)
pyautogui.press('enter')

#volta
time.sleep(2)
acao(376,202,3)

#CONSOLIDADO
pyautogui.moveTo(726, 498)
time.sleep(2)
pyautogui.doubleClick()

#SCROLLDOWN
time.sleep(3)
pyautogui.scroll(-3000)
pyautogui.scroll(-3000)
pyautogui.scroll(-3000)
pyautogui.scroll(-3000)
pyautogui.scroll(-3000)
pyautogui.scroll(-3000)
pyautogui.scroll(-3000)
pyautogui.scroll(-3000)


#Renomeia
pyautogui.moveTo(867, 821)
time.sleep(5)
pyautogui.click()
pyautogui.press('f2')
pyautogui.write(DataTraco)
pyautogui.press('enter')

#volta
time.sleep(2)
acao(376,202,3)

#data referencia
pyautogui.moveTo(737,532)
time.sleep(2)
pyautogui.doubleClick()

#clica no excel
pyautogui.moveTo(690,355)
time.sleep(2)
pyautogui.doubleClick()

#espera o excel abrir
time.sleep(45)

#habilitar edicao
#pyautogui.moveTo(1467, 117)
#time.sleep(10)

#DESCER ATE ULTIMA CELULA
time.sleep(5)

#pyautogui.hotkey('ctrl', 'down')
pyautogui.press('down')

time.sleep(3)
#primeira celula
pyautogui.write(dataHojeMenusDois)

time.sleep(3)

#proxima celula
time.sleep(2)
pyautogui.press('left')
#escreve data
pyautogui.write(dataHoje)   


#fecha e salva
time.sleep(2)
pyautogui.moveTo(1890,25)
pyautogui.click()

#salva
pyautogui.moveTo(955,906)
pyautogui.click()

time.sleep(20)

#volta
acao(963,201,3)


#Cobrança
pyautogui.moveTo(717, 428)
pyautogui.doubleClick()

time.sleep(2)

pyautogui.scroll(-3000)
pyautogui.scroll(-3000)
pyautogui.scroll(-3000)
pyautogui.scroll(-3000)
pyautogui.scroll(-3000)
pyautogui.scroll(-3000)
pyautogui.scroll(-3000)
pyautogui.scroll(-3000)
pyautogui.scroll(-3000)
pyautogui.scroll(-3000)
pyautogui.scroll(-3000)
pyautogui.scroll(-3000)

time.sleep(3)

pyautogui.moveTo(725, 814)
pyautogui.click()

time.sleep(2)
pyautogui.press('f2')
pyautogui.write(DataTraco)

#volta
acao(843,200,3)

time.sleep(3)

pyautogui.moveTo(680, 809)

#ScrollDown
pyautogui.scroll(-3000)
pyautogui.scroll(-3000)
pyautogui.scroll(-3000)

#Clicar no AD BI
acao(699, 740, 3)
pyautogui.doubleClick()

time.sleep(40)

#atualizar
acao(970,111,3)

time.sleep(40)

#publicar
acao(1649,123)


####### Mostrar que o AD foi Publicado (Futuro IF) #######
    #clica no Outlook
acao(144,1050,2)

#clica no novo
acao(166,131,2)

#clica na barra
acao(570,329,2)

#enter
time.sleep(3)
pyautogui.write("ti5166")
pyautogui.press('enter')

acao(558,403,2)
time.sleep(3)
pyautogui.write("Ad Publicado")

acao(666,470,2)
time.sleep(3)
pyautogui.write(f"Confirmado, AD publicado às {hora} do dia {dataHoje} , sem erros registrados.")

acao(1341,458,2)

acao(1369,598,3)

acao(184,460, 3)