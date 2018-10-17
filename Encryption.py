

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
89
90
91
92
93
94
95
96
97
98
99
100
101
102
103
104
105
106
107
108
109
110
111
112
113
114
115
116
117
118
119
120
121
122
123
124
125
126
127
128
129
130
131
132
133
134
135

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
    newstring = ""
    currentpos = 0
    added = 0
    print(len(key))
    for character in string:
        print (currentpos, key[currentpos])
        """Logic: if key[currentpos] < log(1), just add key[currentpos] to character ascii code (probably will never happen).
                if key[currentpos] > log(n), add ceil(log(n)) characters in front of character, add ceil(log(key,10))to ascii code of character. n will be limited to 30. """
        if (key[currentpos] == 0):
            newstring += chr(ord(character)+key[currentpos])
        else:
            if (math.log(key[currentpos]) < math.log(1)):
                newstring += chr(ord(character)+key[currentpos])
                
            elif (math.log(key[currentpos]) >= math.log(1)) and (math.log(key[currentpos]) < math.log(100)):
                newstring += chr(ord(character)+math.ceil(math.log(key[currentpos],10)))
                while (added < math.ceil(math.log(1))):
                    newstring += chr(random.randint(0,127))
                    added += 1
                added = 0
                                 
            elif (math.log(key[currentpos]) >= math.log(100)) and (math.log(key[currentpos]) < math.log(1000)):
                newstring += chr(ord(character)+math.ceil(math.log(key[currentpos],10)))
                while (added < math.ceil(math.log(100))):
                    newstring += chr(random.randint(0,127))
                    added +=1
                added = 0
                    
            elif (math.log(key[currentpos]) >= math.log(1000)) and (math.log(key[currentpos]) < math.log(10000)):
                newstring += chr(ord(character)+math.ceil(math.log(key[currentpos],10)))
                while (added < math.ceil(math.log(10000))):
                    newstring += chr(random.randint(0,127))
                    added +=1
                added = 0
            else:
                newstring += chr(ord(character)+math.ceil(math.log(key[currentpos],10)))
                             
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

phrase = "Test Phrase for my very unsafe and very basic encrypting machine.\nThis is a newline"
print (phrase)
encrypted = Encrypt(phrase)
print (encrypted)
salted = Salt(encrypted)
print (salted)
decrypted = Decrypt(encrypted)
print (decrypted)

