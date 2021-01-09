import os.path
import random
import hashlib, binascii
import os
import base64

def storePassword():
    username = input("Username : ")
    website = input("Website : ")

    dictionary = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890#$%&!@"
    
    length = int(input("Password length = "))
    password = ""
    
    for char in range(length):
        character = random.choice(dictionary) 
        password += character

    #encoding the password in base64
    passBytes = password.encode('ascii')
    base64Bytes = base64.b64encode(passBytes)
    base64_password = base64Bytes.decode('ascii')
    #it outputs the base64 version of the actual password in the file / db

    passwordListFile = open("passList.txt" , "a")
 
    passwordListFile.write(
        "Website : "
        f"{website}"
        "\n"
        "Username : "
        f"{username}"
        "\n"
        "Password : "
        f"{base64_password}"
        "\n"
        "\n"
        "\n"
    )
    passwordListFile.close()


storePassword()