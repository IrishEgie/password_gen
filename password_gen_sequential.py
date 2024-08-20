letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

import random as rd

pass_len = nr_letters+nr_symbols
print("Your password is: ")
for rep in range(1,nr_letters+1):
    rd_l_num = rd.randint(0,len(letters)-1)
    pass_letters = letters[rd_l_num]
    print(pass_letters, end='')
for rep in range(1,nr_symbols+1):
    rd_s_num = rd.randint(0,len(symbols)-1)
    pass_symbols = symbols[rd_s_num]
    print(pass_symbols, end='')
for rep in range(1,nr_numbers+1):
    rd_n_num = rd.randint(0,len(numbers)-1)
    pass_num = numbers[rd_n_num]
    print(pass_num, end='')