##################################################
# The Magicians
#
# Program Description:
#   This program opens the key file, reads it, and turns it into a byte array.
# Then the ciphertext or plaintext file from the stdin is also converted to a 
# byte array. Lastly, an output byte array is appended with each ciphertext byte 
# xored with the corresponding key byte to get the decrypted output or encrypted input.
##################################################
import sys

# reads key file and converts to byte array
file = open("key", "rb")
key = bytearray(file.read())
file.close()

# reads ciphertext file and converts to byte array
ciphertext = bytearray(sys.stdin.buffer.read())

output = bytearray()

# does xor operaton on each value of the ciphertext
for i in range(len(ciphertext)):
    output.append(ciphertext[i] ^ key[i])

sys.stdout.buffer.write(output)

