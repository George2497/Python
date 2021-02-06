# Mini Project - Random Password Generator!

# Importing the relevant modules
from random import randint

# All uppercase password
password = ""
for i in range(10):
    i = chr(randint(65, 90))
    password = str(password) + i
print(password)

# Upper and lowercase password
password = ""
for i in range(5):  # i accounts for the uppercase letters in the password
    i = chr(randint(65, 90))
    for j in range(5):  # j accounts for the lowercase letters in the password
        j = chr(randint(65, 90)).lower()
    password = str(password) + i + j  # concatenates the string of the password of i and j
print(password)