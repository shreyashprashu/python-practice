from math import *

character_name = "Tom"
character_age = 20
phrase = "Peaky Blinders"
is_male = False
if is_male is True:
    character_age = 29
else:
    character_age = 30

# character_name ="shreyash"
print("there was a man named \n" + character_name + ",")
print("he was ", character_age, " years old.")
character_name = "\"shreyash\""
character_age = 29
print("he liked the name "+character_name + ",")
print("but he didn't like the age ", character_age, is_male)
print(phrase.upper() + " is cool")
phrase = phrase.upper()
print(phrase.isupper())
print(len(phrase))
print(phrase[4])
print(phrase.index("Y"))
print(phrase.replace("PEAKY", "SMOKY"))
print(2*(8.5-67))
print(str(67))
print(round(5.50))
print(abs(-4))
print(pow(2, 35))
print(sqrt(121))

name = input("Enter your name: ")
if name.isnumeric():
    print("please enter a valid name")
else:
    print("Hi " + name + "!")
age = input("Enter your age: ")
# print("Hi " + name + "!")
print("You are " + age)