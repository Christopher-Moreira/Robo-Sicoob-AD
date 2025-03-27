import pyautogui
import pyperclip
import schedule
import time
import os
from UsedFiles.DataAndTimeRequest.GetDatas import DataHoje, DataReduzidaFinsDeSemana, DataHojeMenosUm, DataHojeMenusDois, DataMenosSeis, DatahojeComTraco, Obter_hora_atual,Hora_atual_com_traco
from UsedFiles.RequestsDB.GetLogin import LoginPuxa
from UsedFiles.RequestsDB.GetSenha import SenhaPuxa
from UsedFiles.ErrorReg.GetError import NoErrorPath, ErrorRename, ErrorAtualizar_ADcsv
 
login = LoginPuxa()
senha = SenhaPuxa()

hora = Obter_hora_atual()
horatraco = Hora_atual_com_traco()
dataFinsDeSemana = DataReduzidaFinsDeSemana()
dataHoje = DataHoje()
dataMenusUm = DataHojeMenosUm()
dataHojeMenusDois = DataHojeMenusDois()
dataSeisDias = DataMenosSeis()
DataTraco = DatahojeComTraco()

dir = "Images/Screenshots"
path = os.path.join(dir, f"Dia {DataTraco}  Hora {horatraco}.png")


########### Instancia a função de ação ###########
 
def acao(x, y, delay=1):
    time.sleep(delay)
    pyautogui.moveTo(x, y)
    pyautogui.click()


########### Começa Execução do Código ###########

