import pyautogui
import time

def acao(x, y, delay=1):
    time.sleep(delay)
    pyautogui.moveTo(x, y)
    pyautogui.click()

# Clicar no SisBR
acao(300, 1053)

# Clicar na barra de pesquisa
acao(197, 968)

# Esperar dois segundos
time.sleep(2)

# Digitar 'Conta Corrente'
pyautogui.write("Conta Corrente")

# Esperar para clicar em 'Conta Corrente'
acao(104, 279, 2)

# Clicar nos relatórios
acao(494, 126, 2)

# Clicar em relatório saldos
acao(591, 332, 1)

# Clicar em saldos
acao(858, 335, 1)

# Clicar no devedor
acao(700, 508, 1)

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
