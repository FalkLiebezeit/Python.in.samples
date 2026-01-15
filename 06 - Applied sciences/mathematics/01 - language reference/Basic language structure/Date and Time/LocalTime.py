import time
from datetime import datetime

# Get the current local time as a formatted string
local_time = time.asctime(time.localtime())
print("Local current time:", local_time)

# Get the current local date using datetime
current_date = datetime.today().date()
print("Current date:", current_date)