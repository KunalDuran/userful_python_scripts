import smtplib
import os
from email.message import EmailMessage



ID = os.environ.get('MAIL_USERNAME')
PASS = os.environ.get('MAIL_PASS')


with open('samplemail.txt') as f:
    msg = EmailMessage()
    msg.set_content(f.read())
    
msg['Subject'] = 'In love with pythoning'
msg['From'] = ID
msg['To'] = 'kunalduran13@gmail.com'


with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(ID,PASS)
    smtp.send_message(msg)

'''







with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    smtp.login(ID,PASS)

    subject = 'You Know this is subject'
    body = 'Here is body'
    msg = f'{subject}\n\n{body}'

    smtp.sendmail(ID, 'kunalduran13@gmail.com', msg)
    




'''
















