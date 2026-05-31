def add_all(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

with open("numbers.txt", "r") as file:
    total = 0   
    for line in file:
        total = total + int(line)
print("Sum:", total)
