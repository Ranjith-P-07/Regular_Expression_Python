# Created by Ranjith P at 30-11-2020
import re

pattern = "^[A-Z]{1}[a-z]{3,}$"
user_input = input("Enter your Pattern : ")

if re.search(pattern, user_input):
    print("Valid First Name")
else:
    print("Invalid First Name")