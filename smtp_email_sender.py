# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 16:57:30 2021
@author: oguzhan.alptekin
"""

import smtplib, ssl
from email.mime.text import MIMEText

sender = 'SENDER_MAIL'
receivers = ['RECIEVER_MAIL']
body_of_email = 'Test Email'

msg = MIMEText(body_of_email, 'html')
msg['Subject'] = 'Test Email'
msg['From'] = sender
msg['To'] = ",".join(receivers)

#possible ports: 465, 587

#USE smtplib.SMTP_SSL if SSL

s = smtplib.SMTP(host = 'SMTP', port = 587)
s.login(user = 'USER', password = 'PASS')
s.sendmail(sender, receivers, msg.as_string())
print('email sent')
s.quit()
