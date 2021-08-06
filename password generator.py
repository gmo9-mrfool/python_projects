# Password Generator

print('''
╔═══╗                            ╔╗    ╔═══╗                     ╔╗        
║╔═╗║                            ║║    ║╔═╗║                    ╔╝╚╗       
║╚═╝║╔══╗ ╔══╗╔══╗╔╗╔╗╔╗╔══╗╔═╗╔═╝║    ║║ ╚╝╔══╗╔═╗ ╔══╗╔═╗╔══╗ ╚╗╔╝╔══╗╔═╗
║╔══╝╚ ╗║ ║══╣║══╣║╚╝╚╝║║╔╗║║╔╝║╔╗║    ║║╔═╗║╔╗║║╔╗╗║╔╗║║╔╝╚ ╗║  ║║ ║╔╗║║╔╝
║║   ║╚╝╚╗╠══║╠══║╚╗╔╗╔╝║╚╝║║║ ║╚╝║    ║╚╩═║║║═╣║║║║║║═╣║║ ║╚╝╚╗ ║╚╗║╚╝║║║ 
╚╝   ╚═══╝╚══╝╚══╝ ╚╝╚╝ ╚══╝╚╝ ╚══╝    ╚═══╝╚══╝╚╝╚╝╚══╝╚╝ ╚═══╝ ╚═╝╚══╝╚╝ 




''')
import random

system_random = random.SystemRandom()
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
password = []
for l in range(1, nr_letters + 1):
    password.append(system_random.choice(letters))
for s in range(1, nr_symbols + 1):
    password.append(system_random.choice(symbols))
for n in range(1, nr_numbers + 1):
    password.append(system_random.choice(numbers))
# print(password)
system_random.shuffle(password)
string1 = "".join(map(str, password))
print('Your password is: ' + string1)
