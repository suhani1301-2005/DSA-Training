'''
name = "SuhaniSaxena"
print(name[0]) #s
print(name[1]) #u
print(name[-1]) #a
#print(name[15])
print(name[0:5])#Suhani
print(name[1:])#Saxena
print(name[:5])
print(name[:])#SuhaniSaxena
print(name[1:8:2])#uhnS
print(name[::-1])#anexaSinahS
'''

#========================================================================================

'''
s = "Python are High level programming language"
print(s.lower())#python are high level programming language
print(s.upper())#PYTHON ARE HIGH LEVEL PROGRAMMING LANGUAGE
print(s.title())#Python Are High Level Programming Language
print(s.swapcase())#pYTHON ARE hIGH LEVEL PROGRAMMING LANGUAGE
print(s.capitalize())#Python are high level programming language
'''

#========================================================================================

'''
name = "Suhani"
sal = 3000000
age = 21
print("{} sal is {} and age is {}".format(name,sal,age))#Suhani sal is 3000000 and age is 21
print("{0} sal is {1} and age is {2}".format(name,sal,age))#Suhani sal is 3000000 and age is 21
print("{x} sal is {y} and age is {z}".format(x=name,y=sal,z=age))#Suhani sal is 3000000 and age is 21
A=1
print(f"{A} is a good boy")
'''

#========================================================================================

#WAP to remove duplicate
'''
name = "SuhaniSaxena"
newname =" "
for i in name:
    if i not in newname:
        newname += i
print(newname)
'''
#reverse logic

'''
name = "SuhaniSaxena"
newname =" "
N = len(name)
for i in range(N-1 , -1 , -1):
        newname += name[i]
print(newname)
'''
#========================================================================================
   
                                            #Palindrome 
'''
name = "racecar"
#name = "help4code"
print(name)
print(name[ ::-1])
if name == name[::-1]:
    print("Palindrome")
else:
    print("Not palindrome")
'''

#========================================================================================
   
                                            #Count Vowels and Consonents 

"""
vowels = ['a','e','i','o','u' ,'A' , 'E','I' , 'O' , 'U']
Word = input()
cons=0
vow=0
for i in Word:
    if i in vowels:
        vow += 1
    else:
        cons += 1
print(cons)
print(vow)

"""

#========================================================================================
   
                                            #Anagram 
# sample input: "listen" and "silent"
# Output : Anagram
"""
name = "racecar"
"""

#========================================================================================
   
                                            #Count a word in a StriNG
#input: This is a sentence
#output: 4

'''
sentence="This is a sentence"
sen = 0
for i in sentence:
    if i==" ":
        sen += 1
print(sen+1)      

'''         

#========================================================================================
   
#MCQ

'''
a=50
b=30
c=20
d=10
print((a+b)*c/d)
print((a-b)*(c/d))
print(a+(b*c)/d)
'''
#========================================================================================

#Count speciaal character and whitespace in a string

"""
word = ord(input())
for i in word:
    if chr >= 65 and chr <= 90:
        print("Upper case")
    elif chr >= 97 and chr <= 122:
        print("Lower case")
    elif chr >= 48 and chr <= 57:
        print("Digit")
    else:
        print("Special Character")

var = 'jdsw8732@ij&kj#'
count=0

z=ord(i)
print(z)

if z>=97 and z<=122:
    continue
elif z>=48 and z<=57:
    continue
"""
#========================================================================================

#WAP to convert the first letter of each word to uppercase in a sentence

"""
sentence = input()
print(sentence.title())
"""

#========================================================================================
"""
print('suhanisaxena111'.isalnum())
print('suhanisaxena111'.isalpha())
print('777f'.isdigit())
print('sdfsed'.islower())
print(''.islower())
print('SUHANIs'.isupper())
print('My Name Is Suhani'.istitle())
print(''.istitle())
print(''.isspace())
print("Hello".startswith("He"))
print("Hello".endswith("lo"))

print("Suhnai".find("p"))
print("Suhnai".index("p"))
print("Suhani Saxena ".count("a"))

"""

#========================================================================================
#pattern 

# 1 1 1
# 2 2 2
# 3 3 3

'''
for i in range(1,4):
    for j in range(1,4):
        print(i,end=" ")
    print()
'''

#2]
# A A A A A 
# B B B B B 
# C C C C C 
# D D D D D 
# E E E E E

'''
n= int(input("Enter the number of rows: "))
for i in range (1,n+1):
    for j in range(1,n+1):
        print(chr(64+i),end=" ")
    print()
'''

#3]
# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
'''
n= int(input("Enter the number of rows: "))
for i in range (1,n+1):
    for j in range(1,1+i):
        print("*",end=" ")
    print()
''' 

#4]
# A A A A A 
# B B B B 
# C C C 
# D D 
# E 
'''
n= int(input("Enter the number of rows: "))
for i in range (1,n+1):
    for j in range(1,n+2-i):
        print(chr(64+i),end=" ")
    print()
'''

#5]
#      * 
#     * * 
#    * * * 
#   * * * * 
#  * * * * * 
import time
n= int(input("Enter the number of rows: "))
for i in range (1,n+1):
    print(" "*(n-i),end=" ")
    for j in range(1, i+1):
        time.sleep(3)
        print("*",end=" ")
    print()

#========================================================================================

#Question: Given an array, return an array where each element is the
#  prodect of all the elements in the aarray except itself
#sample input: [1,2,3,4]
"""
list=[]
for i in range(1,n-1):
    for j in range(1,n-1):
"""