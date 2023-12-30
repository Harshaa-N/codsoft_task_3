import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!','@','#', '$', '%','^','&', '(', ')', '*']
password=[]
pw=""
print("Welcome to the PyPassword Generator!")
letter= int(input("How many letters would you like in your password? \n")) 
symbol = int(input("How many symbols would you like? \n"))
number = int(input("How many numbers would you like? \n"))
f=int(input("If you need a very strong password enter 1 else enter 0 \n"))
for i in range(0,letter):
  password.append(random.choice(letters))
for i in range(0,symbol):
  password.append(random.choice(symbols))
for i in range(0,number):
  password.append(random.choice(numbers))
 
if f==1:
  random.shuffle(password)
  for element in password:
    pw+=element
else:
  for element in password:
    pw+=element
print(f"Your password is {pw}")
