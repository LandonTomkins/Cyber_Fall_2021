# use Python 3
import socket
from sys import stdout
from time import time

# sleep time guesses from debugging
DELAY = 0.500
VARIATION = 0.050

# enables debugging output
DEBUG = True

# set the server's IP address and port
ip = "localhost"
#ip = "138.47.99.64"
port = 1337
#port = 12000

# create the socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect to the server
s.connect((ip, port))

# receive data until EOF
data = s.recv(4096).decode()

# stores all of the time delays
deltaList = []

while (data.rstrip("\n") != "EOF"):
	# output the data
	stdout.write(data)
	stdout.flush()
	# start the "timer", get more data, and end the "timer"
	t0 = time()
	data = s.recv(4096).decode()
	t1 = time()
	# calculate the time delta (and output if debugging)
	delta = round(t1 - t0, 3)
	deltaList.append(delta)
	if (DEBUG):
	    stdout.write("\t{}\n".format(delta))
	    stdout.flush()

# close the connection to the server
s.close()

###########################################################################
covert_bin = ""
for i in deltaList:
    if i <= DELAY+VARIATION and i >= DELAY-VARIATION:
        covert_bin += "0"
    else:
        covert_bin += "1"
#print(covert_bin)

x = 8
bit8 = []
covert_msg = ""

# divides the input into 8 bit strings
for i in range(0, len(covert_bin), x):
    bit8.append(covert_bin[i:i+x])
#print(bit8)

# converts the binary to ascii
for index in bit8:
    uni = int(index, 2)
    char = chr(uni)
    covert_msg = covert_msg+char

# prints stdout to the console
print("\n8 Bit Secret Message: ", covert_msg)
