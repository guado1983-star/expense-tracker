attempts = 0 
password = input("Enter password: ")

while password != "python123":
    attempts = attempts + 1
    if attempts >= 3:
        print("Account locked.")
        break
    print("Wrong password, try again.")
    password = input("Enter password: ")

if password == "python123":
    print("Access granted.")