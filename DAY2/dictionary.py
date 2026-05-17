# represented by {key:value}
# duplicate keys are not allowed but duplicates value are allowed
# Growable, mutable, unorder list

# mydict = {
#     101: "Pratiksha",
#     102: "Suhani",
#     103: "Sudhanshu",
#     104: "Tejas",
#     101: "Suhani",
#     104: "Suhani"
# }
# print(mydict)

# a = mydict[102]
# print(a)    # By key we can print value

# mydict[102] = "Prachi"
# print(mydict)

# for x in mydict:
#     print(x)      # only print keys

# for x in mydict.values():
#     print(x)      # only print value

# for x, y in mydict.items():
#     print(x, y)   #  print both key and value

# adding a new key:value pair
# mydict["mobile_no"] = 1234506788
# print(mydict)

# mydict["Department"] = "Management"
# print(mydict)

# mydict.pop(101)   # key 101 will be remove
# print(mydict) 

# Que 1
# a = {(1,2):1, (2,3):2, (4,5):3}  # (1,2)(2,3)(4,5) = key
# print(a[4,5])  # 3

# Que 2
# a = {'a':1, 'b':2, 'c':3}
# print(a['a', 'b'])  # key error

# Que 3
# arr = {}
# arr[1] = 1
# arr['1'] = 2
# arr[1] += 1
# print(arr)    # {1: 2, '1': 2}
# sum = 0 
# for k in arr:
#     sum += arr[k]
# print(sum)

# Que 4
# my_dict = {}
# my_dict[1] = 1
# my_dict['1'] = 2
# my_dict[1.0] = 4
# print(my_dict)   # {1: 4, '1': 2}
# sum = 0
# for k in my_dict:
#     sum += my_dict[k]
# print(sum)

# Que 5
# my_dict = {}
# my_dict[(1,2,4)] = 8
# my_dict[(4,2,1)] = 10
# my_dict[(1,2)] = 12
# print(my_dict)
# sum = 0
# for k in my_dict:
#     sum += my_dict[k]
# print(sum)

# Que 6
# box = {}
# jars = {}
# crates = {}
# box['biscuit'] = 1
# box['cake'] = 3
# jars['jam'] = 4
# crates['box'] = box
# crates['jars'] = jars
# print(len(crates[box]))  # error

# box = {}
# jars = {}
# crates = {}
# box['biscuit'] = 1
# box['cake'] = 3
# jars['jam'] = 4
# crates['box'] = box
# crates['jars'] = jars
# print(len(crates['box'])) # 2

# Que 7
# dict = {'c':97, 'a':96, 'b':98}
# for _ in sorted(dict):
#     print(dict[_])

# Que 8
# rec = {"Name": "Python", "Age": 20}
# r = rec.copy()
# print(id(r))
# print(id(rec))
# print(id(r) == id(rec)) 

# Que 9
# rec = {"Name": "Python", "Age": 20}
# id1 = id(rec)
# print(id1)
# del rec
# rec = {"Name": "Python", "Age": 20}
# id2 = id(rec)
# print(id2)
# print(id1 == id2)

# Que 10 - Find the key with maximum value 
# dict = {"A": 50, "B": 30, "C": 70}
# for _ in dict:
#     if dict[_] == max(dict.values()):
#         print(i) 

# Que 11 - Find key with minimum value
# dict = {"X": 20, "Y": 10, "Z": 30} 
# for i in dict:
#     if dict[i] == min(dict.values()):
#         print(i)

# Que 12 - Count frequency of element in a list
list = [1,2,2,3,4,3,5]
freq = {}
for i in list:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1
print(freq)
