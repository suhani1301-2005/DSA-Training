#Full Binary Tree
'''
-> Each node has either 0 or 2 children
-> No node has a single child
'''

#Complete Binary tree
'''
-> All levels except possibly the last are completely filled
-> Nodes in the last level are filled from left to right
'''

#Perfect Binary tree
'''
-> All internal nodes have exactly two nodes
-> All leaf nodes are at the same level

1] Creation of node
2] Insertion of a node
3] Deletion of a node
4] search for a node
5] Traverse all node 
6] Deletion of node

Check time complexity of all traversal and search operationzaq

'''

# Why binary search tree is used?
'''
-> it performs faster than Binary Treee wheen inserting and deleting nodes.
'''

class BSTNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None
    

def insertNode(rootNode , nodeValue):
    if rootNode.data == None:
        rootNode.data = nodeValue

    elif nodeValue <= rootNode.data:
        if rootNode.leftChild is None:
            rootNode.leftChild = BSTNode(nodeValue)
        else:
            insertNode(rootNode.leftChild , nodeValue)

    else :
        if rootNode.rightChild is None:
            rootNode.rightChild = BSTNode(nodeValue)
        else:
            insertNode(rootNode.rightChild,nodeValue)

def searchNode(rootNode,nodeValue):
    if rootNode.data == nodeValue:
        print("The value is found")
    elif nodeValue < rootNode.data:
        if rootNode.leftChild.data == nodeValue:
            print("The value is found")
        else:
            searchNode(rootNode.leftChild , nodeValue)
    else:
        if rootNode.rightChild.data == nodeValue:
            print("The value is found")
            
        else:
            searchNode(rootNode.rightChild , nodeValue) 
    
        

def preOrderTraversal(rootNode):
    if not rootNode:
        return
    print(rootNode.data, end = " ")
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)


def inOrderTraversal(rootNode):
    if not rootNode:
        return
    inOrderTraversal(rootNode.leftChild)
    print(rootNode.data, end = " ")
    inOrderTraversal(rootNode.rightChild)


def postOrderTraversal(rootNode):
    if not rootNode:
        return
    postOrderTraversal(rootNode.leftChild)
    postOrderTraversal(rootNode.rightChild)
    print(rootNode.data, end = " ")


newBST = BSTNode(None)
insertNode(newBST , 70)
insertNode(newBST , 50)
insertNode(newBST , 90)
insertNode(newBST , 30)
insertNode(newBST , 60)
insertNode(newBST , 80)
insertNode(newBST , 100)
insertNode(newBST , 20)
insertNode(newBST , 40)
insertNode(newBST , 10)

print("PreOrder Traversal : ")
preOrderTraversal(newBST)
print()
print("In-Order Traversal :")
inOrderTraversal(newBST)
print()
print("Post-Order Traversal :")
postOrderTraversal(newBST)
print()
searchNode(newBST,80)