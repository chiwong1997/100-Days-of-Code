logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""

print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 
            'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 
            'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))

"""
Encrpyt Function 
    Take a string and return a string shifted by specified amount.

Parameters:
    plain_text: str
        The text string to be encrypted
    shift_amount: int
        The number of spaces in the alphabet to shift

Returns:
    cipher_text: str
        The encrpyted text string
"""
def encrypt(plain_text, shift_amount):
    cipher_list = []
    for letter in plain_text:
        current_index = alphabet.index(letter)
        cipher_index = current_index + shift_amount
        cipher_list.append(alphabet[cipher_index])

    cipher_text = ''.join(cipher_list)
    return print(cipher_text)

"""
Decrpyt Function 
    Take a string and return a string shifted by specified amount.

Parameters:
    cipher_text: str
        The text string to be decrypted
    shift_amount: int
        The number of spaces in the alphabet to shift

Returns:
    decipher_text: str
        The decrpyted text string
"""
def decrypt(cipher_text, shift_amount):
    decipher_list = []
    for letter in cipher_text:
        current_index = alphabet.index(letter)
        decipher_index = current_index - shift_amount
        decipher_list.append(alphabet[decipher_index])
    
    decipher_text = ''.join(decipher_list)
    return print(decipher_text)

"""
Caesar Function
    Take a string and return a string shifted by a specified amount. 

Parameters:
    text: str
        The text string to be encrypted or decrypted
    shift: int
        The number of spaces in the alphabet to shift
    direction: str
        Either "encode" or "decode"

Returns:
    txt: str
        The encrpyted or decrypted text string
"""
def caesar(text, shift, direction):
    shift = shift % 26
    valid_options= ["encode", "decode"]
    if direction not in valid_options:
        return print("Direction must be either encode or decode")
    lst = []
    for letter in text:
        if letter in alphabet:
            current_index = alphabet.index(letter)
            if direction == "encode":
                next_index = current_index + shift
            else:
                next_index = current_index - shift
            lst.append(alphabet[next_index])
        else:
            lst.append(letter)

    txt = ''.join(lst)
    return print(f"The {direction}d text is {txt}") 


# Encrypt or Decrypt Program
again = "yes"
while again == "yes":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text,shift,direction)
    again = input("Do you want to go again? (yes/no)\n").lower()

print("Thanks for using the Caesar Cipher! Goodbye.")

# caesar(text,shift,direction)
# again = input("Do you want to go again? (yes/no)\n").lower()


# if direction == "encode":
#     encrypt(plain_text=text, shift_amount=shift)
# elif direction == "decode":
#     decrypt(cipher_text=text, shift_amount=shift)
# else:
#     print("Not valid, can only encode or decode.")