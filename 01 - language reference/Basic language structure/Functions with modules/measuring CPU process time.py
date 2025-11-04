# Demonstration of measuring CPU process time using process_time from the time module

from time import process_time, sleep

# Record the start process time (CPU time)
t1 = process_time()

# Simulate a time-consuming operation (sleep for 16 seconds)
sleep(16)

# Record the end process time (CPU time)
t2 = process_time()

# Calculate and print the elapsed CPU time in seconds
print('Elapsed CPU time =', t2 - t1, 'seconds')