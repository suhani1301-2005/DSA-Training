#1]
'''
The garments company Apparel wishes to open outlets at various locations. 
The company shortlisted several plots in these locations and wishes to select only plots 
that are square-shaped.
Write an algorithm to help Apparel find the number of plots that it can select for its 
outlets.
Input:- 
The first line of the input consists of an integer numOfPlots, representing the number 
of plots shortlisted by the company for outlets (N).
The second line consists of N space-separated integers - area1, area2, .... , areaN 
representing the area of the N plots selected for outlets.
Output
Print an integer representing the number of plots that will be selected for outlets.
Input:- 8
         #79 77 54 81 48 34 25 16 
Output:- 3    
'''
list = []
numOfPlots = int(input("Enter the number of plots : "))
for i in range(numOfPlots): 
    area = int(input("Enter the area of plot : "))
    list.append(area)   
count = 0
for j in list:
    if j == int(j**0.5)**2:  # Check if the area is a perfect square
        count += 1

print(count)


#========================================================================================

#2]

# Write a Program to accept student name and marks from the keyboard and crerate a dictionary. Also
# display student marks by taking student name 
'''
n= int(input("ENter the number of students : "))
dict = {}
for i in range (n):
    name = input("Enter student Name : ")
    marks = int(input("ENter student marks : "))
    dict[name] = marks  #add key:value
while True:
    name = input("Enter student name to get the marks : ")
    marks = dict.get(name,-1) #if name is available in dict then it will return name if not it will return -1
    if marks == -1:
        print("Student Not Found")
    else:
        print("The marks of",name,"are",marks)
    option = input("Do you want to check anther student : ")
    if option == "No":
        break
print("Thanks for usimg our apllication")
'''
#========================================================================================

#3]Write a program to access each character of string in forward and backward 
# direction by using while loop?
#i/p = "Learning python is very easy"
'''
s = "Learning python is very easy"
n=len(s)
i = 0
print("Forward Direction")
while i<n:
    print(s[i],end=' ')
    i += 1
print()
print("Backword Direction")
i=-1
while i>=-n:
    print(s[i],end=' ')
    i=i-1

'''

#========================================================================================

#4]
# A company provides network encryption for secure data transfer. The data string is 
# encrypted prior to transmission and gets decrypted at the receiving end. 
# But due to some technical error, the encrypted data is lost and the received string is 
# different from the original string by 1 character. 
# Arnold, a network administrator, is tasked with finding the character that got lost in 
# the network so that the bug does not harm other data that is being transferred through the
# network.

# Write an algorithm to help Arnold find the character that was missing at the receiving 
# end but present at the sending end.

# Input

# The input consists of two space-separated strings — stringSent and stringRec, representing the string that was sent through the network and the string that was received at the receiving end of the network, respectively.

# Output
# #input:- abcdfgerj
# output:- j
'''
s = 'abcdfgerj'
r = 'abcdfger'

flag = False

for a, b in zip(s, r):
    if a != b:
        print(a)
        flag = True
        break

if not flag:
    print(s[-1])
'''
#========================================================================================

#5]
'''
v = ['a', 'e', 'i', 'o', 'u']
w = input("Enter the word where we will search the vowels :")
found = []
for i in w:
    if i in v:
        if i not in found:
            found.append(i)
print("Found Vowels : ", found)
print("Unique Vowels : ", len(found), 'from the given word = ', w)
'''

