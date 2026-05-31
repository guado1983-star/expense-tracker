with open("squares.txt", "w") as f:
    for i in range(1, 11):
        f.write(f"{i**2}\n")
print("done")
with open("squares.txt","a") as f:
    f.write('this line is appended')