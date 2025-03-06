from datetime import datetime, timedelta


def DataAtual():

    data_atual = datetime.now()

    return data_atual.strftime("%d/%m/%Y")

def DataReduzidaDoisDias():

    data_atual = datetime.now()
    data_menos_dois_dias = data_atual - timedelta(days=2)

    return data_menos_dois_dias.strftime("%d/%m/%Y") 


def DataReduzidaDiasEspecificos():
    data_atual = datetime.now()
    dia_da_semana = data_atual.weekday() 

    if dia_da_semana == 0:  
        data_reduzida = data_atual - timedelta(days=3)
    elif dia_da_semana == 1:  
        data_reduzida = data_atual - timedelta(days=4)
    else:  
        data_reduzida = data_atual - timedelta(days=2)  

    return data_reduzida.strftime("%d/%m/%Y")

if __name__ == "__main__":
    data = DataAtual()
    data_reduzida = DataReduzidaDoisDias()
    data_especifica = DataReduzidaDiasEspecificos()

    print("Data atual:", data)
    print("Data reduzida em 2 dias:", data_reduzida)
    print("Data reduzida conforme dia da semana:", data_especifica)