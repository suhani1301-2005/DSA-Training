#Stack implementation without size 
# push 
# pop
# peek
# isEmplty
# isFull
# Delete
# Display
'''
import sys
class Stack:
    def __init__(self):
        self.myStack=[]

    def push(self,value):
        self.myStack.append(value)
        print("Element push")

    def display(self):
        print(self.myStack)

    def isEmpty(self):
        if self.myStack == []:
            return True
        else:
            return False
        
    def pop(self): #remove element permenantly from memory
        if self.isEmpty():
            print("Stack is empty")
        else:
            print(self.myStack.pop())     
 
    def peek(self): #return the top most element
        if self.isEmpty():
            print("Stack is Empty")
        else:
            print(self.myStack[-1])        

    def deleteStack(self):
        self.myStack=None


obj = Stack()
print("Stack has created: ")

while True:
    print("1. Push Operation ")
    print("2. Display stack")
    print("3. Pop Operation ")
    print("4. Peek Operation")
    print("5. Delete Stack")
    print("7. Exit")
    choice = int(input("Enter your choice : "))
    if choice == 1:
        value = int(input("Enter value to push in stack : "))
        obj.push(value)
    elif choice == 2:
        obj.display()
    elif choice == 3:
        obj.pop()
    elif choice == 4:
        obj.peek()
    elif choice == 5:
        obj.deleteStack()
    else:
        sys.exit()

'''

#Stack implementation with size limit

import sys
class Stack:
    def __init__(self, size):
        self.myStack=[]  #creating stack
        self.stackSize = size

    def isFull(self):
        if len(self.myStack) == self.stackSize:
            return True
        else:
            return False

    def push(self,value):
        if self.isFull():
                print("Stack is Full")
        else:
            self.myStack.append(value)
            print("Element push")

    def display(self):
        print(self.myStack)

    def isEmpty(self):
        if self.myStack == []:
            return True
        else:
            return False
        
    def pop(self): #remove element permenantly from memory
        if self.isEmpty():
            print("Stack is empty")
        else:
            print(self.myStack.pop())     
 
    def peek(self): #return the top most element
        if self.isEmpty():
            print("Stack is Empty")
        else:
            print(self.myStack[-1])        

    def deleteStack(self):
        self.myStack=None

size = int(input("Enter the size of stack : "))
obj = Stack(size)
print("Stack has created: ")

while True:
    print("1. Push Operation ")
    print("2. Display stack")
    print("3. Pop Operation ")
    print("4. Peek Operation")
    print("5. Delete Stack")
    print("7. Exit")
    choice = int(input("Enter your choice : "))
    if choice == 1:
        value = int(input("Enter value to push in stack : "))
        obj.push(value)
    elif choice == 2:
        obj.display()
    elif choice == 3:
        obj.pop()
    elif choice == 4:
        obj.peek()
    elif choice == 5:
        obj.deleteStack()
    else:
        sys.exit()

'''
Stack using list
    -> Easy to implement
    -> Speed problem when it grows

Stack using Linked List
    -> Fast Performance
    -> Implementation is not easy

                            Time Complexity         Space Complexity
CREATE STACK                    O(1)                        O(1)
Push                         O(1)/O(n^2)                 O(1)                
Pop                             O(1)                        O(1)
Peek                            O(1)                        O(1)
isEmpty                         O(1)                        O(1)
Delete Entire Stack             O(1)                        O(1)
'''