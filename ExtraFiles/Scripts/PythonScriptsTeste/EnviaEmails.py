import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Configurações do e-mail
email_usuario = "christopher.m5166@sicoob.com.br"
senha = ""
email_destino = "ti5166@sicoob.com.br"
assunto = "Assunto do E-mail"
corpo = "Este é o corpo do e-mail."

# Criar o e-mail
mensagem = MIMEMultipart()
mensagem["From"] = email_usuario
mensagem["To"] = email_destino
mensagem["Subject"] = assunto

mensagem.attach(MIMEText(corpo, "plain"))

try:
    # Conectar ao servidor do Outlook e enviar o e-mail
    servidor = smtplib.SMTP("smtp.office365.com", 587)
    servidor.starttls()
    servidor.login(email_usuario, senha)
    servidor.sendmail(email_usuario, email_destino, mensagem.as_string())
    print("E-mail enviado com sucesso!")
    servidor.quit()
except Exception as e:
    print(f"Erro ao enviar e-mail: {e}")
