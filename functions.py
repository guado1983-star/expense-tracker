# def greet(name,greeting):
#     print(f"{greeting},{name}")
# greet("alice","hello")
# greet("bob","hey") 
# def add(a,b):
#     return a+b
# x = add(3,5)
# y = add(10,20)
# z = add(x,y)
# print(z)
# def add_print(a,b):
#     print(a+b)
# x = add_print(3,5)
# print(x)
# def square(number):
#     return number * number
# result = square(8)
# print(result)
def calculate_tip(bill,tip_percent):
    tip = bill * tip_percent/100
    total = bill + tip
    return total
my_total = calculate_tip(50,20)
print(f"you owe: ${my_total:.2f}")
print(my_total)
