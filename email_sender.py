import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path(R'C:\Users\Asus\Documents\Python\python\index.html').read_text())
email = EmailMessage()
email['from'] = ''
email['to'] = ''
email['subject'] = 'Tu as gagne 10 millions de dollars'

email.set_content(html.substitute({'name':'Tintin'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('', '')
    smtp.send_message(email)
    print('Tout est bon chef')