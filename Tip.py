while True:
    try:
        bill = float(input("Enter the bill amount: $"))
        if bill <= 0:
            print("Error: Bill must be greater than zero. Try again.")
            continue
        break
    except ValueError:
        print("Oops! Please enter a valid number, not letters.")
tip_percent=float(input("tip percent?"))
tip=bill*tip_percent/100
total=bill +tip
print("tip:",tip)
print("total:",total)
people=int(input("How manybpeople are splitting the bill?"))
total_with_tip= bill + tip
per_person = total_with_tip/ people
print(f"Total bill with tip: ${total_with_tip:.2f}")
print(f"Each person should pay: ${per_person:.2f}")
tip_amount = bill * (tip_percent / 100)
if bill< 10:
    tip_amount = max(tip_amount,2.0)
total = bill + tip_amount
per_person + total / people
print(f"Total bill with tip: ${total:.2f}")
print(f"Each person should pay: ${per_person: .2f}")
if tip_percent <15:
    print("Warning: low tip")
bill = float(input("Enter the bill amount: $"))
tip_percentage = float(input("Enter the tip percentage (e.g., 15, 20): "))
tip = bill * (tip_percentage / 100)
total = bill + tip


print(f"\nBill: ${bill:.2f}, Tip: ${tip:.2f}, Total: ${total:.2f}\n")


with open("tip_log.txt", "a") as file:
    file.write(f"Bill: ${bill:.2f}, Tip: ${tip:.2f}, Total: ${total:.2f}\n")

print("Saved to tip_log.txt!")