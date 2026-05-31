try:
    # 1. Get user inputs
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    operation = input("Enter operation (+, -, *, /): ").strip()

    # 2. Perform math based on the operation
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        result = num1 / num2  # Python triggers ZeroDivisionError here if num2 is 0
    else:
        result = "Invalid operation! Please use +, -, *, or /."

    # 3. Print the successful result
    print(f"Result: {result}")

except ValueError:
    # Triggers if the user types letters instead of numbers
    print("Oops! Please enter valid numbers, not letters or words.")

except ZeroDivisionError:
    # Triggers if the user tries to divide by 0
    print("Error: You cannot divide a number by zero!")
