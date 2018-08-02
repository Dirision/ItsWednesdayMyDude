import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

from time import sleep
from datetime import datetime, date

# Add to this list to add receivers 
emailReceivers=["Put", "victims", "emails", "in", "this", "list"]
COMMASPACE=', '
# Set SMTP info
msg = MIMEMultipart()
msg['Subject'] = 'IT IS WEDNESDAY, MY DUDES'
msg['From'] = 'yourEmailGoesHere'
msg['To'] = COMMASPACE.join(emailReceivers)
msg.preamble = 'It is Wednesday, my dudes'
fp = open('WMD.jpg','rb')
img = MIMEImage(fp.read())
fp.close()
msg.attach(img)

def isWednesday():
    return datetime.now().strftime('%a') == 'Wed'

if __name__ == '__main__':
   
    print(emailReceivers)
    print(msg.as_string()) 
    while True:
        if isWednesday():
            print("IT IS WEDNESDAY MY DUDES")
            # compose and send message with image 
            s=smtplib.SMTP('smtp.gmail.com')
            s.ehlo()
            s.starttls()
            s.login('YourEmailGoesHere','YourPasswordGoesHere') 
            s.sendmail('YourEmailGoesHere',emailReceivers,msg.as_string())
            s.quit()
        else:
            print("It is not wednesday :(")
        # Wait until tomorrow 
        sleep(24*60*60)
