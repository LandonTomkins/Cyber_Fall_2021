# use Python 3
  
from ftplib import FTP

# FTP server details
IP = "138.47.157.5"
PORT = 21
USER = "anonymous"
PASSWORD = ""
FOLDER = "/10/"
USE_PASSIVE = True # set to False if the connection times out
METHOD = 10

# connect and login to the FTP server
ftp = FTP()
ftp.connect(IP, PORT)
ftp.login(USER, PASSWORD)
ftp.set_pasv(USE_PASSIVE)

# navigate to the specified directory and list files
ftp.cwd(FOLDER)
files = []
file_perms = []
message = ""
ftp.dir(files.append)

# exit the FTP server
ftp.quit()

def ten_bit():
    perm_string = ""
    bin_input = []
    for f in files:
        perm_string+=f[0:10]
    for char in perm_string:
        bin_string = ""
        if char == "-":
            bin_string+="0"
        else:
            bin_string+="1"
    for i in range(0, len(bin_string), 7):
        bin_input.append(bin_string[i:i+7])
    for s in bin_input:
        message += chr(int(s,2))
    print(message)


def seven_bit():
    for f in files:
        if f[0:3] == "---":
            file_perms.append(f[3:10])
    for s in file_perms:
        bin_string = ""
        for char in s:
            if char == "-":
                bin_string+="0"
            else:
                bin_string+="1"
        message+=chr(int(bin_string,2))
    print(message)

if METHOD == 7:
    seven_bit()
if METHOD == 10:
    ten_bit()

