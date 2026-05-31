with open("numbers.txt", "r") as file:
    total_sum = 0
    for line in file:
        total_sum += int(line.strip())

print(total_sum)