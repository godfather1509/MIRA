import smtplib
from email.mime.text import MIMEText

subject = "Email Subject"
body = "This is the body of the text message"
sender = "ayush1500g@gmail.com"
recipients = ["ayushg1500@gmail.com"]
password = "roml pyso volo wisr"


def send_email(subject, body, sender, recipients, password):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ', '.join(recipients)
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
       smtp_server.login(sender, password)
       smtp_server.sendmail(sender, recipients, msg.as_string())
    print("Message sent!")


send_email(subject, body, sender, recipients, password)