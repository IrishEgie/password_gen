letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

import random as rd

pass_len = nr_letters+nr_symbols+nr_numbers

rd_pass = []

for rep in range(nr_letters):
    rd_letter = rd.choice(letters)
    rd_pass.append(rd_letter) 
for rep in range(nr_numbers):
    rd_num = rd.choice(numbers)
    rd_pass.append(rd_num)
for rep in range(nr_symbols): 
    rd_sym = rd.choice(symbols)
    rd_pass.append(rd_sym) 

rd.shuffle(rd_pass)

password = ''.join(rd_pass)
print(f"Your password is: {password}")
