import mysql.connector
import pyautogui
import pyperclip
import time

def SenhaPuxa():
    # Conecta-se ao banco de dados
    db_connection = mysql.connector.connect(
        host="localhost",
        user="root",      
        password="",     
        database="robo_logins"
    )

    # Conecta com a base
    base = db_connection.cursor()

    # Executa o SQL 
    base.execute("SELECT password FROM credenciais")

    # Obtém o primeiro resultado da consulta
    get_senha = base.fetchone()

    # Limpa os resultados restantes
    base.fetchall()

    # Fecha a conexão com a base 
    base.close()
    db_connection.close()

    # Verifica se obteve um resultado
    if get_senha:
        senha_str = get_senha[0]
        return senha_str
