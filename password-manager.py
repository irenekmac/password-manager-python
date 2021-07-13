pwd = input("what is the master password? ")

while True:
    mode = input("Would you like to add a new password or view existing passwords (view, add), press q to quit? ").lower
    if mode == "q":
        break
    if mode == "view":
        pass
    elif passwordelif mode == "add":
        pass
    else:
        print("Invalid mode.")
        continue
