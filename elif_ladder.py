# per = 65
# if per >= 65:
#     print("Grade A")
# elif per <=65 and per >= 50:
#     print("Grade B")
# else:
#     print("Fail")

#Identify if the entered varibale is uppercase/lowercase/digit/special Character
#A-Z= 65-90
#a-z= 97-
#48-57 : digits
#ord function is used to type cast the value into ascii code

chr = ord(input("Enter any one character :"))
if chr >= 65 and chr <= 90:
    print("Upper case")
elif chr >= 97 and chr <= 122:
    print("Lower case")
elif chr >= 48 and chr <= 57:
    print("Digit")
else:
    print("Special Character")