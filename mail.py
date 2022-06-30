import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

email_user = "herbyalert@gmail.com"
email_password = "rpytmofsaefwytuw"
email_send = "michael.neuhaus97@gmail.com"

subject = "test email from pi"

msg = MIMEMultipart()
msg["From"] = email_user
msg["To"] = email_send
msg["Subject"] = subject

body = "test email"
msg.attach(MIMEText(body,"plain"))

text = msg.as_string()
server = smtplib.SMTP("smtp.gmail.com",587)
server.starttls()
server.login(email_user,email_password)

server.sendmail(email_user,email_send,text)
server.quit()