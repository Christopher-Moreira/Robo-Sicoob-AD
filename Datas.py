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


def DataHoje():

    DataHoje = datetime.now()
    return DataHoje.strftime("%d/%m/%Y")

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

