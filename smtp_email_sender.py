# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 16:57:30 2021

@author: oguzhan.alptekin
"""

import smtplib, ssl
from email.mime.text import MIMEText

sender = 'ebys@marmaraosb.org'
receivers = ['oguzhan.alptekin@cbksoft.com', 'alptekinoguz@gmail.com']
body_of_email = 'Test Email'

msg = MIMEText(body_of_email, 'html')
msg['Subject'] = 'Test Email'
msg['From'] = sender
msg['To'] = ",".join(receivers)

#possible ports: 465, 587

s = smtplib.SMTP(host = 'mail.marmaraosb.org', port = 587)
s.login(user = 'ebys@marmaraosb.org', password = 'AWSgMRfy3J(J')
s.sendmail(sender, receivers, msg.as_string())
print('email sent')
s.quit()



"""SSL
s = smtplib.SMTP_SSL(host = 'mail.marmaraosb.org', port = 587)
s.login(user = 'ebys@marmaraosb.org', password = 'AWSgMRfy3J(J')
s.sendmail(sender, receivers, msg.as_string())
print('email sent')
s.quit()
"""