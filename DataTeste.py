from datetime import datetime, timedelta

def DataAtual():
    data_atual = datetime.now()
    return data_atual.strftime("%d/%m/%Y")

def DataReduzidaDoisDias():
    data_atual = datetime.now()
    data_menos_dois_dias = data_atual - timedelta(days=2)
    return data_menos_dois_dias.strftime("%d/%m/%Y")

def DataReduzidaDiasEspecificos(data_teste=None):
   
    if data_teste:
        data_atual = datetime.strptime(data_teste, "%d/%m/%Y")
    else:
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

    data_atual = DataAtual()
    data_teste = data_atual

    
    data_especifica = DataReduzidaDiasEspecificos(data_teste)

    print("Data de teste:", data_teste)
    print("Data reduzida conforme dia da semana:", data_especifica)