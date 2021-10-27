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

