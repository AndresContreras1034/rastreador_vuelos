# utils/mailer.py
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config import correos

# Cambia por tu cuenta Gmail y contraseña de aplicación
email_remitente = "correomeitente"
password = key"

def enviar_correo(asunto, mensaje):
    msg = MIMEMultipart()
    msg["From"] = email_remitente
    msg["To"] = ", ".join(correos)
    msg["Subject"] = asunto

    msg.attach(MIMEText(mensaje, "plain"))

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(email_remitente, password)
        texto = msg.as_string()
        server.sendmail(email_remitente, correos, texto)
        server.quit()
        print("✅ Correo enviado correctamente")
    except Exception as e:
        print("❌ Error al enviar el correo:", e)
