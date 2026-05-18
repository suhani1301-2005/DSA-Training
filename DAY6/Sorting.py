#Insertion sort
'''
arr = [5,3,8,6,2]
for i in range (1,len(arr)):
    key = arr[i]
    j = i - 1
    while j>=0 and arr[j]>key:
        arr[j+1] = arr[j]
        j = j-1
    arr[j+1] = key
print(arr)
'''
#Time complexity - O(N)^2

#====================================================================================================

#Selection sort
'''
arr = [20 , 12 , 10 , 15 , 2]
for i in range(len(arr)):
    min = i
    j = j+1
    while j< len(arr):
        if arr[j] < arr[min]:
            min = j
        j = j+1

    temp = arr[min]
    arr[min] = arr[i]
    arr[i] = temp

    #arr[i] , arr[min] = arr[min] , arr[i] #Shortcut for swapping
print(arr)
'''

#====================================================================================================
#Instance variable

# we can declare tge instance variable in the constructor and we can use it in any method 
# of the class using self keyword
#instance varibla dependent on the state of object and we can create multiple objects of the class
#  and each object will have its own copy of instance variable

#Ex - Different students receive different marks in the exam and we can create multiple objects of the class and each object will have its own copy of instance variable
'''
class New:
    def __init__(self):
        self.a = 10

Obj1 = New()
Obj2 = New()
Obj3 = New()
Obj1.a = 20
print(Obj1.a)
print(Obj2.a)
print(Obj3.a)
'''
#====================================================================================================
#Static variable
# we can declare the static variable inside the class but outside the constructor and we can access it using class name or object name
# static variable is shared among all the objects of the class and it is not dependent on the

'''
class New:
    a = 10

    def __init__(self):
        self.name = "Suhani"
Obj1 = New()
Obj2 = New()
Obj3 = New()
New.a = 50
print(Obj1.a) 
print(Obj2.a)
print(Obj3.a)
'''

#====================================================================================================

# for every object a separate copy of instance variable is created
# but in case of static variable only one copy will be created
# and it is accessible for every object of the class

class College:
    collegename = "Ramdeobaba "   # static variable (1 memory)

    def __init__(self):
        self.studentname = "Suhani"   # instance variable (3 separate memory)


principal = College()    # object creation
teacher = College()
accountant = College()

print("principal=", principal.collegename, ":", principal.studentname)
print("teacher =", teacher.collegename, ":", teacher.studentname)
print("accountant=", accountant.collegename, ":", accountant.studentname)

College.collegename = "RBU"   # second way to add static variable

principal.studentname = "Suhani Saxena"

print("principal=", principal.collegename, ":", principal.studentname)
print("teacher =", teacher.collegename, ":", teacher.studentname)
print("accountant=", accountant.collegename, ":", accountant.studentname)