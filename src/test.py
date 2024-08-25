import pywhatkit
import datetime
import os
import sys

current_time = datetime.datetime.now()
curr_hour = current_time.hour
curr_min = current_time.minute

#def sendText(number, text):

workingdirectory = os.getcwd()
number = sys.argv[1]
text = sys.argv[2]

number = "+91" + number
pywhatkit.sendwhatmsg(number, text, curr_hour, curr_min+2)

