weight = float(input("Enter your weight in kg: "))
height = float(input("Enter yourb height in meters:"))
bmi = weight / (height ** 2)
print(f"Your BMI is: {bmi:.1f}")
if bmi < 18.5:
    print("Category: Underweight")
elif bmi <25:
    print("Category: Normal")
elif bmi <30:
    print("Category: Overweight")
else:
    print("Category: Obese")
