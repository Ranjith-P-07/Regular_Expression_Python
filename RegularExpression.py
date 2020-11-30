# Created by Ranjith P at 30-11-2020
import re

pattern = "^[A-Z]{1}[a-z]{3,}$"
user_input = input("Enter your First Name : ")

if re.search(pattern, user_input):
    print("Valid First Name ")
else:
    print("Invalid First Name")

pattern1 = "^[A-Z]{1}[a-z]{3,}$"
user_input1 = input("Enter your Last Name : ")

if re.search(pattern1, user_input1):
    print("Valid Last Name")
else:
    print("Invalid Last Name")
