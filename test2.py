def load_expenses():
    expenses = []
    try:
        with open("expenses.txt", "r") as file:
            for line_num, line in enumerate(file, start=1):
                line = line.strip()
                if not line:
                    continue
                parts = line.split(",")
                print(f"Line {line_num}: {parts}")  # show what's being parsed
                expense = {
                    "name": parts[0].strip(),
                    "amount": float(parts[1].strip()),
                    "category": parts[2].strip()
                }
                expenses.append(expense)
    except Exception as e:
        print(f"ERROR on load: {e}")
    return expenses

expenses = load_expenses()
print(f"\nLoaded {len(expenses)} expenses:")
for e in expenses:
    print(e)