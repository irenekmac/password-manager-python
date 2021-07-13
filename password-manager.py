pwd = input("what is the master password? ")

# Python function = 'def'
def view():
    pass
# get user account and password and add into file
def add()
    name = input("Account Name: ")
    pwd = input("Password: ")

# 'with' will automatically close the file - 'a' is a pen mode and edit, view or create new
     with open(passwords.txt, "a") as f:
         f.write(name + "|" + pwd)


while True:
    mode = input("Would you like to add a new password or view existing passwords (view, add), press q to quit? ").lower
    if mode == "q":
        break
    if mode == "view":
        view()
    elif passwordelif mode == "add":
        add()
    else:
        print("Invalid mode.")
        continue
