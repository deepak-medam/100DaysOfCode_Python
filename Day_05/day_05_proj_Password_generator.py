import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 
'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 
'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


print("Welcome to PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?"))
nr_symbols = int(input("How many symbols would you like?"))
nr_numbers = int(input("How many numbers would you like?"))

# Picking random characters for password based on user input
pass_list = []
for letter_idx in range(0, nr_letters):
    pass_list.append(random.choice(letters))

for symbol_idx in range(0, nr_symbols):
    pass_list.append(random.choice(symbols))

for number_idx in range(0, nr_numbers):
    pass_list.append(random.choice(numbers))
rand_pswd = "".join(char for char in pass_list)

random.shuffle(pass_list)
strng_pswd = "".join(char for char in pass_list)
print(f"Here is your mixed password:{rand_pswd}. This is a strong password {strng_pswd}")