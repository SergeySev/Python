import random
import secrets
from pprint import PrettyPrinter
import re

from password_db import file_to_list, write_to_file, db_file

pp = PrettyPrinter()


def generate_password(length=10):
    """ This function creates a password and return it"""
    password = ''.join(chr(random.randint(32, 127)) for i in range(length))
    return password


def secret_password(length=10):
    """ This function creates a secret password and return it"""
    my_secret_pass = ''.join(chr(secrets.choice(range(32, 127))) for i in range(length))
    return my_secret_pass


def list_website(data):
    i = 0
    while i < len(data):
        print(i + 1, data[i]['Site'])
        i += 1
    print("Input '+' for adding a new website login and password")
    print("Input '-' for deleting a choosen website login and password")


def get_login(data):
    # Just prints every Site and its number
    while True:
        list_website(data)
        ask = input("Input some digit for getting login website or chose some options:\n>")
        if not ask:
            break
        print('_' * 30)
        if ask == '+':
            while site_input := input("Text a new website:\n> "):
                if site_input == '':
                    print("Incorrect input. Site must not be empty!!!")
                    continue
                break
            while login_input := input("Text a new login:\n> "):
                if login_input == '':
                    print("Incorrect input. Login must not be empty!!!")
                    continue
                break
            while password_input := input("Text a new password:\n> "):
                if password_input == '':
                    print("Incorrect input. Password must not be empty!!!")
                    continue
                break

            data_new = {"Site": site_input, "login": login_input, "password": password_input}
            write_to_file(db_file, data_new)
            data.append(data_new)
            print("The data was successfully added")
            continue

        if num_website := re.fullmatch("- *(\d+)", ask):
            num_website = num_website.group(1)
            num_website = int(num_website) - 1
            data.pop(num_website)
            write_to_file(db_file, data, 'w')
            continue


        if not ask.isnumeric():
            print("Incorrect input. You should use only digits")
            continue

        # i - index of login and password. Must be greater than 0 and less than elements in the list
        i = int(ask) - 1
        if i < 0 or i > len(data) - 1:
            print(f"Please, input number from 1 to {len(data) + 1}. Or press Enter to exit")
            print("_" * 30, "\n")
            continue

        print("The data for", data[i]['Site'] + ":")
        print("Login:", data[i]['login'])
        print("Password:", data[i]['password'])
        print("_"*30, "\n")



if __name__ == "__main__":
    data = file_to_list()
    get_login(data)





