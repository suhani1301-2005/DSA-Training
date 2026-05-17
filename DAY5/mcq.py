#1]
'''
def func(value , values):
        var =1 
        values[0] = 44
t=3
v=[1,2,3]
func(t,v)
print(t,v[0])
'''
#========================================================================================

#2]
'''
def f(i, values = []):
    values.append(i)
    print(values) #return value
f(1)#calling function
f(2)
f(3)
'''
#========================================================================================

#3]
'''
fruit = {}
def addone(index):
    if index in fruit:
        fruit[index] += 1
    else:
        fruit[index] = 1
addone('Apple')
addone('Banana')
addone('apple')
print(len(fruit))
'''
#========================================================================================

#4]
'''
x = ['A', 'B', 'C']
y = ['A', 'B', 'C']
z = [1,2,3,4]
print(x==y)
print(y==z)
print(x!=z)        
'''
#========================================================================================

#5] LIst Comprehenssion

#s=[1,4,9,16,25,36,49,64,81,100]
'''
val = [2**i for i in range(1,6)]
print(val)
'''
#val2=[i for i in s if i%2 ==0]
#print(val2)

#========================================================================================

#5]
'''
s = [i**i for i in range(1,11)]
print(s)
'''

#========================================================================================

#6]Dictionary comprehenssion
'''
squares = {x:x*x for x in range(1,6)}
print(squares)
'''
#========================================================================================

#7]Dictionary comprehenssion
'''
doubles = {x:2*x for x in range(1,6)}
print(doubles)
'''
#========================================================================================

#8]Dictionary comprehenssion
#How to read multiple values from the keyword in a single 

a,b = [int(x) for x in input("Enter 2 numbers : ").split()]
print("Product is :", a*b)

#========================================================================================

#9]
a,b,c = [float(x) for x in input("Enter 3 numbers : ").split(' , ')]
print("The sum is :", a+b+c)