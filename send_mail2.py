import smtplib
import os

content = 'This mail was sent from python script,trying to send to two same time'

mail = smtplib.SMTP('smtp.gmail.com', 587)

mail.ehlo()

mail.starttls()

mail.login(os.environ.get('MAIL_USERNAME'), os.environ.get('MAIL_PASS'))

mail.sendmail(os.environ.get('MAIL_USERNAME'),['kunalduran13@gmail.com','kunalduran16@gmail.com'], content)

mail.close()
