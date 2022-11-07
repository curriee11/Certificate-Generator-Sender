# importing libraries
import os
import re
import time
import smtplib
import imghdr
from email.message import EmailMessage
from email.utils import formataddr

EMAIL_ADDRESS = 'impoeish@gmail.com'
EMAIL_PASSWORD = 'Khush178910!!'

i = 1
with open("emaillogs.txt", 'a') as f:
    for filename in os.listdir('certificates'):
        try:
            # smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            print("ok")
            with open(os.path.join('certificates', filename), 'rb') as fp:
                file_data = fp.read()
                msg = EmailMessage()
                msg['Subject'] = 'Email Subject Here'
                msg['From'] = formataddr(
                    ('Sender Name', 'sender email'))
                mail_to = filename.rsplit(".", 1)[0]
                msg['To'] = mail_to
                msg.set_content('''Email Content Goes Here''')
                # print("ok");
                msg.add_attachment(file_data, maintype='application',
                                   subtype='pdf', filename='techtehvaar.pdf')
                print('read file '+str(i)+" "+str(filename))
                print("ok")
               
                # with smtplib.SMTP_SSL('smtp.gmail.com', 587) as smtp:
                #     print("ok")
                #     smtp.login()
                #     print("hi")
                #     smtp.send_message(msg)
                # server = smtplib.SMTP('smtp.gmail.com', 587)
                # server.ehlo()
                # server.starttls()
                # server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
                
                s = smtplib.SMTP('smtp.gmail.com', 587)
                s.starttls()
                print("kya")
                s.login("impoeish@gmail.com", "Khush178910!!")
                print("wow")
                s.send_message = msg
                s.sendmail("impoeish@gmail.com", dest, message)
                s.quit()
                # s.sendmail("impoeish@gmail.com", dest, message)
     
   
                
                
                # initialize connection to our
                   # initialize connection to our
# email server, we will use gmail here
                # smtp = smtplib.SMTP('smtp.gmail.com', 587)
                # smtp.login('Your Email', 'Your Password')
                # smtp.ehlo()
                # smtp.starttls()
  
# Login with your email and password
                
               
  
                print("k")
                print(str(mail_to) + " Sending Success")
                f.write(str(mail_to) + " Sending Success")
                f.write("\n")
                i += 1
        except:
            print(str(mail_to) + " Sending Failed")
            f.write("\n")
            f.write(str(mail_to)+" Sending Failed")
    f.close()
