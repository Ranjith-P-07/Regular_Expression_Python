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
    first_name = input("Enter the First Name :")
    print(user.validation(name_pattern, first_name))
    last_name = input("Enter your Last Name: ")
    print(user.validation(name_pattern, last_name))