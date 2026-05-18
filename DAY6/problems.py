# 16. Reverse Each Word in a String

# Question:
# Write a program to reverse each word in a string.

# Logic:
# Split the string into words, reverse each word, and join them back together.

# Sample Input:
# "Hello world"

# Expected Output:
# "olleH dlrow"
'''
s = "Hello world"
s1 = s.split()
reversed_s = []
for s2 in s1:
    reversed_s.append(s2[::-1])

result = " ".join(reversed_s)
print(result)
'''

# 17. Check for Valid Parentheses

# Question:
# Write a program to check if a string containing parentheses is valid.

# Logic:
# Use a stack to keep track of open and close parentheses.

# Sample Input:
# "({[()]})"

# Expected Output:
# Valid

def valid_parentheses(s):

    stack = []

    for ch in s:

        # opening brackets
        if ch in "({[":
            stack.append(ch)

        # closing brackets
        else:

            if not stack:
                return "Invalid"

            top = stack.pop()

            if (ch == ')' and top != '(') or \
               (ch == '}' and top != '{') or \
               (ch == ']' and top != '['):
                return "Invalid"

    if not stack:
        return "Valid"
    else:
        return "Invalid"


# Sample Input
s = "({[()]})"

print(valid_parentheses(s))

#====================================================================================================


# 30. Find All Duplicates in a List
# Question:
# Write a function to find all the elements that appear more than once in a list.
# Logic:
# Use a loop and a dictionary to count occurrences.
# Sample Input:
# [4, 3, 2, 7, 8, 2, 1, 5, 5]
# Expected Output:
# [2, 5]
'''
list = [4, 3, 2, 7, 8, 2, 1, 5, 5]
newlist = {}
def duplicate(list):
    for i in range(len(list)):
        if list[i] in newlist:
            list[i] += 1
    return list
    
'''
    
'''
nums = [4, 3, 2, 7, 8, 2, 1, 5, 5]

def duplicate(nums):

    count = {}
    ans = []

    for num in nums:

        if num in count:
            count[num] += 1
        else:
            count[num] = 1

    for key in count:

        if count[key] > 1:
            ans.append(key)

    return ans

print(duplicate(nums))
'''
# 22. Sort Dictionary by Key or Value
# Question:
# Write a function to sort a dictionary by keys or values in ascending or descending order.
# Logic:
# Use the sorted() function with a custom key or use list comprehension.
# Sample Input:
# {"C": 3, "B": 2, "A": 1}
# Expected Output (Ascending by Key):
# {"A": 1, "B": 2, "C": 3}
# Expected Output (Descending by Value):
# {"C": 3, "B": 2, "A": 1}
'''
# Function to sort dictionary by keys
def sort_by_key(d, reverse=False):
    return dict(sorted(d.items(), key=lambda x: x[0], reverse=reverse))


# Function to sort dictionary by values
def sort_by_value(d, reverse=False):
    return dict(sorted(d.items(), key=lambda x: x[1], reverse=reverse))


# Sample Dictionary
data = {"C": 3, "B": 2, "A": 1}

# Ascending by Key
print("Ascending by Key:")
print(sort_by_key(data))

# Descending by Value
print("\nDescending by Value:")
print(sort_by_value(data, reverse=True))
'''