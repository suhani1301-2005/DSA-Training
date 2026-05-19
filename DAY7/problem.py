# 14. Find the First Non-Repeating Character

# Question:
# Write a function to find the first non-repeating character in a string.

# Logic:
# Define a function that uses loops to count characters and find the first non-repeating character.

# Sample Input:
# "leetcode"

# Expected Output:
# "l"
'''
def first_non_repeating_character(s):
    count = {}
    for i in s:
        if i
'''

#====================================================================================================
#Recursion
'''
1)recursion uses stack memory thats why we avoid using recursion

2)When will you use recursion?
    ->Wnen the main problem can be divided into similar sub problem 
    ->Preorder , postorder traversal

3)Difference between recurssion and itteration
Que : Comparision between recursion and iteration in tewrm of time and space complexity?

                        TC               SC
Space efficiency        No               Yes      Iteration does not require extra stack 
                                                  memory, while recursion uses stack 
                                                  memory for every function call.

Time efficiency         No               Yes      Recursion takes more time because of 
                                                  repeated function calls and stack 
                                                  operations like push and pop.

Easy to use             Yes              No       Recursion is easier to write when a 
                                                  problem can be divided into smaller 
                                                  similar sub-problems.
'''

#====================================================================================================
'''
def factorial(num):
    if num <= 1:
        return 1
    return num * factorial(num - 1)
print(factorial(4))
'''

#====================================================================================================
#2]
'''
def capitalizeFirst(arr):

    result = []
    if len(arr) == 0:
        return result

    result.append(arr[0][0].upper() + arr[0][1:])
    return result + capitalizeFirst(arr[1:])

print(capitalizeFirst(['car' , 'taco' , 'banana']))
'''
#====================================================================================================
#3]
'''
def power(base,exponents):
    if exponents == 0:
        return 1
    return base * power(base , exponents-1)

print(power(2,0))
print(power(2,2))
print(power(2,4))
#2*power(2,1)
#2*power(2,0)
#2*2*1
'''
#====================================================================================================
#4] Product of array
'''
def productOfArray(arr):
    if len(arr) == 0:
        return 1
    return arr[0] * productOfArray(arr[1:])

print(productOfArray([1,2,3]))
print(productOfArray([1,2,3,10]))
'''
#====================================================================================================
#5] Reverse a string using recurssion
'''
def reverse(strng):
    if len(strng) <=1:
        return strng
    return strng[len(strng)-1] + reverse(strng[0: len(strng)-1])

print(reverse('python'))
print(reverse('suhani'))
'''
#====================================================================================================
#6] Recurssive range
'''
def recursiveRange(num):
    if num <= 0:
        return 0
    return num + recursiveRange(num-1) #6+5+4+3+2+1

print(recursiveRange(6))
'''
#====================================================================================================
#7] Is string pallindrome

'''
def isPalindrome(string):
    if len(string) == 0: # if string is empty
        return True
    if string[0] != string[len(string)-1]:
        return False
    return isPalindrome(string[1:-1])
print(isPalindrome('racecar'))
print(isPalindrome('awesome'))
print(isPalindrome('s'))
print(isPalindrome('treat'))
'''

#====================================================================================================
#8]
'''
def someRecursive(arr, cb):
    if len(arr) == 0:
        return False

    if not(cb(arr[0])):
        return someRecursive(arr[1:], cb)

    return True


def isOdd(num):
    if num % 2 == 0:
        return False
    else:
        return True


print(someRecursive([1,2,3,4], isOdd))   # true
print(someRecursive([4,6,8,9], isOdd))   # true
print(someRecursive([4,6,8], isOdd))     # false
'''
# 6. Array Rotation

# Question:
# Rotate an array to the right by a given number of steps.

# Logic:
# Use array slicing or create a new array to rearrange elements according to the rotation steps.

# Sample Input:
# [1, 2, 3, 4, 5] rotated by 2 steps

# Expected Output:
# [4, 5, 1, 2, 3]
'''
arr = [1,2,3,4,5]

k=int(input("Enter the no of steps : "))

for n in range(k):
    last = arr[len(arr)-1]
    for i in range(len(arr)-1 , 0 , -1):
        arr[i] = arr[i-1]
    arr[0] = last
print(arr)
'''
#2nd method
'''
arr = [1,2,3,4,5]

k = 8

new_arr = []

for i in range(len(arr)):
    new_arr.append(0)

for i in range(len(arr)):

    new_index = i + k

    if new_index >= len(arr):
        new_index = new_index - len(arr)

    new_arr[new_index] = arr[i]

print(new_arr)
#3rd method
'''
arr = [1,2,3,4,5]

k = 7

while k >= len(arr):
    k = k - len(arr)

arr = arr[-k:] + arr[:-k]

print(arr)
