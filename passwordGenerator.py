import random
import os.path

chars = 'qwertyuioplkjhgfdsazxcvbnmMLPOKNJIUHBVGYTFCXDRESZAWQ1234567890!@#$%^&*'

number = input('Number of passwords? - ')
number = int(number)

length = input('Password length? - ')
length = int(length)

for passEach in range(number):
    password = ''
    for character in range(length):
        password += random.choice(chars)

    file = open("passwordsList.txt", 'a')
    passWrd = "Password = " + password + "\n"
    file.write(passWrd)
    file.write("\n")


    