'''
try:
    a = int(input("Enter the first number : "))
    b = int(input("Enter the second number : "))
    print(a/b)
except ZeroDivisionError:
    print("can't divide by zero")
except ValueError:
    print("Enter only integer value")
except:
    print("ABC")
'''
'''
try:
    a = int(input("Enter the first number : "))
    b = int(input("Enter the second number : "))
    print(a/b)
except (ZeroDivisionError):
    print("can't divide by zero")
else:
    print("Everything is ok")
'''

#Finally Block
'''
Always execute
This block always run ,
to close the sql file
'''
import logging

logging.basicConfig(filename="newfile.txt", level=logging.DEBUG)

try:
    a = int(input("enter first integer no"))
    b = int(input("enter second integer no"))

    print(a / b)

except (ZeroDivisionError, ValueError) as message:
    print(message)
    logging.exception(message)

print("Logging Level is set up. Check 'newfile.txt' for log details.")

