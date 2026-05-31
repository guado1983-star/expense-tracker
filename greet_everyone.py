with open("names.txt") as f:
    for line in f:
        print(f"Hello, {line.strip()}!")