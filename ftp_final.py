# use Python 3
# TEAM NAME: the magician
# DESCRIPTION: The code logs into the the local ftp server and retrieves the file permissions 
# converts the permissions into binary and decodes that into a message

from ftplib import FTP

# FTP server details
IP = "138.47.157.5"
PORT = 21
USER = "anonymous"
PASSWORD = ""
FOLDER = "/7/"
USE_PASSIVE = True # set to False if the connection times out
METHOD = 7

# connect and login to the FTP server
ftp = FTP()
ftp.connect(IP, PORT)
ftp.login(USER, PASSWORD)
ftp.set_pasv(USE_PASSIVE)

# navigate to the specified directory and list files
ftp.cwd(FOLDER)
files = []
file_perms = []
ftp.dir(files.append)

# exit the FTP server
ftp.quit()

# method if we are using all 10 bits of the permissions
def ten_bit():

    perm_string = ""
    bin_string = ""
    message = ""
    bin_input = []

    # combine all permissions into a single string
    for f in files:
        perm_string+=f[0:10]

    # convert the permissions string into a binary string
    for char in perm_string:
        if char == "-":
            bin_string+="0"
        else:
            bin_string+="1"

    # break the binary string into 7-bit binary strings
    for i in range(0, len(bin_string), 7):
        bin_input.append(bin_string[i:i+7])

    # convert the 7-bit binary strings into the corresponding ASCII characters
    # and add those characters to the final message
    for s in bin_input:
        message += chr(int(s,2))
    
    print(message)


def seven_bit():
    message = ""

    # clean the input and disregard the files which do not have "---" as the first
    # 3 permissions, then store the 7 relevant permissions from the valid files
    for f in files:
        if f[0:3] == "---":
            file_perms.append(f[3:10])

    # for every set of permissions make the corresponding 7-bit binary string
    for s in file_perms:
        bin_string = ""
        for char in s:
            if char == "-":
                bin_string+="0"
            else:
                bin_string+="1"

        # add the character corresponding to the binary string to the final message
        message+=chr(int(bin_string,2))

    print(message)

# calls the appropriate decryption method based on the METHOD variable
if METHOD == 7:
    seven_bit()
if METHOD == 10:
    ten_bit()

