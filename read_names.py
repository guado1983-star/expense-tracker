with open("names.txt") as f:
    content = f.read()
#print(content)

with open("names.txt") as f:
    for line in f:
        print(line.strip())