def executar_script():

    # Clicar no sisbr
    acao(300, 1053)

    time.sleep(30)

    #coloca login
    acao(1054, 465, 2)
    time.sleep(3)
    for j in range(50):
        pyautogui.press('backspace')
    pyperclip.copy(login)
    pyautogui.hotkey('ctrl', 'v')

    time.sleep(3)

    #coloca senha
    acao(1015, 501, 2)
    time.sleep(3)
    pyperclip.copy(senha)
    pyautogui.hotkey('ctrl', 'v')

    #logar
    time.sleep(3)
    acao(802,684,2)

    #logar botao
    time.sleep(3)
    acao(804,683,2)


    time.sleep(20)

    # Clicar na barra de pesquisa
    acao(197, 968)

    # Esperar segundos
    time.sleep(3)

    # Digitar 'Conta Corrente'
    pyautogui.write("Conta Corrente")

    # Esperar para clicar em 'Conta Corrente'
    acao(104, 279, 3)

    time.sleep(15)

    # Clicar nos relatórios
    acao(484, 126, 3)

    time.sleep(5)

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

    time.sleep(10)
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

    time.sleep(10)

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

    time.sleep(10)
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
    acao(403,216,5)
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
    pyautogui.moveTo(402, 972)
    time.sleep(5)
    pyautogui.click()
    pyautogui.press('f2')
    pyautogui.write(DataTraco)
    pyautogui.press('enter')

    ################# Erro Rename 1
    time.sleep(5)
    if ErrorRename():
    
        screenshot = pyautogui.screenshot()
        screenshot.save(path)

        time.sleep(5)       
        acao(144,1050,2)

        #clica no novo
        acao(166,131,2)

        #clica na barra
        acao(429,218,2)

        #enter
        time.sleep(3)
        pyautogui.write("ti5166@sicoob.com.br")
        pyautogui.press('enter')
        time.sleep(2)
        pyautogui.hotkey('space')

        time.sleep(3)

       # pyautogui.write('gerentes5166@sicoob.com.br')
        time.sleep(2)
        pyautogui.press('enter')

        #clica em assunto
        acao(550, 320, 2)
        time.sleep(3)
        pyautogui.write("ERRO AD - AD-> File Already Exists")

        acao(454, 378, 2)
        time.sleep(3)
        #pyperclip.copy(f"Confirmado, AD publicado às {hora} do dia {dataHoje}, sem erros registrados.")
        #pyautogui.hotkey('ctrl', 'v')
        pyperclip.copy(f"File Already Exists: Erro durante a geração do AD:\n-O arquivo não pode ser renomeado porque já existe um arquivo com o mesmo nome;\n-File Path: R:\T.I\Relatorios BI\Arquivos de Origem\AD\AD\n-File Name:'{dataHoje}'\n-{dataHoje} - {hora}.")
        pyautogui.hotkey('ctrl', 'v')

        #anexa print
        acao(1028,127,2)
        time.sleep(3)
        acao(1160,922,2)

        acao(549, 69, 2)
        pyperclip.copy('\Desktop\ScriptDias\Images\Screenshots')
        pyautogui.hotkey('ctrl','v')
        time.sleep(3)
        acao(485, 270,2)
        pyautogui.press('end')
        time.sleep(3)
        pyautogui.press('enter')

        
        acao(1781, 308, 2)

        acao(1745, 456, 2)

        acao(78, 296, 3)

    else:
        time.sleep(10)
        #volta para o AD 
        time.sleep(2)
        acao(1194,69,2)

        time.sleep(3)   

        #CONSOLIDADO
        pyautogui.moveTo(318, 363)
        time.sleep(3)
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
        pyautogui.moveTo(308, 973)
        time.sleep(5)
        pyautogui.click()
        pyautogui.press('f2')
        pyautogui.write(DataTraco)
        pyautogui.press('enter')

        time.sleep(5)
    ############### Erro Rename 2
    if ErrorRename():
            
        acao(144,1050,2)

        #clica no novo
        acao(166,131,2)

        #clica na barra
        acao(429,218,2)

        #enter
        time.sleep(3)
        pyautogui.write("ti5166@sicoob.com.br")
        pyautogui.press('enter')
        time.sleep(2)
        pyautogui.hotkey('space')

        time.sleep(3)

       # pyautogui.write('gerentes5166@sicoob.com.br')
        time.sleep(2)
        pyautogui.press('enter')

        #clica em assunto
        acao(550, 320, 2)
        time.sleep(3)
        pyautogui.write("ERRO AD - CONSOLIDADO -> File Already Exists")

        acao(454, 378, 2)
        time.sleep(3)
        #pyperclip.copy(f"Confirmado, AD publicado às {hora} do dia {dataHoje}, sem erros registrados.")
        #pyautogui.hotkey('ctrl', 'v')
        pyperclip.copy(f"File Already Exists: Erro durante a geração do AD:\n-O arquivo não pode ser renomeado porque já existe um arquivo com o mesmo nome.\n-File Path: R:\T.I\Relatorios BI\Arquivos de Origem\AD\CONSOLIDADO\n-File Name:'{dataHoje}'\n-{dataHoje} - {hora}.")
        pyautogui.hotkey('ctrl', 'v')
        
        acao(1781, 308, 2)

        acao(1745, 456, 2)

        acao(78, 296, 3)
        
    else:

        #volta para o AD
        time.sleep(2)
        acao(1051,72,3)



        #########################Processo de abrir e editar o arquivo Excel#########################

        time.sleep(5)
        #data referencia
        pyautogui.moveTo(503,397)

        #clica na pasta
        time.sleep(2)
        pyautogui.doubleClick()

        #vai ate o Excel
        time.sleep(2)
        pyautogui.moveTo(457,215)

        #abre o Excel
        pyautogui.doubleClick()

        #espera o Excel abrir
        time.sleep(30)

        #clica para baixo para selecionar celula de baixo
        pyautogui.hotkey('Down')
        time.sleep(3)

        pyautogui.hotkey('Left')
        time.sleep(2)

        pyautogui.hotkey('Left')
        time.sleep(2)
        

        #escreve data de referencia (Data reduzida de acordo com o dia da semana)
        pyperclip.copy(dataHoje)
        pyautogui.hotkey('ctrl', 'v')

        #vai para celula do lado
        pyautogui.hotkey('Right')
        time.sleep(2)

    
        #escreve data de hoje
        pyperclip.copy(dataFinsDeSemana)
        pyautogui.hotkey('ctrl', 'v')

        #Fecha o Excel
        time.sleep(3)
        acao(1889,26,2)

        #Salva
        acao(937,918,2)
        time.sleep(20)

        #volta arquvios origem
        acao(910,70,5)

        #Vai ate cobrança
        pyautogui.moveTo(332,287)
        pyautogui.doubleClick()

        #Cobrança
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
        pyautogui.moveTo(308, 973)
        time.sleep(5)
        pyautogui.click()
        pyautogui.press('f2')
        pyautogui.write(DataTraco)
        pyautogui.press('enter')

        time.sleep(5)

    ################ Erro Rename 3
    if ErrorRename():
            
        acao(144,1050,2)

        #clica no novo
        acao(166,131,2)

        #clica na barra
        acao(429,218,2)

        #enter
        time.sleep(3)
        pyautogui.write("ti5166@sicoob.com.br")
        pyautogui.press('enter')
        time.sleep(2)
        pyautogui.hotkey('space')

        time.sleep(3)

       # pyautogui.write('gerentes5166@sicoob.com.br')
        time.sleep(2)
        pyautogui.press('enter')

        #clica em assunto
        acao(550, 320, 2)
        time.sleep(3)
        pyautogui.write("ERRO Cobrança -> File Already Exists")

        acao(454, 378, 2)
        time.sleep(3)
        #pyperclip.copy(f"Confirmado, AD publicado às {hora} do dia {dataHoje}, sem erros registrados.")
        #pyautogui.hotkey('ctrl', 'v')
        pyperclip.copy(f"File Already Exists: Erro durante a geração do AD:\n-O arquivo não pode ser renomeado porque já existe um arquivo com o mesmo nome.\n-File Path: R:\T.I\Relatorios BI\Arquivos de Origem\Cobrança\n-File Name:'{dataHoje}'\n-{dataHoje} - {hora}.")
        pyautogui.hotkey('ctrl', 'v')
        
        acao(1781, 308, 2)

        acao(1745, 456, 2)

        acao(78, 296, 3)   

    else:
        #volta #relatorios BI
        acao(878,68,3)

        time.sleep(3)

        pyautogui.moveTo(329, 702)

        #ScrollDown
        pyautogui.scroll(-3000)
        pyautogui.scroll(-3000)
        pyautogui.scroll(-3000)

        ##############################Clicar no AD BI######################################


        acao(368,707,2)
        pyautogui.doubleClick()

        time.sleep(40)

        #atualizar
        acao(932,113,3)

    ###############################Checa a conclusão do AD###############################

        
        time.sleep(45)
            #publicar
        acao(1605,116,3)

        acao(1050, 573,2)

        time.sleep(25)

            #relatorios BI
        acao(714, 495, 5)

            #selecinar
        acao(1112,737,5)

        time.sleep(10)

            #substituir
        acao(1030,687,2)


        time.sleep(30)

            #salvar
        acao(1185,693,2)


