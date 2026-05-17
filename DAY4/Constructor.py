#Dedaulf constructor
"""
class Name: #naming convention rule - first letter should be capital of class name
    age = 30 # data member
    def display(self): #method   # object is a runtime entitiy # object is also called as reference variable
        print("Hello world! ")
    
obj = Name()
print(obj.age)
obj.dispaly()
"""
# This code has default constructor which is provided by python itself. It is used to initialize the 
# data members of the class. It is called when an object is created. It is also called as default constructor because it does not take any parameters. 
# It is also called as no-argument constructor because it does not take any arguments.

#========================================================================================

"""
class Students:
    def __init__(self):
        self.name = "Suhani"
        self.age = 30

    def display(self):
        print("Name",self.name)
        print("Age=",self.age)
stuObj = Students()
print(stuObj)
"""

#========================================================================================

"""
class Message:
    def __init__(self):
        print("I am a constructor")

    def show(self):
        print("Class Program")
obj = Message()   # ek object k liye constructor ek hi baar call honga
obj.show()
obj1 = Message()
obj1.show()
"""
#========================================================================================
#Parameterized constructor - when you initilize the data members of the class with the help of parameterized constructor then we can create multiple objects with different values of data members. It is also called as argument constructor because it takes arguments.

class StudentInfo:
    def __init__(self , name , age, roll_no):
        self.Name = name 
        self.Age = age
        self.RollNo = roll_no

    def displayStudentInfo(self):
        print("Name: ",self.Name)
        print("Age: ",self.Age)
        print("Roll No.: ",self.RollNo)

studentObj = StudentInfo("Suhani", 21 , 57)
studentObj.displayStudentInfo()