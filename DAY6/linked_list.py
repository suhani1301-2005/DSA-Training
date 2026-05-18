'''
class Node:
    def __init__(self, data):
        self.data = data #instance variable
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = Node

linkedlist = Linkedlist()

linkedlist = Node(5)
second = Node(10)
third = Node(15)
fourth = Node(20)

#Connecting nodes
linkedlist.head.next = second
second.next = third
third.next = fourth

#display LinkedLisst
while linkedlist.head.next != None:
    print(linkedlist.head.data,"|","->",end=" ")
    linkedlist.head = linkedlist.head.next
'''
#Dynamic node
class Node:
    def __init__(self, data):
        self.data = data #instance variable
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None
        self.tail = None

    def addNode(self,value):
        self.node = Node(value)
        if self.head is None:
            self.head = self.node
            self.tail = self.node

        else:
            self.tail.next = self.node
            self.tail      = self.node

    def display(self,value):
        while self.head is not None:
            print(self.head.data,"|","->",end=" ")
            self.head = self.head.next
        print()

    def addNodeInBeg(self,value):
        print("Add node at begining")
        self.node = Node(value)
        if self.head is None:
            self.head = self.node
            self.tail = self.node
        else:
            self.node.next = self.head
            self.head = self.node


if __name__ == '__main__': #memory is assign to main function first than other functions
    object = Linkedlist()

    while True:
        print("1. Add node Linked List :")
        print("2. Add node in Beginning :")
        print("3. Add node in Between :")
        print("4. Add node in end :")
        print("5. Display Linked List :")
        print("6. Exit :")

        ch = int(input(" Enter your choice"))
        if ch ==1:
            value = int(input(" Enter value for node"))
            object.addNode(value)
            print("Node added successfully in silgle linkedlist")

        elif ch == 2:
            value = int(input(" Enter value for node"))
            object.addNodeInBeg(value)
            print("Node added successfully in silgle linkedlist")

        elif ch == 5:
            object.display(value)


        


