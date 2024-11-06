import random
import utils

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# generate password list
password_list = password.generatePassword(nr_letters, nr_symbols, nr_numbers)

# randomize password list
random.shuffle(password_list)

password = ""
for pwd in password_list:
    password += pwd

print(f"Your password is: {password}")
