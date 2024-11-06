import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def generatePassword(letters_count, symbols_count, numbers_count):
    max_count = max([letters_count, symbols_count, numbers_count])
    password_list = []
    for i in range(0, max_count):

        if i < letters_count:
            password_list.append(random.choice(letters))

        if i < symbols_count:
            password_list.append(random.choice(symbols))

        if i < numbers_count:
            password_list.append(random.choice(numbers))

    return password_list