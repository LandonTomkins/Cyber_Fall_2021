from pynput.keyboard import Controller
from time import sleep
from random import uniform
from termios import tcflush, TCIFLUSH
from sys import stdout

keyboard = Controller()

password = input()
timings = input()

print(f"Features = {password}")
print(f"Timings = {timings}")

password = password.split(",")
password = password[:len(password) // 2 + 1]
password = "".join(password)
print(f"Sample = \"{password}\"")

timings = timings.split(",")
timings = [ float(a) for a in timings ]
keypress = timings[:len(timings) // 2 + 1]
keyinterval = timings[len(timings) // 2 + 1:]
keyinterval.append(0)
print(f"KHTs = {keypress}")
print(f"KITs = {keyinterval}")

pos = 0
sleep(5)

for char in password:
    keyboard.press(char)
    sleep(keypress[pos])
    keyboard.release(char)
    sleep(keyinterval[pos])
    pos += 1

tcflush(stdout, TCIFLUSH)
print()
