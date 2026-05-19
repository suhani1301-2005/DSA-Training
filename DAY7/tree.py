#tree real life application isasxu
'''
class Tree:
    def __init__(self,data):
        self.data = data #("Drinks")("Hot")("Cold")
        self.child = []


    def addChild(self,object):
        self.child.append(object)
        print("Tree Node added")

    def __str__(self,level =0):
        ret =" "*level + str(self.data) +"\n"
        for ch in self.child:
            ret += ch.__str__(level+1)
        return ret

rootNode = Tree("Drinks")
Hot      = Tree("Hot")
Cold     = Tree("cold")
Tea      = Tree("Tea")
Coffee   = Tree("Coffee")
NonAlcoholic = Tree("NonAlchoholic")
Alchoholic = Tree("Alchoholic")

rootNode.addChild(Hot) #left 
rootNode.addChild(Cold) #right
Hot.addChild(Tea)  #left 
Hot.addChild(Coffee) #right
Cold.addChild(NonAlcoholic) #left 
Cold.addChild(Alchoholic) #right

print(rootNode) #when this method call str method wil aitomatcally called
'''

#tree real life application isasxu
class Tree:
    def __init__(self,data):
        self.data = data #("N1")("N2")("N3")
        self.child = []


    def addChild(self,object):
        self.child.append(object)
        print("Tree Node added")

    def __str__(self,level =0):
        ret =" "*level + str(self.data) +"\n"
        for ch in self.child:
            ret += ch.__str__(level+1)
        return ret

rootNode = Tree("N1")
N2= Tree("N2")
N3     = Tree("N3")
N4      = Tree("N4")
N5   = Tree("N5")
N7 = Tree("N7")
N8 = Tree("N8")
N6 = Tree("N6")

rootNode.addChild(N2) #left 
rootNode.addChild(N3) #right
N2.addChild(N4)  #left 
N2.addChild(N5) #right
N4.addChild(N7) #left 
N4.addChild(N8) #right
N3.addChild(N6)

print(rootNode) #when this method call str method wil aitomatcally called