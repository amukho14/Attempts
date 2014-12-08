__author__ = 'amukhopadhyay'

import urllib
from googlevoice import Voice
from googlevoice.util import input
import time
voice = Voice()
voice.login("gut123lin@gmail.com",raw_input("pass"))
phoneNumber = "+91-9550606490"
text = "text"
i=0
while i < 10:
        voice.send_sms(phoneNumber, text)
        time.sleep(60)
        i = i + 1

# site = "https://oncourse.umn.edu/recreg/Pages/frmCourseDetail.aspx?serviceoff_pk=251757"
# a=urllib.urlopen(site).read()
#
# while a.find("0 available") != -1:
#         time.sleep(60)
#         a=urllib.urlopen(site).read()
#         print a.find("0 available")
#
#
# while i < 10:
#         voice.send_sms(phoneNumber, text)
#         time.sleep(60)
#         i = i + 1
