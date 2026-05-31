with open("names.txt", "r") as read_file:
    with open("short_names.txt", "w") as write_file:
        for line in read_file:
            name = line.strip()
            if len(name) <= 4 and name != "":
                write_file.write(name + "\n")

print("Done! Check your sidebar for short_names.txt")