import time
from datetime import datetime, timedelta


feriados = [
    "01/01/2025",  # Ano Novo
    "03/03/2025",  # Carnaval (segunda-feira)
    "04/03/2025",  # Carnaval (terça-feira)
    "05/03/2025",  # Quarta-feira de Cinzas (ponto facultativo até as 14h)
    "18/04/2025",  # Sexta-feira Santa
    "21/04/2025",  # Tiradentes
    "01/05/2025",  # Dia do Trabalhador
    "19/06/2025",  # Corpus Christi (ponto facultativo)
    "07/09/2025",  # Independência do Brasil
    "12/10/2025",  # Nossa Senhora Aparecida
    "02/11/2025",  # Finados
    "15/11/2025",  # Proclamação da República
    "20/11/2025",  # Dia da Consciência Negra
    "24/12/2025",  # Véspera de Natal (ponto facultativo após as 13h)
    "25/12/2025",  # Natal
    "31/12/2025",  # Véspera de Ano Novo (ponto facultativo após as 13h)
]

def obter_hora_atual():
    agora = datetime.now()
    return agora.strftime("%H:%M:%S do dia %d/%m/%Y")

def DataHoje():

    DataHoje = datetime.now()
    return DataHoje.strftime("%d/%m/%Y")

def DatahojeComTraco():
       DataHoje = datetime.now()
       return DataHoje.strftime("%d-%m-%Y")

def DataHojeMenosUm():
    data_atual = datetime.now()
    dia_da_semana = data_atual.weekday() 

    #Segunda
    if dia_da_semana == 0:  
        data_reduzida = data_atual - timedelta(days=4)
        #Terça
    elif dia_da_semana == 1:  
        data_reduzida = data_atual - timedelta(days=3)
            #Else
    else:  
        data_reduzida = data_atual - timedelta(days=2)  

    return data_reduzida.strftime("%d/%m/%Y")

def DataHojeMenusDois():
    DataHojeMenosDois = datetime.now()
    DataFormatada = DataHojeMenosDois - timedelta(days  = 2)

    return DataFormatada.strftime("%d/%m/%Y")

def DataReduzidaFinsDeSemana():

    data_atual = datetime.now()
    dia_da_semana = data_atual.weekday() 

    if dia_da_semana == 0:  
        data_reduzida = data_atual - timedelta(days=3)
    elif dia_da_semana == 1:  
        data_reduzida = data_atual - timedelta(days=4)
    else:  
        data_reduzida = data_atual - timedelta(days=2)  

    return data_reduzida.strftime("%d/%m/%Y")

def DataMenosSeis():
    data_atual = datetime.now()
    DataMenosSeis = data_atual - timedelta(days = 6)

    return DataMenosSeis.strftime("%d/%m/%Y") 



if __name__ == "__main__":
    data = DataHoje()
    data_reduzida = DataHojeMenosUm()
    data_especifica = DataReduzidaFinsDeSemana()
    data_seis = DataMenosSeis()

    print("Data atual:", data)
    print("Data reduzida em 2 dias:", data_reduzida)
    print("Data reduzida conforme dia da semana:", data_especifica)
    print("Data Seis:", data_seis)
