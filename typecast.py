print(2+2)
print("2"+"2")
# a=input("Enter first number: ")
# b=input("Enter second number: ")
#Implicit Typecasting
#Complex number cannot typecasted to integer or float. So we cannot perform addition operation on complex numbers.
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
print(a+b)
#Input function by default take input in string format. So we need to convert it into integer format to perform addition operation.

#==============================================================================================

# int() used to convert in integer 3.14=int=3
#print(int(3.14))
#print(int(10+5j))
#print(int(True))#=-1
#print(int(False))#=0
#print(int("4.22"))#ValueError: invalid literal for int() with base 10: '4.22'
#print(int("123"))
#we cannot convert float to integer directly because it will lose the decimal part. So we need to use int() function to convert it into integer format.
#we cant convert string name to int'''

#==============================================================================================

# float() used to convert in float 3=int(3.0)
#print(float(3))
#print(float(10+5j))
# print(float(True))
# print(float(False))
# print(float("4.22"))
# print(float("123"))
# #print(float("name))
#we cannot convert complex number to float because it will lose the imaginary part. So we need to use float() function to convert it into float format.
#cant conert string name to float

#==============================================================================================

# print(complex(3))
# print(complex(12.5))
# print(complex(True))
# print(complex(False))
# print(complex("5"))
# print(complex("5.6"))
# #print(complex("name"))
# print(complex(5,-3))
# print(complex(True,False))
#we cannot convert string name to complex because it will lose the imaginary part. So we need to use complex() function to convert it into complex format.

#==============================================================================================

#bool() used to convert in boolean
print(bool(0))
print(bool(1))
print(bool(-1))
print(bool(0.0))
print(bool(3.14))
print(bool("1+2j"))
print(bool("0+0j"))
print(bool(False))
print(bool(True))
#print(bool(""))#empty string is false 
