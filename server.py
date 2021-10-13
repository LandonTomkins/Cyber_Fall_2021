import socket
from time import sleep

port = 1337

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("", port))
s.listen(0)
print("Server is listening...")

c, addr = s.accept()

msg = "This is the visible string that contains a secret message for you to get"

covert_message = "secret" + "EOF"
covert_bin = ""

# convert to binary
for i in covert_message:
    covert_bin += bin(ord(i))[2:].zfill(8)
#print(covert_bin)
    
j = 0
for i in msg:
    c.send(i.encode())
    if covert_bin[j] == None:
        pass
    else:
        if covert_bin[j] == "0":
            sleep(0.5)
        else:
            sleep(0.25)
    j += 1

c.send("EOF".encode())
print("Message sent...")

c.close()
