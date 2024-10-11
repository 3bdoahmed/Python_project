import random # to genrate random password
import string # to use some methods of strings

def generatePassword(length): # func to generate password 
    if length < 6 : # must the length of password biger than 6
        return "pleasse Length should be at least 6."
    
    # use some methods of string to save char and digits and symbols 
    lowerchar = string.ascii_lowercase
    uperchar = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    # create an calcollation of char(uper and lower ) + digits + symbols
    all_char = lowerchar + uperchar + digits + symbols
    password = "" # var to save password the user enter

    # to chose random password form collection (all_char)
    for x in range(length):
        password += random.choice(all_char) # call methode choice from random
    return password # func return password is generate 

# ex at generated password.
len = int(input("please enter lenght of password you want: "))
print ("Generated Password: ", generatePassword(len))