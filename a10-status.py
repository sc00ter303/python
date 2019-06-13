#!/usr/bin/env python

import sys
import cisco
import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

myStatus = ""

#Parse the status
if len(sys.argv) > 1:
    myStatus = sys.argv[1]

    if (myStatus != "up" and myStatus != "down"):
        quit()

# me == my email address
# you == recipient's email address
me = "cs1-colo-den@sncorp.com"
you = ['netops@sncorp.com', 'CyberAnalysts@sncorp.com']

# Create message container - the correct MIME type is multipart/alternative.
msg = MIMEMultipart('alternative')
msg['Subject'] = "*** COLO A10 Path " + myStatus + " ***"
msg['From'] = me
msg['To'] = ", ".join(you)

# Create the body of the message (a plain-text and an HTML version).
text = "The COLO A10 Path is " + myStatus
html = """\
<html>
  <head></head>
  <body>
    <p>Hi!<br>
       The COLO A10 Path is """ + myStatus + """!
    </p>
  </body>
</html>
"""

# Record the MIME types of both parts - text/plain and text/html.
part1 = MIMEText(text, 'plain')
part2 = MIMEText(html, 'html')

# Attach parts into message container.
# According to RFC 2046, the last part of a multipart message, in this case
# the HTML message, is best and preferred.
msg.attach(part1)
msg.attach(part2)

#Change to the default vrf
set_vrf('default')

# Send the message via local SMTP server.
s = smtplib.SMTP('10.100.6.16')
# sendmail function takes 3 arguments: sender's address, recipient's address
# and message to send - here it is sent as one string.
s.sendmail(me, you, msg.as_string())
s.quit()
