#Binary search is a searching algorithm used to find the position of a target value within a sorted array. It works by repeatedly dividing the search interval in half until the target value is found or the search interval is empty.
'''
def binarysearch(array,targer):
    low=0
    high = len(array)-1
    while low <= high:
        mid = (low + high) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            low = mid +1
        else:
            high = mid - 1
    return -1


array = [2,4,5,9,11,13,14,15,19,20,22,23,27,30,32,39,42,44,45,49,51,
         53,54,55,59,60,62,63,67,70,72,79]
target = 72

result = binarysearch(array,target)
if result == -1:
    print("Element not found")
else:
    print("Element found at position",result)
'''

#========================================================================================

#Bubble sort is a simple sorting algorithm that repeatedly steps through the list, compares adjacent elements and swaps them if they are in the wrong order. The pass through the

def bubble_sort(array):
    for i in range(len(array)-1):
        for j in range(len(array)-i-1):
            if array[j] > array[j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
            print(array)
        print()
array = [64,34,25,12,22,11,90]
bubble_sort(array)