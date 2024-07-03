import psutil
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time
from dotenv import load_dotenv
import os

load_dotenv()

# Email configuration
email_sender = 'naama.tzeiri1712@gmail.com'
email_receiver = 'naama.tzeiri1712@gmail.com'
email_password = os.getenv('EMAIL_PASSWORD')
smtp_server = 'smtp.gmail.com'
smtp_port = 587

def send_email_alert(usage):
    subject = "CPU Usage Alert"
    body = f"CPU usage is at {usage}%"

    msg = MIMEMultipart()
    msg['From'] = email_sender
    msg['To'] = email_receiver
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(email_sender, email_password)
        text = msg.as_string()
        server.sendmail(email_sender, email_receiver, text)
        server.quit()
        print("Email sent successfully")
    except Exception as e:
        print(f"Failed to send email: {e}")

def monitor_cpu():
    while True:
        usage = psutil.cpu_percent(interval=1)
        if usage > 80:
            send_email_alert(usage)
        time.sleep(5)

if __name__ == "__main__":
    monitor_cpu()