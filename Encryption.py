####
##Ugly Python encrypter to waste time.
##Idea is UUDDLRLRABS
## Up = +1
## Down = -1
## Right = +10
## Left = -10
## A = +65
## B = +66
## Start = Switch Case
## Temporary salting for now
####

import os
import math
import random
from string import ascii_lowercase


def generate_key(seed):
    return os.urandom(seed)

def Encrypt(string):
    counter = 0
    newstring = ""
    for i in string:
        if (counter == 0 or counter == 1):
            newstring += chr(ord(i) + 1)
            counter += 1
        elif(counter==2 or counter ==3):
            newstring += chr(ord(i) - 1)
            counter += 1
        elif(counter ==4 or counter ==6):
            newstring += chr(ord(i) - 10)
            counter += 1
        elif (counter ==5 or counter ==7):
            newstring += chr(ord(i) + 10)
            counter += 1
        elif (counter == 8):
            newstring += chr(ord(i) + 65)
            counter += 1
        elif (counter == 9):
            newstring += chr(ord(i) + 66)
            counter += 1
        elif (counter == 10):
            if i.isupper():
                newstring += i.lower()
            else:
                newstring += i.upper()
            counter = 0
    return newstring
def Salt(string):
    key = generate_key(os.urandom(8)[0])
    print (key)
    newstring = ""
    currentpos = 0
    addto = ""
    print(len(key))
    i=0
    for character in string:
        print (i)
        """Logic: if key[currentpos] < log(1), just add key[currentpos] to character ascii code (probably will never happen).
                if key[currentpos] > log(n), add ceil(log(n)) characters in front of character, add ceil(log(key,10))to ascii code of character. n will be limited to 30. """
        if (key[currentpos] == 0):
            newstring += chr(ord(character)+key[currentpos])
            i+=1
        else:
            if (math.log(key[currentpos]) < math.log(1)):
                newstring += chr(ord(character)+key[currentpos])
                i+=1
                
            elif (math.log(key[currentpos]) >= math.log(1)) and (math.log(key[currentpos]) < math.log(100)):
                newstring += chr(ord(character)+math.ceil(math.log(key[currentpos],10)))
                for i in range (2):
                    addto +=(random.choice(ascii_lowercase))
                newstring += addto
                i+=2
                                 
            elif (math.log(key[currentpos]) >= math.log(100)) and (math.log(key[currentpos]) < math.log(1000)):
                newstring += chr(ord(character)+math.ceil(math.log(key[currentpos],10)))
                for i in range (3):
                    addto +=(random.choice(ascii_lowercase))
                    newstring += addto
                i+=3
                    
            elif (math.log(key[currentpos]) >= math.log(1000)) and (math.log(key[currentpos]) < math.log(10000)):
                newstring += chr(ord(character)+math.ceil(math.log(key[currentpos],10)))
                for i in range (4):
                    addto +=(random.choice(ascii_lowercase))
                    newstring += addto
                i+=4
            else:
                newstring += chr(ord(character)+math.ceil(math.log(key[currentpos],10)))
                i+=1
                             
        if currentpos < (len(key)-1):
            currentpos += 1
        else:
            currentpos = 0
    return newstring, key
    
def Unsalt(string, key):
    newstring = ""
    currentpos = 0
    i=0
    while (i <= len(string)-1):
        print (i)
        """Logic: if key[currentpos] < log(1), just add key[currentpos] to character ascii code (probably will never happen).
            if key[currentpos] > log(n), add ceil(log(n)) characters in front of character, add ceil(log(key,10))to ascii code of character. n will be limited to 30. """
        if (key[currentpos] == 0):
            newstring += chr(ord(string[i])-key[currentpos])
        else:
            if (math.log(key[currentpos]) < math.log(1)):
                newstring += chr(ord(string[i])-key[currentpos])
            elif (math.log(key[currentpos]) >= math.log(1)) and (math.log(key[currentpos]) < math.log(100)):
                newstring += chr(ord(string[i])-math.ceil(math.log(key[currentpos],10)))
                i += 2
                                 
            elif (math.log(key[currentpos]) >= math.log(100)) and (math.log(key[currentpos]) < math.log(1000)):
                newstring += chr(ord(string[i])-math.ceil(math.log(key[currentpos],10)))
                i += 3
                    
            elif (math.log(key[currentpos]) >= math.log(1000)) and (math.log(key[currentpos]) < math.log(10000)):
                newstring += chr(ord(string[i])-math.ceil(math.log(key[currentpos],10)))
                i += 4
            else:
                newstring += chr(ord(string[i])-math.ceil(math.log(key[currentpos],10)))
        i += 1
        if currentpos < (len(key)-1):
            currentpos += 1
        else:
            currentpos = 0
    return newstring

def Decrypt(string):
    counter = 0
    newstring = ""
    for i in string:
        if (counter == 0 or counter == 1):
            newstring += chr(ord(i) - 1)
            counter += 1
        elif(counter==2 or counter ==3):
            newstring += chr(ord(i) + 1)
            counter += 1
        elif(counter ==4 or counter ==6):
            newstring += chr(ord(i) + 10)
            counter += 1
        elif (counter ==5 or counter ==7):
            newstring += chr(ord(i) - 10)
            counter += 1
        elif (counter == 8):
            newstring += chr(ord(i) - 65)
            counter += 1
        elif (counter == 9):
            newstring += chr(ord(i) - 66)
            counter += 1
        elif (counter == 10):
            if i.isupper():
                newstring += i.lower()
            else:
                newstring += i.upper()
            counter = 0
    return newstring

phrase = input("Insert Phrase here: ")
print (phrase)
encrypted = Encrypt(phrase)
print (encrypted)
salted, key = Salt(encrypted)
print (salted)
print (key)
unsalted = Unsalt(salted,key)
print (unsalted)
decrypted = Decrypt(unsalted)
print (decrypted)

