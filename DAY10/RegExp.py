#Regular Expression
#is python is a pure object oriented programming language?
#No, python is not a pure object oriented programming language because it supports procedural programming as well
'''
import re #re module for performing all the regular expression based operation
count = 0 #to count the number of matching found
pattern = re.compile("function") #string converts into bytecode

matcher = pattern.finditer("A function in python is defined by a def statement. python The general syntax looks like this: def function-name(Parameter list): statements, i.e. the function body. The parameter python list consists of none or more parameters.")

for i in matcher:
    count += 1
    print(i.start(),"....",i.end(),".....",i.group())
print("The number of occurance : ",count)
'''

#=========================================================================================
'''
import re
count = 0
matcher = re.finditer("Hi","HiHiHiHi")
for i in matcher:# loop 4 times execute HiHiHiHi
    count += 1
    print(i.start(),"....",i.end(),".....",i.group())
print("The number of occurance : ",count)
'''

#=========================================================================================
'''
import re

obj = input("enter any charecter : ")   

objmatch = re.finditer(obj, "a7b @k9z")

# print(objmatch)

for match in objmatch:
    print(match.start(), "...", match.end(), "...", match.group())
'''
#=========================================================================================

'''
Match character classes

By using this character classes we match the group of characters

[abc]      ==> Either a or b or c

[^abc]     ==> Except a and b and c

[a-z]      ==> Any lower case alphabet symbol

[A-Z]      ==> Any upper case alphabet symbol

[a-zA-Z]   ==> Any alphabet symbol

[0-9]      ==> Any digit from 0 to 9

[a-zA-Z0-9] ==> Any alphanumeric character

[^a-zA-Z0-9] ==> Except alphanumeric characters (Special Characters)


Inbuilt character classes

\s  => Space character

\S  => Any character except space character

\d  => Any digit from 0 to 9

\D  => Any character except digit

\w  => Any word character [a-zA-Z0-9]

\W  => Any character except word character (Special Characters)

.   => Any character including special characters


match() function

For performing match operation we need string, this match function used to match the given pattern to starting or beginning of the string. 
If match is done then we will get match object else we will get None.

fullmatch()

As a name suggest when we have to match full string with the given pattern then we have to
 use fullmatch() function. If match is done then we will get match object else we will get
 None.
'''

#=========================================================================================
'''
import re

a = input("Enter string to perform match operation : ")

mtch = re.match(a, "python is very important language")

print(mtch)

if mtch != None:
    print("match found at begining level")
    print(mtch.start(), " ", mtch.end())

else:
    print("there is no matching at begining level")

'''
#=========================================================================================

'''
import re

a = input("Enter string to perform match operation : ")

mtch = re.fullmatch(a, "pythonisvery")

print(mtch)

if mtch != None:
    print("match found at begining level")
    print(mtch.start(), " ", mtch.end())

else:
    print("there is no matching at begining level")
'''
#=========================================================================================
'''
#Write a program to check whether the given mail valid or not?
import re
s = input("Enter mail id : ")
m = re.fullmatch("\w[a-zA-Z0-9_.]*@rbunagpur[.]in", s)
if m != None:
    print("Vaild mail id")
else:
    print("Invalid mail id")
'''
#=========================================================================================
'''
# Write a program to check whether the given mobile number is valid or not?
import re
mo = input("ENter the mobile no.")
obj = re.fullmatch("[0-5]\\d{9}",mo)
if obj != None:
    print("Valid Mobile Number")
else:
    print("Invalid mobile number")
'''

#=========================================================================================

# search() function
'''
import re

a = input("enter string to perform match operation : ")

mtch = re.search(a, "python sss dynamic lannn")

print(mtch)

if mtch != None:
    print(mtch.start(), " ", mtch.end(), " ", mtch.group())

else:
    print("there is no matching anywhere")
'''

#=========================================================================================
'''
import re
mtch = re.findall('[A-Z]',"abj3ndk5ndfdo8@#$%^&*()_+")
print(mtch)
'''

#=========================================================================================

#Sub Function()
'''
import re
obj = re.sub('[a-z]','*','2345 ABCD habc deff')
print(obj)
'''

#=========================================================================================
#subn Function()
'''
import re
obj = re.subn('[0-7]','@','ab3gd6nk17')# substitute n function return the number of string
print(obj)
print("The string is = ",obj[0])
print("The number of replacement is = ",obj[1])

'''

#To search a word in a file
'''
import re
a= input("Enter a word to perform search operation : ")
f1 = open("paragraph.txt", "r")
data = f1.read()
mtch = re.search(a, data)
print(mtch)
if mtch != None:
    print(mtch.start(), " ", mtch.end(), " ", mtch.group())
else:
    print("There is no matching anywhere")
'''

# Program to print the number of lines, words and characters
# present in the given file

import os
import sys

fname = input("Enter File Name: ")

if os.path.isfile(fname):
    print("File exists:", fname)

    f = open(fname, "r")

else:
    print("File does not exist:", fname)
    sys.exit(0)

lcount = wcount = ccount = 0

for line in f:
    lcount = lcount + 1
    ccount = ccount + len(line)

    words = line.split()
    wcount = wcount + len(words)

print("The number of Lines:", lcount)
print("The number of Words:", wcount)
print("The number of Characters:", ccount)