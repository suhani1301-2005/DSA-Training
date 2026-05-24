

# 22. Remove Leading Zeros from a List of Integers

# Question:
# Write a function to remove leading zeros from a list of integers.

# Logic:
# Use list slicing or a loop to remove zeros until a non-zero element is encountered.

# Sample Input:
# [0, 0, 1, 2, 0, 3, 0, 0, 4]


arr = [0, 0, 1, 2, 0, 3, 0, 0, 4]
new_arr = []
def removeZero(arr):
    for i in range (len(arr)):
        if arr[i] != 0:
            new_arr.append(arr[i])
    return new_arr
    
print(removeZero(arr))