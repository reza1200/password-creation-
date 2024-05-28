#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
#list1 = letters+numbers+symbols
#print(list1)
print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))
     
#difinding an empty list to hold the password
password_list = []

#looping throught the letters,numbers and symbpls list and adding the random letters to the password list
for letter in range(1,nr_letters+1):
  password_list.append(random.choice(letters))
for symbol in range(1,nr_symbols+1):
  password_list.append(random.choice(symbols))
for num in range(1,nr_numbers+1):
  password_list.append(random.choice(numbers))

#Shuffleing the password list 
random.shuffle(password_list)
#converting the list to a string
password=''.join(password_list)
print(f"Your password is = {password}")



      