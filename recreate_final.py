#The Magicians
#This program is meant to mimic the typing patterns of a user. The patterns, both the text and the typing speed,
#can be altered on the fly and the code should, after a 5 second delay, type the message as directed

#this is all the importing and setting things up for the rest of the code
from pynput.keyboard import Key, Controller
from time import sleep
from random import uniform
from termios import tcflush, TCIFLUSH
from sys import stdout

keyboard = Controller()

#here are where the actual "biometerics" are stored
#the password is the actual text being typed by the program, and then the timings being the "pattern"
#the code is looking to copy
password = "C, a, n,  , y, o, u,  , b, e, l, i, e, v, e,  , c, y, b, e, r, s, t, o, r, m,  , i, s,  , i, n,  , t, w, o,  , w, e, e, k, s, ?, Ca, an, n ,  y, yo, ou, u ,  b, be, el, li, ie, ev, ve, e ,  c, cy, yb, be, er, rs, st, to, or, rm, m ,  i, is, s ,  i, in, n ,  t, tw, wo, o ,  w, we, ee, ek, ks, s?"


timings = "0.27, 0.51, 0.69, 0.71, 0.38, 0.42, 0.36, 0.90, 1.00, 0.16, 0.40, 0.82, 0.33, 0.60, 0.58, 0.87, 0.47, 0.30, 0.47, 0.73, 0.83, 0.94, 0.80, 0.43, 0.42, 0.24, 0.43, 0.19, 0.37, 0.18, 0.34, 0.44, 0.20, 0.33, 0.42, 0.77, 0.41, 0.73, 0.88, 0.22, 0.35, 0.67, 0.27, 0.38, 0.35, 0.34, 0.86, 0.26, 0.90, 0.35, 0.75, 0.17, 0.51, 0.26, 0.75, 0.10, 0.95, 0.67, 0.33, 0.28, 0.27, 0.41, 0.52, 0.12, 0.25, 0.72, 0.52, 0.93, 0.26, 0.45, 0.46, 0.99, 0.39, 0.54, 0.39, 0.81, 0.31, 0.18, 0.36, 0.40, 0.23, 0.85, 0.40, 0.74, 0.12"

#need to get the password into a useable state
#first remove all the commas and needless spaces
#then use only the first half due to the second not being needed
password = password.split(", ")
password = password[:len(password) // 2 + 1]
password = "".join(password)

#similar to the password, we need to make th einputs useable
#get rid of the commas
#convert the strings into floats
#keypress values are teh second half of timings
#keyintervals are the first half of timings
timings = timings.split(",")
timings = [ float(a) for a in timings ]
keypress = timings[:len(timings) // 2 + 1]
keyinterval = timings[len(timings) // 2 + 1:]
keyinterval.append(0)
#print(f"KHTs = {keypress}")
#print(f"KITs = {keyinterval}")

#set the position to 0 for the upcoming loop
pos = 0
#sleep for 5 so you can get the rigth window up
sleep(5.0)

#for each character in the password
for char in password:
	#press teh key
    keyboard.press(char)
    #wait for how long teh user would hold the key
    sleep(keypress[pos])
    #realse teh key
    keyboard.release(char)
    #wait for however long the user would wait
    sleep(keyinterval[pos])
    #move to the next position for the next loop
    pos += 1
    
#this is the wrap up of the code
#print is to set the next line in the terminal to a new line
print()
#this is to flush out stdout
tcflush(stdout, TCIFLUSH)
#presses and releases the enter key to finish up the time in teh TKinter window
keyboard.press(Key.enter)
keyboard.release(Key.enter)
