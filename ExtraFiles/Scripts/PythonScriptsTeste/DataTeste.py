from datetime import datetime, timedelta

feriados = [
    "01/01/2025",
    "03/03/2025",
    "04/03/2025",
    "05/03/2025",
    "07/03/2025",
    "21/04/2025",
    "01/05/2025",
    "24/06/2025",
    "08/07/2025",
    "07/09/2025",
    "12/10/2025",
    "02/11/2025",   
    "15/11/2025",
    "25/12/2025"]

def DataReduzidaDiasEspecificos(data_teste=None):
    if data_teste:
        data_atual = datetime.strptime(data_teste, "%d/%m/%Y")
    else:
        data_atual = datetime.now()

    data_str = data_atual.strftime("%d/%m/%Y")
    
    if data_str in feriados:
        dia_da_semana = (data_atual + timedelta(days=1)).weekday()  # Verificar dia da semana após o feriado

        if dia_da_semana == 0:  # Segunda-feira
            data_reduzida = data_atual - timedelta(days=3)
        elif dia_da_semana == 1:  # Terça-feira
            data_reduzida = data_atual - timedelta(days=4)
        else:  
            data_reduzida = data_atual - timedelta(days=2)  
    else:
        if dia_da_semana == 0:  # Segunda-feira
            data_reduzida = data_atual - timedelta(days=3)
        elif dia_da_semana == 1:  # Terça-feira
            data_reduzida = data_atual - timedelta(days=4)
        else:  
            data_reduzida = data_atual - timedelta(days=2) 

    return data_reduzida.strftime("%d/%m/%Y")

if __name__ == "__main__":
    data_teste = input("Digite uma data de teste no formato dd/mm/aaaa: ")
    
    try:
        data_especifica = DataReduzidaDiasEspecificos(data_teste)
        print("Data de teste:", data_teste)
        print("Data reduzida conforme dia da semana:", data_especifica)
    except ValueError:
        print("Formato de data inválido. Por favor, insira no formato dd/mm/aaaa.")
