#mylist=["suhani","pratiksha","Vaishnavi","Sakshi","Nandini",77,"Ayush",60.52,"Suahni"]

#Changing the value in list
"""
mylist[2]="Akshay" 
print(mylist)
"""
#========================================================================================
"""
print(mylist)
print(type(mylist))#<List>
print(mylist[0])#suhani
print(mylist[1])#pratiksha
print(mylist[2])#Vaishnavi
print(mylist[-1])#Suhani
print(mylist[2:5])# n=5,n-1=4'Vaishnavi', 'Sakshi', 'Nandini'
print(mylist[:5])#n=5,n-1=4 'pratiksha', 'Vaishnavi', 'Sakshi', 'Nandini'
print(mylist[1:])#n=8, n-1=8-1'pratiksha', 'Vaishnavi', 'Sakshi', 'Nandini', 77, 'Ayush', 60.52, 'Suahni'
print(mylist[1:8:2])#['pratiksha', 'Sakshi', 77, 60.52]
"""

#========================================================================================

#if else
"""
if "ankush" in mylist:
   print('Yes ankush is available')
else:
   print("Not available")

"""
#========================================================================================

#appnd() -always add the value in right side / top side
#appnd() and extend works same
"""
mylist.append('harsh')
mylist.append('laxmi')
print(mylist)
"""
#========================================================================================

#insert()- To add an element at specific position

"""
mylist.insert(3,"sanket")
print(mylist)
"""
#========================================================================================

#removing element in the list

"""
mylist.remove("Sakshi")
print(mylist)
"""

#========================================================================================

#copy() - Copy all the elemnt of old list in new list

"""
newlist = mylist.copy()
print(newlist)
"""

#========================================================================================
"""
mylist = [['Suhani', 'saxena'] , ['85.56'] , [440022,"yyy"]]
print("Example of multidimensional list: ")
print(mylist)
#print(mylist[row][column])
print(mylist[0][0])#Suhani
print(mylist[0][1])#saxena
print(mylist[1][0])#85.56
print(mylist[2][0])#440022
print(mylist[2][1])#yyy

"""
#========================================================================================

#Delete list
"""
list2 = [50,25.50,'Suhani']
del list2
print(list2)
"""

#To delet a particular item
"""
del list2[2]
"""
#========================================================================================

"""
list2 = [50,25.50,'Suhani']
list2.clear()
print(list2)
"""

#========================================================================================

#Converting stringf into list

"""
name = "Suhani"
print(name)#Suhani
myname=list(name)
print(myname)#['S', 'u', 'h', 'a', 'n', 'i']
"""
#========================================================================================

#Sorting 
"""
mylist=[44,22,77,0,9,88]
mylist.sort()
#mylist.sort(reverse=True) #for descending order
print(mylist)
"""
#========================================================================================

#Alias

#Alising means assigning one variable reference to another
"""
mylist=[44,22,77,0,9,88]
newlist=mylist
print(id(mylist))
print(id(newlist))
"""

#========================================================================================

#For loop in list

'''
mylist=[44,22,77,0,9,88]
for i in mylist:
    print(i)
'''

#========================================================================================

                              #TASK1-Move the zero in last

'''
mylist=[0,1,4,0,2,5]

for i in mylist:
    if i== 0:
        mylist.remove(i)
        mylist.append(i)
print(mylist) #1, 4, 2, 5, 0, 0
'''
#========================================================================================

#Find The second largest element:
'''
mylist=[7,3,9,2,8]
mylist.sort()
print(mylist[-2])

'''
#========================================================================================

#MCQ
#1]
'''
a=[1,2,3,4,5,6,7,8,9]
a[::2]=10,20,30,40,50,60 #remove 60 to get the correct ans
print(a)
'''

#2]
'''
b=[1,2,3,4,5]
print(b[3:0:-1])
# A. Syntax error
# B. [4,3,2]   right
# C. [4,3]
# D. [4,3,2,1]
'''

#3]
'''
arr = [[1,2,3,4],
       [4,5,6,7],
       [8,9,10,11]
       [12,13,14,15]]
for i in range(0,4): #only focused on row's
    print(arr[i].pop())
'''

#4]

#5]
'''
fruit_list1 = ['Apple' , 'Berry' , 'Cherry' , 'papaya']
fruit_list2 = fruit_list1
fruit_list3 = fruit_list1[:]
fruit_list2[0] = 'Guava'
fruit_list3[1] = 'Kiwi'

sum=0
for ls in(fruit_list1 , fruit_list2 , fruit_list3):
    if ls[0] == 'Guava':
        sum += 1
    if ls[1] == 'Kiwi':
        sum += 20

print(sum)
'''
#========================================================================================

# FInd the Intersection of three arrays:
# Find the comm
#use three sets to keep track of common elementsbetween the arrays
'''
A=[1,2,3]
B=[2,3,4]
C=[3,4,5]

for i in A:
    if i in B and i in C:
        print(i) #3
'''

#========================================================================================

#Task

mylist=[]
N = int(input("Enter the value of N: "))
for i in range(N):
    val = int(input("Enter the value: "))
    mylist.append(val)
#print(len(mylist))

sum=0

for i in range(len(mylist)-1):
    if i+1 in range(len(mylist)):
        sum += abs(mylist[i]-mylist[i+1]) 

print(sum)