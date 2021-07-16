from cryptography.fernet import Fernet


'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)'''

# Load encrypted key
def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

master_pwd = input("what is the master password? ")
# encode() - takes string and change into bytes
key = load_key() + master_pwd.encode()
fer = Fernet(key)


# Python function = 'def'
def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("User: ",user, ", Password: ", str( fer.decrypt( passw.encode() ) ))


# get user account and password and add into file
def add():
    name = input("Account Name: ")
    pwd = input("Password: ")

# 'with' will automatically close the file - 'a' is a pen mode and edit, view or create new
    with open('passwords.txt', 'a') as f:
        f.write(name + " | " + str( fer.encrypt( pwd.encode() ) ) + "\n")


while True:
    mode = input("Would you like to add a new password or view existing passwords (view, add), press q to quit? ").lower()
    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
        continue
