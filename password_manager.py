from cryptography.fernet import Fernet

# KEY

def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)


def load_key():
    with open("key.key", "rb") as file:
        key = file.read()
    return key


# create key only if it doesn't exist
import os
if not os.path.exists("key.key"):
    write_key()

key = load_key()
fer = Fernet(key)

#MASTER PASsword

master_pwd = input("What is the master password? ")

#ADD PASSWORD

def add():
    name = input("Account name: ")
    pwd = input("Password: ")

    encrypted_pwd = fer.encrypt(pwd.encode()).decode()

 # there are 3 types of model w,r,a, w rwrites the model r only reads the model amd r add the file besides an existing file
    with open("passwords.txt", "a") as file:
        file.write(name + "|" + encrypted_pwd + "\n")

    print("Password saved securely !")


# VIEW PASSWORDS

def view():
    if not os.path.exists("passwords.txt"):
        print("No passwords saved yet.")
        return

    with open("passwords.txt", "r") as file:
        for line in file.readlines():
            data = line.rstrip()
            user, encrypted_pwd = data.split("|")

            decrypted_pwd = fer.decrypt(encrypted_pwd.encode()).decode()

            print("User:", user, "| Password:", decrypted_pwd)


# MAIN LOOP

while True:
    mode = input(
        "\nWould you like to add a new password or view existing ones? (add/view), press q to quit: "
    ).lower()

    if mode == "q":
        break

    elif mode == "add":
        add()

    elif mode == "view":
        view()

    else:
        print("Invalid mode.")