import time
from datetime import datetime

# Get the current local time as a formatted string
localtime = time.asctime(time.localtime(time.time()))
print("Local current time:", localtime)

# Get the current local date using datetime
current_date = datetime.today().date()
print("Local current date:", current_date)