################### Caminho Sem Erro
                #clica no Outlook
        acao(144,1050,2)

            #clica no novo
        acao(166,131,2)

            #clica na barra
        acao(429,218,2)

            #enter
        time.sleep(3)
        pyautogui.write("ti5166@sicoob.com.br")
        pyautogui.press('enter')
        time.sleep(2)
        pyautogui.hotkey('space')

        time.sleep(3)

        pyautogui.write('gerentes5166@sicoob.com.br')
        time.sleep(2)
        pyautogui.press('enter')

            #clica em assunto
        acao(550, 320, 2)
        time.sleep(3)
        pyautogui.write("Ad Publicado")

        acao(454, 378, 2)
        time.sleep(3)
        pyperclip.copy(f"Confirmado, AD publicado às {hora} do dia {dataHoje}, sem erros registrados.")
        pyautogui.hotkey('ctrl', 'v')
            #pyautogui.write("Sem Erro AutoMitigado")

        acao(1781, 308, 2)

        acao(1745, 456, 2)

        acao(78, 296, 3)

        #Minimiza E-mail
        acao(144,1050,2)

        #Fecha BI
        acao(1890, 20, 3)

        time.sleep(2)
        #Clica no SISBR
        acao(313, 1054 ,3)

        time.sleep(2)
        #Fecha Cobranca
        acao(560, 844, 3)

        time.sleep(2)
        #fecha sisbr
        acao(426, 834, 3)
        
        time.sleep(2)
        acao(1060, 673, 3)


schedule.every().day.at("08:42").do(executar_script)

while True:
    schedule.run_pending()
    time.sleep(1)