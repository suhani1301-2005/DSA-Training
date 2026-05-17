# #for loop (sequentially incremment )
# for i in range(5):
#     print(i)

# print("=================================================================================")


# for i in range(2,11):#10 tak print krne k liye 
#     print(i)

# print("=================================================================================")

# for i in range(2,10,2): #2 se increment krne k liye
#     print(i)

# print("=================================================================================")

# for i in range(5,0,-1): # 1 se decrement krne k liye
#     print(i)

# print("=================================================================================")
#  #Table of 2

# for i in range(1,11):
#     print(2*i)

#TAsk1

# print("=================================================================================")
 
# for i in range (1,11):
#     print(2*i," " , 3*i," ", 4*i," ", 5*i," ", 6*i," ", 7*i," ", 8*i," ", 9*i," ", 10*i)

# print("=================================================================================")

# for j in range (1,11):
#     print(11*i," " , 12*i," ", 13*i," ", 14*i," ", 15*i," ", 7*16," ", 17*i," ", 18*i," ", 119*i)

"""
task2 Write a program to accept three paper marks and calculate total, 
percentage and check if he/she is passed in all the subjects so print pass 
else print fail

if percentage is greater than 65 and greater ="male" so he is eligible for placemrnt
else not eligible
"""

# English=int(input("Enter marks of English : "))
# Maths=int(input("Enter marks of Maths :  "))
# Science=int(input("Enter marks of Science : "))

# total = English+Maths+Science
# percentage=total/3.0

# print("Total=",total)
# print("Percentage=",percentage)

# if English>=40 and Maths>=40 and Science>40:
#     print("PASS")
# else:
#     print("Fail")

# gender=input("Enter your gender M/F : ")
# if percentage>=65 and gender == "M":
#     print("ELIGIBLE FOR PLACEMENT")
# else:
#     print("NOT ELIGIBLE")


#Task 3
"""
1     5
2     4
4     2
5     1
"""

#zip():- we can take multiple range function inside zip()
for i,j in zip(range(1,6),range(5,0,-1)):
    if i==3 and j==3:
        continue
    print(i," ",j)