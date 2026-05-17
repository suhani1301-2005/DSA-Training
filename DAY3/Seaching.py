#Linear Search

def linearSearch(array , target):
    for i in range(0,len(array)):  #O(N)
        if array[i] == target:     #O(1)
            return i
    return -1  #if the target value is not in a array
array = [1,2,3,4,5,6,7,8,9]         #O(1)
target = 7 # search the target value i.e 7  #O(1)
result = linearSearch(array,target)    #O(1)
if result == -1:   #O(1)
    print("Element not found")
else:
    print("Element found at index",result)

#TIme complexity :- O(N)