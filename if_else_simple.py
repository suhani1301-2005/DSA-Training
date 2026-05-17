a=int(input("Enter any single digit number: "))
if a > 0:
    print(" Positive number")
if a < 0:
    print("Negative number")
if a == 0:
    print("Zero")

# Question: monday to friday is a working day and saturday and sunday is a holiday.Either in uppercase or lower case
day=input("Enter the day either in uppercase or lowercase:")
 
if day=="sunday" or day=="saturday" or day == "SATURDAY" or day == "SUNDAY":
    print("WEEKEND")
else:
    print("WORKING DAYS")



