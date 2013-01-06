import csv, random, smtplib, time

from email.header    import Header
from email.mime.text import MIMEText

morning   = {}
afternoon = {}
chosen    = {}

reader = csv.reader(open('questions.csv', 'r'),
                    quotechar = '"')


for row in reader:    
    if row[1] == 'morning':
        morning[ row[2] ] = 1
    else:
        afternoon[ row[2] ] = 1


msg = ''

msg = "Morning questions. Choose two.\n"
for i in range(1,5):
    choice = random.choice(morning.keys())
    if choice not in chosen: 
        msg += "%d. %s" % (i, choice)
        msg += "\n"
        chosen[ choice ] = 1
    #time.sleep(1)

msg += "\n"
msg += "Afternoon questions. Choose two."
for i in range(1,5):
    choice = random.choice(afternoon.keys())
    if choice not in chosen: 
        msg += "%d. %s" % (i, choice)
        msg += "\n"
        chosen[ choice ] = 1
    #time.sleep(1)

emailmsg = MIMEText(msg, _charset='utf-8') 
emailmsg['Subject'] = Header("Practice Prelim Exam Winter 2013", 'utf-8')
emailmsg['From']    = "Prelim committee"
emailmsg['To']      = "alex.hanna@gmail.com"

s = smtplib.SMTP('localhost')
s.sendmail('ahanna', ['alex.hanna@gmail.com'], emailmsg.as_string())
s.quit()
