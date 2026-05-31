while True:
    filename = input("Enter the filename to open: ").strip()
    try:
        with open(filename, "r") as file:
            print(file.read())
        break
    except FileNotFoundError:
        print("File not found, try again")