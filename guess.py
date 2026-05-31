secret = 7
guess = int(input("Guess a number 1-10: "))



while guess != secret:
    print("Wrong! Try again.")
    guess = int(input("Guess again: "))



print("You got it!")
total = 0
for i in range(5):
    number = float(input(f"Enter number {i + 1}: "))
    total = total + number 
print(f"Total: {total}")
print(f"Average: {total / 5}")
