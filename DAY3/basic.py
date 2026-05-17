#While-loop
'''
i = 1
while i <= 5:
    print(i)
    i += 1
'''

#========================================================================================

#function
'''
def hello():
    print("Hello world!")
hello() #calling funtion
hello()
'''
#========================================================================================
'''
def arithmetic():
    a = int(input("Enter a value of a: "))
    b = int(input("Enter a value of b: "))
    sum = a + b
    sub = a - b
    div = a / b
    mul = a * b
    return sum , sub , div , mul # output will be in tupple as it wont be cahnge 
    #return multiple value as we want 

#print(arithmetic())
result = arithmetic()
print("Arithmetic =",result)
'''

#========================================================================================

#Positional arguments
'''
def arithmetic(a,b):
    sum = a + b
    sub = a - b
    div = a / b
    mul = a * b
    return sum , sub , div , mul  
result = arithmetic(5,5)
print("Arithmetic =",result)
'''

#========================================================================================

#Keyword arguments

'''

def credential(username , password):
    if username == password:
        print("Login Successfully")
    else:
        print("invalid credentials")

credential(username = "admin" , password = "admin")
'''

#========================================================================================
#default arguments

'''
def cityname(city="pune"):  #default argument (if any calling function dont have any value then it will use this default value)
    print(city)
cityname("Nagpur") #positional argu
cityname("Mumbai")
cityname() #TypeError: cityname() missing 1 required positional argument: 'city (without using default argument thois errir will conme)
'''

#========================================================================================

# variable length argument / variable number of arguments

'''
def cityname(*name):
    print(name)

cityname("Nagpur" , "delhi" , "Pune" , "mumbai")

'''
#========================================================================================

#modularity approach in function
import sys
def add():
    a = int(input("Enter the value of a: "))
    b = int(input("Enter the value of b: "))
    print(a+b)

def sub():
    a = int(input("Enter the value of a: "))
    b = int(input("Enter the value of b: "))
    print(a-b)

def div():
    a = int(input("Enter the value of a: "))
    b = int(input("Enter the value of b: "))
    print(a/b)

def mul():
    a = int(input("Enter the value of a: "))
    b = int(input("Enter the value of b: "))
    print(a*b)

while True:
    print("1. Addition")
    print("2. Subtraction")
    print("3, Division")
    print("4, Multiplication")
    print("5, Exit")

    choice = int(input("Enter your choice: "))
    if choice == 1:
        add() #callling function

    elif choice == 2:
        sub()

    elif choice == 3:
        div()

    elif choice == 4:
        mul()

    # else:
    #     print("Enter a valid number")

    elif choice == 5:
        sys.exit()