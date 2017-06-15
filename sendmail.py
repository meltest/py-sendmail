# -*- coding: utf-8 -*-

import smtplib

from email.mime.text import MIMEText

print "smtp server domain: "
smtp_server = raw_input()

print "from address: "
from_address = raw_input()

print "to address: "
to_address = raw_input()

print "subject: "
subject = raw_input()

print "message:  "
message = raw_input()

msg = MIMEText(message)

msg['Subject'] = subject
msg['From'] = from_address
msg['To'] = to_address

smtp = smtplib.SMTP(smtp_server)
smtp.connect
smtp.sendmail(from_address, to_address, msg.as_string())
smtp.close()

print "sendmail complete."
