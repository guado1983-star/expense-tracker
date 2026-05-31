student = {
    "name": "Lupe",
    "age": 21,
    "grade": "A",
    "city": "Austin"}

# Print just the name and grade
print("Name:", student["name"])
print("Grade:", student["grade"])

# Add a new key: email
student["email"] = "lupe@example.com"

# Change the grade
student["grade"] = "A+"

# Print the final dictionary
print("\nFinal student record:")
print(student)