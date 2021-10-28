import sys

SENTINEL = [0x0, 0xff, 0x0, 0x0, 0xff, 0x0]

#mode is eitehr storing or retrieving
mode = str(sys.argv[1])
#method is eitehr bit or byte
method = str(sys.argv[2])

#set by default to these values, but if user specified somethign else
#they would be chnaged to that as is appropriate
offset = 0
interval = 1

#here is the changing of offset or interval, if a value si actually given
#if no value is given, they will remain at their default values
try:
	#if the 3 and 4 arguments are integers, than they are 
	#teh offset and interval values and the 5 and 6 should be 
	#the files, otherwise, they are
	#either a mistake or teh files we need
	offset = int(sys.argv[3])
	interval = int(sys.argv[4])
	
	wrapper_file = sys.argv[5]
	hidden_file = sys.argv[6]
except:
	wrapper_file = sys.argv[3]
	hidden_file = sys.argv[4]


#each function follows the pseudo code he put up 
#for the steg pdf

#remaining comments of pseudo codes are where I am not
#sure exactly what to do as of this moment
def byte_method():
	if mode == "-s":
		#he said to use bytearray to do this part but I am not quite sure how
		#he means to use it
		#W <-- wrapper bytes
		#H <-- hidden bytes
		
		i = 0
		while i < len[H]:
			W[offset] = H[i]
			offset += interval
			i += 1
		
		i = 0
		while i < len[SENTINEL]:
			W[offset] = SENTINEL[i]
			offset += interval
			
			i += 1
	elif mode == "-r":
		#W <-- wrapper bytes
		#H <-- empty byte array
		
		while offset < length(W):
			b = W[offset]
			
			# check if b matches a sentinel byte
			# if so, we need to check further
			# if not, we can add this byte to H
			# but we may need to add matched partial sentinel bytes first!
			# afterwards...
			
			H += b
			offset += interval
	else:
		#this si just to make sure the user chooses either storage or retrevial
		print("please choose -s for storage or -r for retreival")
		

		
def bit_method():
	if mode == "-s":
		#W <-- wrapper bytes
		#H <-- hidden bytes
		
		i = 0
		while i < len[H]:
			for(j=0, j<8, j++):
				W[offset] & 11111110
				W[offset] | ((H[i] & 10000000) >> 7)
				H[i] = (H[i] << 1) & (2 ** 8-1)
				offset += interval
			
			i += 1
		
		i = 0
		while i < len[SENTINEL]:
			for(j=0, j<8, j++):
				W[offset] & 11111110
				W[offset] | ((SENTINEL[i] & 10000000) >> 7)
				SENTINEL[i] << (SENTINEL[i] << 1) & (2 ** 8-1)
				offset += interval
			
			i += 1
		
	elif mode == "-r":
		#W <-- wrapper bytes
		#H <-- empty byte array
		
		while offset < len[W]:
			b = 0
			
			for(j=0, j<8, j++):
				b | (W[offset] & 00000001)
				if j < 7:
					b = (b << 1) & (2 ** 8-1)
					offset += interval
			
			# check if b matches a sentinel byte
			# if so, we need to check further
			# if not, we can add this byte to H
			#but we may need to add matched partial sentinel bytes first!
			# afterwards...
			
			H += b
			offset += interval
		
		else:
			print("please choose -s for storage or -r for retreival")
		
		
###################################################################################################################
if method == "-b":
	bit_method()
elif method == "-B":
	byte_method()
