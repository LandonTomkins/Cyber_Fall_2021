##################################################
# The Magicians
#
# Program Description:
#   This program decrypts a hidden mesage/image from a wrapper file using hidden bits/bytes within wrapper.
# The user specifies byte (-B) or bit (-b) mode and storage (-s) or retireval (-r) mode along with the offset (-o)
# and the interval (-i). However, if the interval is not specified in the bit method it is set to 1 by default.
# The wrapper file (-w) and the hidden file (-h) must be specified for encryption, but only the wrapper is needed
# for decryption. Once the program has recorded all of the command line arguments, it either stores the hidden bits
# or bytes within another file along with the sentinel bytes, or it retireves the hidden bits or bytes until it detects
# the sentinel bytes. Then, the encrypted or decrypted data is redirected to an output file through stdout.
##################################################

import sys

# detects bit or byte method
method = str(sys.argv[2])

######################### Byte Method #########################

def byte_method():

    # detects storage or retrieval mode
    mode = str(sys.argv[1])

    # detects the offset and interval
    offset = int(sys.argv[3][2:])
    interval = int(sys.argv[4][2:])

    # creates a sentinel byte list 
    sList = [0x0, 0xff, 0x0, 0x0, 0xff, 0x0]
    SENTINEL = bytearray(sList)

    # storage mode that stores hidden bytes within a file
    if mode == "-s":

        # puts the wrapper and hidden files into byte arrays
        try:
            file = open(sys.argv[5][2:], "rb")
        except FileNotFoundError:
            sys.stderr.write("Wrapper file not found.")
            exit()
            
        W = bytearray(file.read())
        file.close()

        try:
            file = open(sys.argv[6][2:], "rb")
        except FileNotFoundError:
            sys.stderr.write("Hidden file not found.")
            exit()
            
        H = bytearray(file.read())
        file.close()

        # stores the bytes of the hidden file along with the sentinel bytes
        i = 0
        while i < len(H):
            W[offset] = H[i]
            offset += interval
            i += 1
          
        i = 0
        while i < len(SENTINEL):
            W[offset] = SENTINEL[i]
            offset += interval
            i += 1
            
        sys.stdout.buffer.write(W)

    # retrieval mode that retrieves hidden bytes within a file
    elif mode == "-r":

        # puts the wrapper file into a byte array and creates an empty byte array for the hidden file
        try:
            file = open(sys.argv[5][2:], "rb")
        except FileNotFoundError:
            sys.stderr.write("Wrapper file not found.")
            exit()
        
        W = bytearray(file.read())
        file.close()
        H = bytearray()

        # puts the hidden bytes into the hidden file until the sentinel bytes are detected
        bytecount = 0
        while offset < len(W):
            b = W[offset]
            if b == SENTINEL[bytecount]:
                bytecount += 1
                if bytecount ==  len(SENTINEL):
                    H = H[:len(H) - (len(SENTINEL)-1)]
                    sys.stdout.buffer.write(H)
                    break
                              
            else:
                bytecount = 0
                
            H.append(b)
            offset += interval

######################### Bit Method #########################

def bit_method():

    # detects storage or retrieval mode
    mode = str(sys.argv[1])

    # detects the offset and the interval (if no interval is given, it is 1 by default)                         
    offset = int(sys.argv[3][2:])
    if sys.argv[4][:2] != "-i":
        interval = 1
    else:
        interval = int(sys.argv[4][2:])

    # creates a sentinel byte list 
    sList = [0x0, 0xff, 0x0, 0x0, 0xff, 0x0]
    SENTINEL = bytearray(sList)

     # storage mode that stores hidden bits within a file
    if mode == "-s":

        # puts the wrapper and hidden files into byte arrays
        if sys.argv[4][:2] != "-i":
            x = 4
            y = 5
        else:
            x = 5
            y = 6
            
        try:
            file = open(sys.argv[x][2:], "rb")
        except FileNotFoundError:
            sys.stderr.write("Wrapper file not found.")
            exit()
            
        W = bytearray(file.read())
        file.close()

        try:
            file = open(sys.argv[y][2:], "rb")
        except FileNotFoundError:
            sys.stderr.write("Hidden file not found.")
            exit()
            
        H = bytearray(file.read())
        file.close()

        # stores the bits of the hidden file along with the sentinel bits
        i = 0
        while i < len(H):
            for j in range(8):
                W[offset] &= 0b11111110
                W[offset] |= ((H[i] & 0b10000000) >> 7)
                H[i] = (H[i] << 1) & (2 ** 8 - 1)
                offset += interval   
            i += 1

        i = 0
        while i < len(SENTINEL):
            for j in range(8):
                W[offset] &= 0b11111110
                W[offset] |= ((SENTINEL[i] & 0b10000000) >> 7)
                SENTINEL[i] = (SENTINEL[i] << 1) & (2 ** 8 - 1)
                offset += interval   
            i += 1
            
        sys.stdout.buffer.write(W)

    # retrieval mode that retrieves hidden bits within a file
    elif mode == "-r":

        # puts the wrapper file into a byte array and creates an empty byte array for the hidden file
        if sys.argv[4][:2] != "-i":
            try:
                file = open(sys.argv[4][2:], "rb")
            except FileNotFoundError:
                sys.stderr.write("Wrapper file not found.")
                exit()
        else:
            try:
                file = open(sys.argv[5][2:], "rb")
            except FileNotFoundError:
                sys.stderr.write("Wrapper file not found.")
                exit()
            
        W = bytearray(file.read())
        file.close()
        H = bytearray()

        # puts the hidden bits into the hidden file until the sentinel bytes are detected
        bytecount = 0  
        while offset < len(W): #len(W) - offset -  1 >= 0
            b = 0
            for j in range(8):
                b |= (W[offset] & 0b00000001) #(W[len(W) - offset - 1] & 0b00000001)
                if j < 7:
                    b = (b << 1) & (2 ** 8 - 1)
                    offset += interval
                    
            if b == SENTINEL[bytecount]:
                bytecount += 1
                if bytecount ==  len(SENTINEL):
                    H = H[:len(H) - (len(SENTINEL)-1)]
                    sys.stdout.buffer.write(H)
                    break
                              
            else:
                bytecount = 0
                
            H.append(b)
            offset += interval
            
###########################################################################                        

# runs bit or byte method depending on method specified
if method == "-B":
    byte_method()
if method == "-b":
    bit_method()