#========================================================================================
'''

A company wishes to provide cab service for their N employees. 
The employees have distance ranging from 0 to N-1. 
The company has calculated the total distance from an employee's residence to the company, 
considering the path to be followed by the cab is a straight path. 
The distance of the company from itself is 0. 
The distance for the employees who live to the left side of the company is represented 
with a negative sign. 
The distance for the employees who live to the right side of the company is represented 
with a positive sign. The cab will be allotted a range of distance.
 The company wishes to find the distance for the employees who live within the 
 particular distance range.

Write an algorithm to find the distance for the employees who live within the distance 
range.

Input

The first line of the input consists of three space-separated integers - num, start and end representing   
The size of the list (N), the starting value of the range, and the ending value of the range, respectively.

The second line of the input consists of N space-separated integers representing the distances of the employees from the company.

Output

Print the distances that lie within the given range.

Example

Input:
6 30 50
29 38 12 48 39 55
Output:
38 48 39 
'''
'''
num, start, end = map(int, input().split())
myList = []
for i in range(num):
    a = int(input())
    myList.append(a)

for j in myList:
    if j>=start and j <= end:
        print(j, end=' ')
'''

#========================================================================================

#dateTime Formating
'''
import datetime
now = datetime.datetime.now()
print("It's now : {:%d%m%Y %H:%M:%S}".format(now))
'''

#========================================================================================
'''
mycart = [10, 20, 800, 60, 70]
for item in mycart:
    if item > 400:
        print("This is not in my budget")
        continue
        print(item)
    else:
        print("You have purchased everything")
'''

#========================================================================================
'''
username = input("Enter username : ")
password = input("Enter password : ")

if username == "admin" and password == "admin123":
    print("Login Successfull")
else:
    print("Invalid Credential")
    username = input("Enter username :")
    password = input("Enter password : ")
'''

#========================================================================================
#Tower of Hanoi
'''
import time
class Tower:
    def __init__(self):
        print("Welcome to tower of Hanoi game")
        print()
        print("Given Problem    A=[3,2,1]   B=[]    C[] ")
        print()
        print("Expected Output    A=[]      B=[]    C[3,2,1] ")
        self.A=[]
        self.B=[]
        self.C=[]

    def tower(self,item):
        self.A.append(item)
        time.sleep(3)
        print("A=",self.A)
        print("Items in Tower A\n")

    def pass1(self):
        self.temp = self.A.pop(2)
        self.C.append(self.temp)
        time.sleep(3)
        print("A=",self.A   ,"  ",  "B=",self.B     ,"  ","C=",self.C)
        print("Pass one has Completed=========================\n")


    def pass2(self):
        self.temp = self.A.pop(1)
        self.B.append(self.temp)
        time.sleep(3)
        print("A=",self.A   ,"  ",  "B=",self.B     ,"  ","C=",self.C)
        print("Pass two has Completed=========================\n")


    def pass3(self):
        self.temp = self.C.pop(0)
        self.B.append(self.temp)
        time.sleep(3)
        print("A=",self.A   ,"  ",  "B=",self.B     ,"  ","C=",self.C)
        print("Pass three Completed=========================\n")

    
    def pass4(self):
        self.temp = self.A.pop(0)
        self.C.append(self.temp)
        time.sleep(3)
        print("A=",self.A   ,"  ",  "B=",self.B     ,"  ","C=",self.C)
        print("Pass four has Completed=========================\n")

        
    def pass5(self):
        self.temp = self.B.pop(1)
        self.A.append(self.temp)
        time.sleep(3)
        print("A=",self.A   ,"  ",  "B=",self.B     ,"  ","C=",self.C)
        print("Pass five has Completed=========================\n")

    def pass6(self):
        self.temp = self.B.pop(0)
        self.C.append(self.temp)
        time.sleep(3)
        print("A=",self.A   ,"  ",  "B=",self.B     ,"  ","C=",self.C)
        print("Pass six has Completed=========================\n")

    def pass7(self):
        self.temp = self.A.pop(0)
        self.C.append(self.temp)
        time.sleep(3)
        print("A=",self.A   ,"  ",  "B=",self.B     ,"  ","C=",self.C)
        print("Pass seven has Completed=========================\n")

obj = Tower()
obj.tower(3)
obj.tower(2)
obj.tower(1)
obj.pass1()
obj.pass2()
obj.pass3()
obj.pass4()
obj.pass5()
obj.pass6()
obj.pass7()
'''