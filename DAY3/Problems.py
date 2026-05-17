#1] Maximum number of consecutive 1's in a binary array
"""
list=[]

count=0
maxi=0

for i in list:
    if i==1:
        count += 1

        if count > maxi:
            count = maxi
        else:
            count = 0
"""
#========================================================================================

#2] To count a number of substring in a string

"""
name = input()

count = 0
for i in range(len(name)):
    for j in range(i,len(name)):
        print(name[i:j+1])
        count += 1
print(count)

""" 
#========================================================================================

#3] Biggest number
"""

def findBiggestNumber(sampleArray):
    biggestNumber = sampleArray[0]  # time complexity -> O(1)
    for index in range(1,len(sampleArray)): # time complexity ->O(N)
        if sampleArray[index] > biggestNumber: # time complexity -> O(1)
            biggestNumber = sampleArray[index] # time complexity -> O(1)
    print(biggestNumber) # time complexity -> O(1)

sampleArray = [5 , 7 , 9 , 2 , 3 , 4]  # time complexity -> O(1)
findBiggestNumber(sampleArray)  # time complexity -> O(1)

#Total time complexity = O(1) + O(1) + O(1) + O(1) + O(N) = O(N)
"""

#========================================================================================

#4] what is the runtime of the above code
"""
def foo(array):
    sum = 0   # time complexity -> O(1)
    product = 1 # time complexity -> O(1)

    for i in array: # time complexity -> O(N)
        sum += i # time complexity -> O(N)

    for i in array: # time complexity -> O(N)
        product *= i # time complexity -> O(1)

    print("Sum = "+str(sum)+", product = "+str(product)) # time complexity -> O(1)
 
#Total time complexity = O(N)
"""

#========================================================================================

#5]Removing spaces from the strip
# 1. rstrip() - To remove spaces at righjt hand side 
# 2. lstrip() - To remove spaces at left hand side 
# 3. strip() -  To remove spaces from both side

"""
city = input("ENter your city Name")
scity = city.strip()
if scity == 'Hyderabad':
    print("Hello Hyderabad..Adab")
elif scity == 'Chennai':
    print("Hello Madrasi..Vadakkam")
elif scity == 'Banglore':
    print("Hello Kannadiga..Shubhodaya")
else:
    print("Your entered city is invalid")

"""

#========================================================================================

#6] Flow wise max value
#[100 , 198 , 333 , 323]
#[122 , 232 , 221 , 111]
#[223 , 565 , 245 , 764]
"""
newlist = [[100 , 198 , 333 , 323],
           [122 , 232 , 221 , 111],
           [223 , 565 , 245 , 764]]
mylist=[]
for i in range(3):
    j=0
    max = newlist[i][j]
    for j in range(4):
        c_max = newlist[i][j]
        if max < c_max:
            max = c_max
    mylist.append(max)
print(mylist)

"""

#========================================================================================
#input = 'Suhani*is*a*good*programmer'
#output = ****Suhaniisagoodprogrammer
"""
name = 'Suhani*is*a*good*programmer'
newname = '' 
val = ''
for i in name :
    if i != '*':
        newname += i
    else:
        val += i
print(newname)
print(str(val+newname))

"""

#========================================================================================
#input = aaabbbbccceeeee
#output = a3b4c3e5
a = input()
count = 1
for i in range(len(a)-1):
    if a[i]==a[i+1]:
        count += 1
    else:
        print(a[i] + str(count), end="")
        count = 1

print(a[-1] + str(count))