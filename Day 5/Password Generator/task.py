# The objective is to take the inputs from the user to these questions and then generate a random password. Use your knowledge about Python lists and loops to complete the challenge.
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Easy level
# password = ""

# for option in range(0, nr_letters):
#     password += random.choice(letters)

# for option in range(0, nr_symbols):
#     password += random.choice(symbols)

# for option in range(0, nr_numbers):
#     password += random.choice(numbers)

# print(f"Your password is: {password}")

# Hard level
hard_password = []

for option in range(0, nr_letters):
    hard_password.append(random.choice(letters))

for option in range(0, nr_symbols):
    hard_password.append(random.choice(symbols))

for option in range(0, nr_numbers):
    hard_password.append(random.choice(numbers))

random.shuffle(hard_password)

final_password = ""

for character in hard_password:
    final_password += character

print(f"Your password is: {final_password}")


