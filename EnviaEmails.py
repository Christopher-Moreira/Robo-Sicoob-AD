import smtplib
import time
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText



def hora():
    agora = datetime.now()
    return agora.strftime("%H:%M:%S do dia %d/%m/%Y")

def hoje():
    DataHoje = datetime.now()
    return DataHoje.strftime("%d/%m/%Y")


def enviar_email(destinatario, assunto, mensagem):
    remetente = ''
    senha = ''

    # Cria a mensagem
    msg = MIMEMultipart()
    msg['From'] = remetente
    msg['To'] = destinatario
    msg['Subject'] = assunto
    msg.attach(MIMEText(mensagem, 'plain'))

    # Configura o servidor SMTP
    servidor = smtplib.SMTP('smtp-mail.outlook.com', 587)
    servidor.starttls()
    servidor.login(remetente, senha)

    # Envia o e-mail
    servidor.sendmail(remetente, destinatario, msg.as_string())
    servidor.quit()

# Exemplo de uso
Hora = hora()
Hoje = hoje()

destinatario = 'ti5166@sicoob.com.br'
assunto = 'Geração do AD feita com sucesso'
mensagem = f'O AD foi gerado sem nenhuma falha às {Hora} do dia {Hoje}'
enviar_email(destinatario, assunto, mensagem)