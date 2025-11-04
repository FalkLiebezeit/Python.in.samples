# Demonstration of measuring elapsed time using perf_counter from the time module

from time import perf_counter, sleep

# Record the start time
t1 = perf_counter()

# Simulate a time-consuming operation (sleep for 16 seconds)
sleep(16)

# Record the end time
t2 = perf_counter()

# Calculate and print the elapsed time in seconds
print('Elapsed time =', t2 - t1, 'seconds')