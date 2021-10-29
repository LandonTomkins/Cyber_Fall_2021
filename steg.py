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


if method == "-B":
    byte_method()


