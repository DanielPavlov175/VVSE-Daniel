import smtplib
from email.mime.text import MIMEText
email_address="danielpavlov175@gmail.com"
email_password="tkoxltljfupcymf"
to_email="ddimitrov@elsys-bg.org"
body=f"Email"
message=MIMEText(body)
message["From"]=email_address
message["To"]=to_email
message["Subject"]="Python email from Daniel Pavlov 9g"
with smtplib.SMTP_SSL("smtp.gmail.com",465)as server:
    server.login(email_address,email_password)
    server.send_message(message)
print("Email sent")