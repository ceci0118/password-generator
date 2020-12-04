#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

myletters = []
for l in range(1,nr_letters +1):
  myletters.append(random.choice(letters))

mysymbols = []
for s in range(1,nr_symbols +1):
  mysymbols.append(random.choice(symbols))

mynumbers = []
for n in range(1,nr_numbers +1):
  mynumbers.append(random.choice(numbers))

total = myletters+mysymbols+mynumbers
password = []

for i in total:
  password.append(random.choice(total))

print(f"Your password could be {''.join(password)}")
