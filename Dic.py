person = {"name": "Alice", "age": 30, "city": "New York"}
print(person["name"])
print(person["age"])
person_dict = {"name": "Alice", "job": "Engineer", "hobbies": ["reading", "hiking",
                                                                "coding"]}
person_dict["age"] = 30
print(person_dict)
if "email" in person_dict:
    print("Email:", person_dict["email"])
else:
    print("Email key not found.")
for key, value in person_dict.items():
    print(f"{key}: {value}")
products = [
    {"name": "Laptop", "price": 999.99, "stock": 10},
    {"name": "Smartphone", "price": 499.99, "stock": 20},
    {"name": "Headphones", "price": 199.99, "stock": 15}
]
for product in products:
    if product["stock"] > 0:
        print(f"{product['name']} is in stock at ${product['price']}.")
    else:
        print(f"{product['name']} is out of stock.")