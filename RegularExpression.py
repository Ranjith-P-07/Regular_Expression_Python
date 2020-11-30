# Created by Ranjith P at 30-11-2020
import re


class UserRegestration:

    def validation(self, pattern, input):
        if re.search(pattern, input):
            return "Valid Input"
        else:
            return "Invalid Input"


if __name__ == '__main__':
    user = UserRegestration()
    name_pattern = "^[A-Z]{1}[a-z]{3,}$"
    email_pattern = "^[0-9a-zA-Z]+([._+-][0-9a-zA-Z]+)*@[0-9a-zA-Z]+.[a-zA-Z]{2,3}([.][a-zA-Z]{2})*$"
    phone_number_pattern = "^91 [0-9]{10}$"

    first_name = input("Enter the First Name : ")
    print(user.validation(name_pattern, first_name))
    last_name = input("Enter your Last Name: ")
    print(user.validation(name_pattern, last_name))
    user_email = input("Enter your Email Address : ")
    print(user.validation(email_pattern, user_email))
    phone_number = input("Enter your Phone number : ")
    print(user.validation(phone_number_pattern, phone_number))