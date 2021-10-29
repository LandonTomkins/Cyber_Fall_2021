import sys

method = str(sys.argv[2])

def byte_method():
    mode = str(sys.argv[1])

    offset = int(sys.argv[3][2:])
    interval = int(sys.argv[4][2:])

    sList = [0x0, 0xff, 0x0, 0x0, 0xff, 0x0]
    SENTINEL = bytearray(sList)
    
    if mode == "-s":
        file = open(sys.argv[5][2:], "rb")
        W = bytearray(file.read())
        file.close()

        file = open(sys.argv[6][2:], "rb")
        H = bytearray(file.read())
        file.close()
        
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

    elif mode == "-r":
        file = open(sys.argv[5][2:], "rb")
        W = bytearray(file.read())
        file.close()
        H = bytearray()

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
                bytecount == 0
                
            H.append(b)
            offset += interval

###########################################################################

def bit_method():
    mode = str(sys.argv[1])

    offset = int(sys.argv[3][2:])
    interval = 1

    sList = [0x0, 0xff, 0x0, 0x0, 0xff, 0x0]
    SENTINEL = bytearray(sList)

    if mode == "-s":
        file = open(sys.argv[4][2:], "rb")
        W = bytearray(file.read())
        file.close()

        file = open(sys.argv[5][2:], "rb")
        H = bytearray(file.read())
        file.close()
        
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

    elif mode == "-r":
        file = open(sys.argv[4][2:], "rb")
        W = bytearray(file.read())
        file.close()
        H = bytearray()
        
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
                bytecount == 0
                
            H.append(b)
            offset += interval
            
###########################################################################                        

if method == "-B":
    byte_method()
if method == "-b":
    bit_method()


