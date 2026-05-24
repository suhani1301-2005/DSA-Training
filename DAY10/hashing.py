'''
Hashing is a technique used to convert data into a fixed size value called a 
hash value or hash code.

Imagine :
10 student = easy to search
10 lakh student = searching becomes slow

Without hashing = searching may take a lot of time
With hashing = 

Before hashing, searching required :
1. linear search = O(n)
2. Binary search = O(log n)
#  Hashing = O(1) lookup time

Operation     Without hashing       With Hashing
Search            O(n)                 O(1)
Insert            O(n)                 O(1) 
Delete            O(n)                 O(1)

In hashing we use hash() function
=> A hash function cinvert input -> fixed index
Example : hash("apple")

key % 10

Key     Calculation     Index

15      15 % 10         5

25      25 % 10         5

35      35 % 10         5


Problem?

All map to same index.

This is called:
Collision


'''
class HashTable:

    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_function(self, key):
        return key % self.size

    def insert(self, key):
        index = self.hash_function(key)
        self.table[index].append(key)

    def display(self):
        print(self.table)


h = HashTable(10)

h.insert(15)
h.insert(25)
h.insert(35)

h.display()