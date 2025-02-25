import mysql.connector

# Conecta-se ao banco de dados
db_connection = mysql.connector.connect(
    host="localhost",
    user="root",      
    password="",     
    database="robo_logins"
)

#Conecta com a base
base = db_connection.cursor()

#Executa o SQL 
base.execute("SELECT * FROM credenciais")

#Torna o resultado em um executavel
resultados = base.fetchall()

base.close()
db_connection.close()
#^^^^^^^^^^
#Fecha a conexão com a base 

#Cria um array com os dados
logins_lista = [list(login) for login in resultados]

# Imprime a lista de logins
print(logins_lista)
