#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

random_letters = []
for n in range(0, nr_letters):
  random_letter = random.choice(letters) 
  random_letters.append(random_letter)
print(random_letters)

random_symbols = []
for n in range(0, nr_symbols):
  random_symbol = random.choice(symbols)
  random_symbols.append(random_symbol)
print(random_symbols)

random_numbers = []
for n in range(0, nr_numbers):
  random_number = random.choice(numbers)
  random_numbers.append(random_number)
print(random_numbers)

password_chars = random_letters + random_symbols + random_numbers
print(password_chars)

# easy mode
password_str = ''
for c in password_chars:
  password_str += c
print(password_str)

# hard mode done easy
# pythonic alternative is using list.shuffle()
# random.shuffle(password_chars)
# print(password_chars)

# hard mode
randomised_pass = []
for c in range(0, len(password_chars)):
  random_index_password_char = random.randint(0, len(password_chars)-1)
  char = password_chars.pop(random_index_password_char)
  print(password_chars)
  randomised_pass.append(char)
print(randomised_pass)

randomised_password_str = ''
for c in randomised_pass:
  randomised_password_str += c
print(randomised_password_str)
