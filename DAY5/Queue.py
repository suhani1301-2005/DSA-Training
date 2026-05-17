#Queue Ds
#enque
#deque

import sys
class Queue:
    def __init__(self,size):
        self.myQueue = [] #creating stack /* FIFO */
        self.queueSize = size

    def isFull(self):
        if len(self.myQueue) == size:
            return True
        else:
            return False
        
    def enqueue(self, value):
        if self.isFull():
            print("Queue is Full. ")
        else:
            self.myQueue.append(value)

    def display(self,value):
        print(self.myQueue) 

    def isEmpty(self):
        if self.myQueue == []:
            return True
        else:
            return False
        
    def dequeue(self, value):
        if self.isEmpty():
            print("Queue is Empty. ")
        else:
            self.myQueue.pop(0) #self.myQueue.remove() - thuis teakes one element and gives error

    def peek(self,value):
        if self.isEmpty():
            print("Queue is Empty. ")
        else:
            print(self.myQueue[0])
    
    def delete(self,value):
        self.myQueue = None



size = int(input("Enter the size of the queue : "))
obj = Queue(size)
print("Stack has created :")

while True:   #range is not fixed and to run access loop  multiple times
    print("1. Enque Operation :")
    print("2. Display Queue :")
    print("3. Deque Operation :")
    print("4. Peek Operation :")
    print("5. Delete Queue :")
    print("6. Exit :")

    choice = int(input("Enter the valid number : "))

    if choice == 1:
        value=int(input("Enter element to add in queue : "))
        obj.enqueue(value)
    elif choice ==2:
        obj.display(value)
    elif choice == 3:
        obj.dequeue(value)
    elif choice == 4:
        obj.peek(value)
    elif choice == 5:
        obj.delete(value)
    elif choice == 6:
        sys.exit()
    else:
        exit
'''    
Queue using list
    -> Easy to implement
    -> Speed problem when it grows

Queue using Linked List
    -> Fast Performance
    -> Implementation is not easy

                            Time Complexity         Space Complexity
CREATE Queue                    O(1)                        O(1)
Enque                         O(n)/O(1)                     O(1)                
Deueue                        O(n)/O(1)                     O(1)
Peek                            O(1)                        O(1)
isEmpty                         O(1)                        O(1)
Delete Entire Queue             O(1)                        O(1)
'''
    
