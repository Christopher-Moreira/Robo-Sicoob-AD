import schedule
import time

def executar_script():

    print("teste2")

schedule.every().day.at("11:06").do(executar_script)



while True:
    schedule.run_pending()
    time.sleep(1)