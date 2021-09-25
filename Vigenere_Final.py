import string
import sys

#Get the mode and the key for the cypher
mode = str(sys.argv[1])
given_key = str(sys.argv[2])

#continuously get input for decoding then send to be deciphered once the input is over
def decode():
    strings_to_decode = []
    message = ""
    while(True):
        try:
            message = str(input())
            strings_to_decode.append(str(message))
        except EOFError:   
            print_decoded_strings(strings_to_decode)
            break


#continuously get input for encoding then send to be encoded once the input is over
def encode():
    strings_to_encode = []
    message = ""
    while(True):
        try:
            message = str(input())
            strings_to_encode.append(str(message))
        except EOFError:   
            print_encoded_strings(strings_to_encode)
            break

#print all encoded input strings
def print_encoded_strings(strings_list):
    for string in strings_list:
        vin_encode(string, given_key)

#print all decoded input strings
def print_decoded_strings(strings_list):
    for string in strings_list:
        vin_decode(string, given_key)


#BLACK MAGIC BOX: DO NOT TOUCH OR YOU WILL ANGER THE BUG GODS
#####################################################################################################################

def key_sizing(message, key):
    num_nonalphas = 0
    for char in message:
        if not char.isalpha():
            num_nonalphas += 1
    key_len = 0
    key_index = 0
    key_list = []
    while key_len < (len(message) - num_nonalphas):
        if key[key_index % len(key)].isalpha():
            key_list.append(str(key[key_index % len(key)]).upper())
            key_len += 1
        key_index += 1
    return key_list

def vin_decode(cypherText, key):
    key_list = key_sizing(cypherText, key)
    cypher_text_list = list(cypherText)
    cypher_list_index = 0
    key_index = 0
    decoded_string = ""
    for char in cypher_text_list:
        if char.isalpha():
            if char.isupper():
                decoded_string += chr((ord(char) - 65 - ord(key_list[key_index]) - 65) % 26 + 65)
            else:
                decoded_string += chr((ord(char) - 97 - ord(key_list[key_index]) - 65) % 26 + 97)
            key_index += 1
            cypher_list_index += 1
        else:
            decoded_string += char
            cypher_list_index += 1
    print(decoded_string)

def vin_encode(plainText, key):
    key_list = key_sizing(plainText, key)
    plain_text_list = list(plainText)
    plain_list_index = 0
    key_index = 0
    encoded_string = ""
    for char in plain_text_list:
        if char.isalpha():
            if char.isupper():
                encoded_string += chr((ord(char) - 65 + ord(key_list[key_index]) - 65) % 26 + 65)
            else:
                encoded_string += chr((ord(char) - 97 + ord(key_list[key_index]) - 65) % 26 + 97)
            key_index += 1
            plain_list_index += 1
        else:
            encoded_string += char
            plain_list_index += 1
    print(encoded_string)

###########################################################################################################################

#select the mode based on the command prompt
if(mode == "-d"):
    decode()
elif(mode == "-e"):
    encode()





