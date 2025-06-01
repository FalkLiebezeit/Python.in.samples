# Here a list is defined
LST1=[7,8,9,10,11,12,15]
# Get every second element
OUTPUT = LST1[::2]
print(OUTPUT)  # OUTPUT: [7,9,11,15]
# Get every third element
OUTPUT = LST1[::3]
print(OUTPUT)  # OUTPUT: [7,10,15]
# In case of Strings
LST2= "Python Course"
# Start from 1st index in above given string
# and get every second character
OUTPUT= LST2[1::2]
print(OUTPUT)  # OUTPUT: yhnCus
# Reverse of a List1 using negative step size i.e.-1
OUTPUT = LST1[::-1]
print(OUTPUT)
# Reverse of a String using negative step
OUTPUT = LST2[::-1]
print(OUTPUT)
# Following the start,stop and step sequence for List
# Here, it means start from 0th index,
# 4th index is the stop i.e.slice end and
# 2 is the step size
LST3 = [10,11,12,15,25,27]
OUTPUT = LST3[0:5:2]
print(OUTPUT)
