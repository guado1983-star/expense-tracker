try:
    age = int(input("Enter your age: "))
    if age < 0:
        raise ValueError("Age cannot be negative.")
    print("Your age is:", age)
except ValueError as e:
    print("thats not a number")

while True:
    try:
        age = int(input("Enter your age: "))
        break
    except ValueError as e:
        print("please enter a real number")