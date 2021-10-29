##############################################################################################
# The Magician
# Takes the input of a date and time, finds the time in seconds since then, hashes the
# result twice, and then prints out the first 2 letters left-to-right and the first 2
# numbers right-to-left
##############################################################################################

import datetime
import math
import hashlib

# setting the interval for validity of codes and making some variable used to put the final output together
interval = 60
code = ""
count = 0

# helper function to tell if something is affected by daylight savings time based on CST
def is_dst(self):

    if self.month > 11 or self.month < 3:
        return True
    elif (self.month == 11 and self.day > 7) or (self.month == 3 and self.day < 14):
        return True
    elif (self.month == 11 and self.day > 7 and self.hour >= 2) or (self.month == 3 and self.day == 14 and self.hour < 2):
        return True
    else: 
        return False


##############################################################################################
# Main Section of the program
##############################################################################################

# format the input and place the values into a datetime object along with the current time
d = input().split(" ")
for i in range (0,6):
    d[i] = int(d[i])

time = datetime.datetime(d[0],d[1],d[2],d[3],d[4],d[5])
time1 = datetime.datetime.now()

# calculate the time difference between the two objects and cut off the decimals
timediff = time1-time
timediff = math.floor(timediff.total_seconds())

# adjust the difference by an hour in the approprite direction if applicable
if is_dst(time) and not is_dst(time1):
    timediff -= 3600
if is_dst(time1) and not is_dst(time):
    timediff += 3600


# change the difference to the preceding multiple of the time interval for validity
timediff -= timediff % interval
timediff = str(timediff)

# perform the MD5 hashes and store the final result
result1 = str(hashlib.md5(timediff.encode("utf-8")).hexdigest())
result2 = str(hashlib.md5(result1.encode("utf-8")).hexdigest())

# find the first 2 letters from left-to-right and add them to the output
for char in result2:
    if(count==2):
        break
    if char.isalpha():
        code+=char
        count+=1

count = 0

#find the first 2 numbers from right-to-left and add them to the output
for char in result2[::-1]:
    if(count==2):
        break
    if char.isnumeric():
        code+=char
        count+=1

# print the output and the current system time
print(code+"\n")
print("Current System Time: ", end="")
print("{:04d} {:02d} {:02d} {:02d} {:02d} {:02d}".format(time1.year,time1.month,time1.day,time1.hour,time1.minute,time1.second))

