import string

num_to_letter = dict(zip(range(0, 27), string.ascii_lowercase))

def key_sizing(message, key):
    #whole section is to check teh length of the key and make it as long as the message
    key_len = 0
    key_index = 0
    key_list = []
    #while the key is shorter than the message, we have to make it longer to match
    while key_len < len(message):
        #for each character in the key we check to see if 
        for char in key:
            if char in string.ascii_letters:
                if key_len < len(message):
                    key_list.append(str(char))
                    key_len += 1
            else:
                key_index += 1

    return key_list

def symbol_handiling(text):
    text_len = 0
    #symbol_buffer = 0
    
    symbols = {}
    #print(len(text))
    while text_len < len(text):
        for char in text:
            if char not in string.ascii_letters:
                symbols[text_len] = str(char)
                text_len += 1
                #symbol_buffer += 1
            else:
                text_len += 1

    return symbols

#############################################################################################
def vin_decode(cypherText, key):
    #this is a variable that I will use later
    i = 0
    symbol_buffer = 0
    
    #calls key_sizing to make the key as long as the cypherText
    key_list = key_sizing(cypherText, key)
    #print(key_list)
    #creates a list to hold the cypherText in
    cyph_list = []
    cyph_len = 0
    #adds the text to the aforementioned list
    symb_list = symbol_handiling(cypherText)
    for char in cypherText:
            if char in string.ascii_letters:
                if cyph_len < len(cypherText):
                    cyph_list.append(str(char))
                    cyph_len += 1
            else:
                cyph_len += 1

    #print(cyph_list)

    #this is where the actual decoding come from
    while i < len(cyph_list):
        #our current letter we are seeking to decipher is equal to that mathmatic thing to break the sypher
        message_num = (26 + (ord(cyph_list[i]) - 96) - (ord(key_list[i]) - 96)) % 26

        #print each letter of the sypher, with the end there to make it so that each letter is printed on teh same line
        #as the last letter printed to the screen
        if (i + symbol_buffer) in symb_list:
            print(symb_list[i + symbol_buffer], end='')
            if (i + 1 + symbol_buffer) in symb_list:
                print(symb_list[i + 1 + symbol_buffer], end='')
                print(num_to_letter[int(message_num)], end='')
                symbol_buffer += 2
                i += 1
            else:
                print(num_to_letter[int(message_num)], end='')
                symbol_buffer += 1
                i += 1
                
        else:
                print(num_to_letter[int(message_num)], end='')
                i += 1
    print(' ')


def vin_encode(plainText, key):
    #this is a variable that I will use later
    i = 0
    symbol_buffer = 0
    
    #calls key_sizing to make the key as long as the cypherText
    key_list = key_sizing(plainText, key)
    #creates a list to hold the cypherText in
    mess_list = []
    mess_len = 0
    #adds the text to the aforementioned list
    symb_list = symbol_handiling(plainText)
    for char in plainText:
            if char in string.ascii_letters:
                if mess_len < len(plainText):
                    mess_list.append(str(char))
                    mess_len += 1
            else:
                mess_len += 1

    #this is where the actual decoding come from
    while i < len(mess_list):
        #our current letter we are seeking to decipher is equal to that mathmatic thing to break the sypher
        cypher_num = ((ord(mess_list[i]) - 97) + (ord(key_list[i]) - 97)) % 26
        #increment i to go to the next letter of teh cypher
        if (i + symbol_buffer) in symb_list:
            print(symb_list[i + symbol_buffer], end='')
            if (i + 1 + symbol_buffer) in symb_list:
                print(symb_list[i + 1 + symbol_buffer], end='')
                print(num_to_letter[int(cypher_num)], end='')
                symbol_buffer += 2
                i += 1
            else:
                print(num_to_letter[int(cypher_num)], end='')
                symbol_buffer += 1
                i += 1
                
        else:
                print(num_to_letter[int(cypher_num)], end='')
                i += 1

    #resets to a new line after each cypher is finished
    print('')
        

#vin_decode('Zlb jmspw psp Vfjwz Kfmbq! Ux’ym ywaze ds rnyv qwmd uyvjw bxkqvq byal hu Vgdwyzov 12!', 'This is my key')
#vin_encode('Get ready for Cyber Storm! We’re going to turn your world upside down on November 12!', 'This is my key')
