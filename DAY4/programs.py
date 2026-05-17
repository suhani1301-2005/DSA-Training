#1] input-aabbbeeeeffggg

'''
name = 'aabbbeeeeffggg'
newname = {}
for i in range(len(name)):
    key = name[i]
    count = 0
    for j in range(len(name)):
        if key == name[j]:
            count += 1
    newname[key] = count
#print(newname)
for i,j in newname.items():
    print(i,j,sep='',end='')

'''
#========================================================================================

#2]salary increment
'''
salary = int(input('Enter your salary: '))
rating = int(input('Enter your performance apparisal rating : '))
increment = 0
if rating >= 1 and rating <= 3:
    increment = salary*10/100
elif rating >= 3.1 and rating <= 4:
    increment = salary*30/100
elif rating>=4.1 and rating <= 5:
    increment = salary *40/100
else:
    print('Invalid rating')
print('Increment salary: ',increment+salary)
'''
#========================================================================================

#3]basic salary = 20000
#So we have to calculate the
#HRA of basic salary = 20%
#TA of basic salary = 30%
#DA of basic salary = 45%

'''
basic_salary = 20000
sum=0
HRA = (basic_salary*(20 / 100))
print(HRA)
TA = (basic_salary*(30 /100))
print(TA)
DA = ((45 /100)*basic_salary)
print(DA)
sum=HRA+TA+DA
print(basic_salary-sum)
'''

#========================================================================================

#4] A company is transmitting data to another server. The data is in the form of numbers. To secure the data during transmission, they plan to obtain a security key that will be sent along with the data. The security key is identified as the count of the repeating digits in the data.

# Write an algorithm to find the security key for the data.

# Input:- 578378923

# The input consists of an integer data, representing the data to be transmitted.

# Output: 3 (The repated digits in the data are 7, 3 and 8. so the security key is 3)

# Print an integer representing the security key for the given data. If no data is repeated it should display

# -1

# Constraints

# NA
"""
nums = [5,7,8,3,7,8,9,2,3]
nums1 = []
for i in range (len(nums)):
    count = 0
    key = nums[i]
    j=i+1
    while j<len(nums):
        if key == nums[j]:
            nums1.append(key)
        j=j+1
print(len(nums1))

"""

# Another Method
'''
mylist = [5,7,8,3,7,8,9,2,3]
newdict = {}
for i in range(len(mylist)):
    count = 0
    key = mylist[i]
    j = 1
    while j < len(mylist):
        if key == mylist[j]:
            count += 1
        j += 1
    if count > 1:
        newdict[key] = count
max = newdict
print(max)
'''

#========================================================================================
# Student Management System

# 1. Add Student
# 2. Show Student
# 3. Update Student
# 4. Delete Student
# 5. Exit

# Select any choice

# StudentID    StudentRollNo    StudentName    StudentCity
# ---------------------------------------------------------               Show student
# 101          11               prashant       Nagpur
# ---------------------------------------------------------

# 4. Delete Student
# 5. Exit

# Select any choice3

# Enter student ID: 101

# Matched Student Data Are:

# 1 Student Roll No: 11
# 2 Student Name: prashant
# 3 Student City: Nagpur
# 4. Don't Want to Update

# Select Above Option To Update:
# Give a code
# make show table format and also add delete student option

import sys

class Student:

    def __init__(self, studentID, studentRollNo, studentName, studentCity):
        self.studentID = studentID
        self.studentRollNo = studentRollNo
        self.studentName = studentName
        self.studentCity = studentCity

    # Show Student Table
    def showStudent(self):

        print(f"{self.studentID:<12}{self.studentRollNo:<18}{self.studentName:<20}{self.studentCity}")

    # Update Student
    def updateStudent(self):

        print("\nMatched Student Data Are:\n")

        print("1. Student Roll No :", self.studentRollNo)
        print("2. Student Name :", self.studentName)
        print("3. Student City :", self.studentCity)
        print("4. Don't Want to Update")

        choice = int(input("\nSelect Above Option To Update: "))

        if choice == 1:
            self.studentRollNo = int(input("Enter New Student Roll No: "))
            print("Student Roll No Updated Successfully.")

        elif choice == 2:
            self.studentName = input("Enter New Student Name: ")
            print("Student Name Updated Successfully.")

        elif choice == 3:
            self.studentCity = input("Enter New Student City: ")
            print("Student City Updated Successfully.")

        elif choice == 4:
            print("No Update Performed.")

        else:
            print("Invalid Choice")



students = []

while True:

    print("\n========== Student Management System ==========")
    print("1. Add Student")
    print("2. Show Student")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = int(input("\nSelect Any Choice: "))

    # Add Student
    if choice == 1:

        studentID = int(input("Enter Student ID: "))
        studentRollNo = int(input("Enter Student Roll No: "))
        studentName = input("Enter Student Name: ")
        studentCity = input("Enter Student City: ")

        student = Student(studentID, studentRollNo, studentName, studentCity)

        students.append(student)

        print("Student Added Successfully.")

    # Show Student
    elif choice == 2:

        if students == []:
            print("No Student Found")

        else:
            print("\n--------------------------------------------------------------")
            print(f"{'StudentID':<12}{'StudentRollNo':<18}{'StudentName':<20}{'StudentCity'}")
            print("--------------------------------------------------------------")

            for student in students:
                student.showStudent()

            print("--------------------------------------------------------------")

    # Update Student
    elif choice == 3:

        studentID = int(input("Enter Student ID to Update: "))

        found = False

        for student in students:

            if student.studentID == studentID:

                found = True
                student.updateStudent()
                break

        if found == False:
            print("Student Not Found.")

    # Delete Student
    elif choice == 4:

        studentID = int(input("Enter Student ID to Delete: "))

        found = False

        for i, student in enumerate(students):

            if student.studentID == studentID:

                del students[i]

                found = True

                print("Student Deleted Successfully.")
                break

        if found == False:
            print("Student Not Found.")

    # Exit
    elif choice == 5:
        sys.exit()

    else:
        print("Invalid Choice. Please Try Again.")