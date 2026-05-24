#static method and class method
'''
class Student:
    #by using class name we can access static method
    def get_personal_detail(firstname,lastname):
        print("Your personal detail=",firstname,lastname)

    @staticmethod
    def contact_detail(mobile_no , roll_no):
        print("Your contact detail = ",mobile_no , roll_no)

Student.get_personal_detail("Suhani" , "Saxena")
Student.contact_detail(8090474874,1001)
'''

#==============================================================================================

# Single level inheritance
'''
class College:      # parent class

    def college_name(self):      # member function of college
        print("Modern College")


class Student(College):      # child class

    def student_info(self):      # member function
        print("Name: Suhani saxena")
        print("Branch: Mechanical")


obj = Student()      # object create child class

obj.college_name()
obj.student_info()
'''
#==============================================================================================

# Multilevel inheritance
'''
class College:      # first class (first level)

    def college_name(self):
        print("Modern College")

class Student(College):      # second class (second level)

    def student_info(self):
        print("Name: Suhani saxena")
        print("Branch: Mechanical")

class Exam(Student):      # child class

    def subject(self):
        print("Subject1: Design Engineering")
        print("Subject2: Math")
        print("Subject3: C-Language")

obj = Exam()

obj.college_name()
obj.student_info()
obj.subject()
'''
#==============================================================================================

# Multiple inheritance
'''
class SubMarks:      # class-1

    math = int(input("Enter paper marks of math : "))
    DE = int(input("Enter paper marks of design engineering : "))
    c = int(input("Enter paper marks of c language : "))
    english = int(input("Enter paper marks of english : "))
# parent class -1

class PractMarks:      # class-2

    cpract = int(input("Enter practical marks of c language : "))
# parent class -2

class Result(SubMarks, PractMarks):      # child class

    def total(self):

        if self.math >= 40 and self.DE >= 40 and self.c >= 40 and self.english >= 40 and self.cpract >= 20:

            print("pass")

        else:
            print("fail")


obj = Result()

obj.total()
'''

#==============================================================================================
'''
class A:
    def add(self,a):
        print("The sum is 5")

class B:
    def add(self,a):
        print("The sum is 10")

class C(A,B):
    def display(self):

        print("This is a default statement")

obj = C
obj.display()
'''

#==============================================================================================
#method Overriding  
'''
class Rbi:
    def home_loan(self):
        print("Home loan ROI = 8%")

    def education_loan(self):
        print("Education lone ROI = 9%")

class SBI(Rbi):
    def education_loan(self):
        print("Education lone ROI = 10%")
        super().education_loan()

obj = SBI()
obj.education_loan()
'''
#==============================================================================================

# ====================== Constructor overloading ============================

class Rbi:
    def __init__(self):
        print("parent class constructor")

class Sbi(Rbi):
    def __init__(self):
        print("child class constructor")

obj = Sbi()