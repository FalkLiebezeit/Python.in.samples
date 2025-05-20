import time;
from datetime import datetime


localtime = time.asctime(time.localtime(time.time()))
print("Local current time :",localtime)

print("current date :", datetime.today().date())



