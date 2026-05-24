'''
import csv
f = open("employee.csv",'a')
a = csv.writer(f)
#a.writerow(["EmpID" , "Emp name" , "Emp age"])
empid = int(input("Enter employee id : "))
empName = input("Enter employee name : ")
age = int(input("Enter employee age : "))
a.writerow([empid , empName , age])
print("File has created")
'''
#TASK
'''
col name = studId  | studName | physics | chemistry | maths | total | percentage | Result
input : studentid , studentname physics marks , chemistry marks , maths marks
calculate : total marks , percentage 
check condition all paper marks >= 40 pass else fail

    '''

import csv
f = open("student.csv", 'a')
a = csv.writer(f)
#a.writerow(["studID", "studName", "phy", "chem", "maths", "total", "percentage"])
studID = int(input("Enter the studID :"))
studName = input("Enter the studname :")
phy = int(input("Enter the phy :"))
chem = int(input("Enter the chem :"))
maths = int(input("Enter the maths :"))
total = phy+chem+maths
percent = (total/300)*100
a.writerow([studID,studName,phy,chem,maths,total,percent])
print("File has been created")