'''
mytuple = ("prashant", "Ashish", "Rahul", "Sandip", "Komal", "ankush", "rajesh", 23, 3.15, 77,
           "sandip")
print(mytuple)
print(type(mytuple))

mytuple[2]="sunil" #checking immutability of tuple
print(mytuple)
'''

#========================================================================================

#MCQ
'''
#1] 
init_tuple = ()
print(init_tuple.__len__())

#========================================================================================

init_tuple_a = 'a', 'b'
init_tuple_b=('a', 'b')
print(init_tuple_a == init_tuple_b) #True

#========================================================================================


init_tuple_a = '1', '2'
init_tuple_b=('3', '4')
print(init_tuple_a + init_tuple_b) #True

#========================================================================================

l=[1,2,3]
init_tuple = ('python',) * (l.__len__()-l[::-1][0])
print(init_tuple)

#========================================================================================

init_tuple= ('Python',)*3
print(type(init_tuple)) #tuple

#========================================================================================
 
init_tuple= ('Python')*3
print(type(init_tuple)) #tuple

#========================================================================================

init_tuple = (1,)*3
iniit_tuple[0] = 2 #checking immutability of tuple
print(init_tuple)

#========================================================================================

init_tuple=((1,2,))*7

print (len(init_tuple[3:8]))
'''
#========================================================================================
'''
mydict = {
    101: "Suhani",
    102: "Ashish",
    103: "Mohini",
    104: "trivani",
    101: "Ashish",
    104: "Ashish"
}
print(type(mydict)) #<class 'dict'
print(mydict) # {101: 'Ashish', 102: 'Ashish', 103: 'Mohini', 104: 'Ashish'
    
#with the help of key we have to print values
a = mydict[102]
print(a) #Ashish

#with the help of key we will replace the old value by new value
mydict[102] = "Suhani"
print(mydict) # {101: 'Ashish', 102: 'Suhani', 103: 'Mohini', 104: 'Ashish'

#only print key x=0,1
for x in mydict:
    print(x) #101,102,103,104

#only print values
for x in mydict.values():
    print(x) #Ashish, Suhani, Mohini, Ashish

#print key and values both
for x,y in mydict.items():
    print(x,y) #101 Ashish, 102 Suhani, 103 Mohini, 104 Ashish

#adding a new key:valuees pair
mydict["mobile_no"] = 1234567890
print(mydict) # {101: 'Ashish', 102: 'Suhani', 103: 'Mohini', 104: 'Ashish', 'mobile_no': 1234567890}

'''
#========================================================================================

'''
a = {(1,2):1,(2,3):2,(4,5):3}
print(a[4,5]) 
'''

'''
a = {'a':1,'b':2,'c':3 }
print(a['a','b'])
'''
#========================================================================================

'''
my_dict = {}
my_dict[(1,2,4)]=8
my_dict[(4,2,1)]=10
my_dict[(1,2)]=12
sum = 0
for k in my_dict:
    sum += my_dict[k]
print(sum) #30
print(my_dict) #{(1, 2, 4): 8, (4, 2, 1): 10, (1, 2): 12}
'''

#========================================================================================

'''
box = {}
jars = {}
crates = {}
box['biscuits'] = 1
box['cake'] = 3
jars['jam'] = 4
crates['box'] = box
crates['jars'] = jars
print(len(crates[box])) #type error
'''
#========================================================================================
'''
dict = {'c': 97, 'a': 96, 'b': 98}
for _ in sorted(dict):
    print (dict[_])
'''
#========================================================================================

'''
rec = {"Name": "Python", "Age": 30, "City": "Pune"}
r = rec.copy()
print(id(r) == id(rec))
print(id(r))
print(id(rec))
'''
#========================================================================================

#find the key with maximum value in a dictionary

# num = 123
# a= num%10
# num = num // 10 
# b= num 

Amount = int(input("Please enter amout for withdraw: "))
print(" 100 notes= ",Amount//100)
print(" 50 notes= ",(Amount%100)//50)
print(" 20  notes=" ,((Amount%100)%50)//20 )
print(" 10  notes=" ,(((Amount%100)%50)%20 )//10)
print(" 5  notes=" ,((((Amount%100)%50)%20 )%10)//5)
print(" 2  notes=" ,(((((Amount%100)%50)%20 )%10)%5)//2)
