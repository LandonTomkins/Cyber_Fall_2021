# takes stdin from the console
input1 = input()

x = 7
y = 8

bit7 = []
bit8 = []

string1 = ""
string2 = ""

# divides the input into 7 and 8 bit strings
for i in range(0, len(input1), x):
    bit7.append(input1[i:i+x])
for i in range(0, len(input1), y):
    bit8.append(input1[i:i+y])

# converts the binary to ascii 
for index in bit7:
    uni = int(index, 2)
    if(uni == 8):
        string1 = string1[:len(string1)-1]
        continue
    char = chr(uni)
    string1 = string1+char
for index in bit8:
    uni = int(index, 2)
    if(uni == 8):
        string2 = string2[:len(string2)-1]
        continue
    char = chr(uni)
    string2 = string2+char

# prints stdout to the console
print("7 Bit: ", string1)
print("\n8 Bit: ", string2)
