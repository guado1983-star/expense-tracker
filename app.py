import csv
import os
from datetime import datetime

EXPENSES_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "expenses.txt")
EXPORT_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "expenses_export.csv")

def load_expenses():
    expenses = []
    if not os.path.exists(EXPENSES_FILE):
        return expenses
    with open(EXPENSES_FILE, "r") as f:
        for i, line in enumerate(f, 1):
            line = line.strip()
            if not line:
                continue
            parts = line.split(",", 3)
            if len(parts) != 4:
                continue
            try:
                date_str = parts[3].strip()
                datetime.strptime(date_str, "%Y-%m-%d")
                expenses.append({
                    "name": parts[0].strip(),
                    "amount": float(parts[1].strip()),
                    "category": parts[2].strip(),
                    "date": date_str
                })
            except ValueError:
                continue
    print(f"{len(expenses)} expenses loaded.")
    return expenses

def save_expenses(expenses):
    try:
        with open(EXPENSES_FILE, "w") as f:
            for e in expenses:
                f.write(f"{e['name']},{e['amount']:.2f},{e['category']},{e['date']}\n")
    except Exception as ex:
        print(f"[ERROR] Could not save expenses: {ex}")

def add_expense(expenses):
    name = input("Expense name: ").strip()
    if not name:
        input("Name cannot be empty. Press Enter...")
        return
    try:
        amount = float(input("Amount: ").strip())
    except ValueError:
        input("Invalid amount. Press Enter...")
        return
    if amount <= 0:
        input("Amount must be greater than zero. Press Enter...")
        return
    category = input("Category: ").strip()
    if not category:
        input("Category cannot be empty. Press Enter...")
        return
    date_input = input("Date (YYYY-MM-DD): ").strip()
    try:
        datetime.strptime(date_input, "%Y-%m-%d")
    except ValueError:
        input("Invalid date format. Expense not saved. Press Enter...")
        return
    for e in expenses:
        if (e['name'].lower() == name.lower() and
            e['amount'] == amount and
            e['category'].lower() == category.lower() and
            e['date'] == date_input):
            confirm = input("Duplicate exists. Add anyway? (y/n): ").strip().lower()
            if confirm != "y":
                input("Expense not added. Press Enter...")
                return
            break
    expenses.append({"name": name, "amount": amount, "category": category, "date": date_input})
    input("Expense added! Press Enter...")

def show_expenses(expenses):
    if not expenses:
        input("No expenses recorded. Press Enter...")
        return
    output = "\n--- All Expenses ---\n"
    for i, e in enumerate(expenses, 1):
        output += f"{i}. {e['name']}: ${e['amount']:.2f} | {e['category']} | {e['date']}\n"
    input(output + "\nPress Enter to continue...")

def show_total(expenses):
    if not expenses:
        input("No expenses recorded. Press Enter...")
        return
    input(f"\nTotal: ${sum(e['amount'] for e in expenses):.2f}\n\nPress Enter to continue...")

def show_total_by_category(expenses):
    if not expenses:
        input("No expenses recorded. Press Enter...")
        return
    totals = {}
    for e in expenses:
        totals[e['category']] = totals.get(e['category'], 0.0) + e['amount']
    output = "\n--- By Category ---\n"
    for cat, total in totals.items():
        output += f"  {cat}: ${total:.2f}\n"
    input(output + "\nPress Enter to continue...")

def show_expenses_by_month(expenses):
    if not expenses:
        input("No expenses recorded. Press Enter...")
        return
    months = {}
    for e in expenses:
        key = e['date'][:7]
        months[key] = months.get(key, 0.0) + e['amount']
    output = "\n--- By Month ---\n"
    for month, total in sorted(months.items()):
        output += f"  {month}: ${total:.2f}\n"
    input(output + "\nPress Enter to continue...")

def delete_expense(expenses):
    if not expenses:
        input("No expenses to delete. Press Enter...")
        return
    output = "\n--- Select Expense to Delete ---\n"
    for i, e in enumerate(expenses, 1):
        output += f"{i}. {e['name']}: ${e['amount']:.2f} | {e['category']} | {e['date']}\n"
    print(output)
    try:
        choice = int(input("Enter number to delete: "))
        if 1 <= choice <= len(expenses):
            removed = expenses.pop(choice - 1)
            input(f"Deleted: {removed['name']}. Press Enter...")
        else:
            input("Invalid number. Press Enter...")
    except ValueError:
        input("Please enter a valid number. Press Enter...")

def search_expenses(expenses):
    if not expenses:
        input("No expenses to search. Press Enter...")
        return
    query = input("Search keyword (searches name, category, date): ").strip().lower()
    results = [e for e in expenses if
               query in e['name'].lower() or
               query in e['category'].lower() or
               query in e['date']]
    output = f"\n--- Results for '{query}' ---\n"
    if results:
        for e in results:
            output += f"  {e['name']}: ${e['amount']:.2f} | {e['category']} | {e['date']}\n"
    else:
        output += "No results found.\n"
    input(output + "\nPress Enter to continue...")

def edit_expense(expenses):
    if not expenses:
        input("No expenses to edit. Press Enter...")
        return
    output = "\n--- Select Expense to Edit ---\n"
    for i, e in enumerate(expenses, 1):
        output += f"{i}. {e['name']}: ${e['amount']:.2f} | {e['category']} | {e['date']}\n"
    print(output)
    try:
        choice = int(input("Enter number to edit: ").strip())
        if not (1 <= choice <= len(expenses)):
            input("Invalid number. Press Enter...")
            return
    except ValueError:
        input("Please enter a valid number. Press Enter...")
        return
    e = expenses[choice - 1]
    print(f"\nEditing: {e['name']} | ${e['amount']:.2f} | {e['category']} | {e['date']}")
    print("Press Enter to keep the current value for any field.\n")
    new_name = input(f"Name [{e['name']}]: ").strip()
    if new_name:
        e['name'] = new_name
    new_amount = input(f"Amount [{e['amount']:.2f}]: ").strip()
    if new_amount:
        try:
            new_amount_float = float(new_amount)
            if new_amount_float <= 0:
                input("Amount must be greater than zero — keeping original. Press Enter...")
            else:
                e['amount'] = new_amount_float
        except ValueError:
            input("Invalid amount — keeping original. Press Enter...")
    new_category = input(f"Category [{e['category']}]: ").strip()
    if new_category:
        e['category'] = new_category
    new_date = input(f"Date [{e['date']}] (YYYY-MM-DD): ").strip()
    if new_date:
        try:
            datetime.strptime(new_date, "%Y-%m-%d")
            e['date'] = new_date
        except ValueError:
            input("Invalid date format — keeping original. Press Enter...")
    input("\nExpense updated successfully! Press Enter...")

def export_to_csv(expenses):
    if not expenses:
        input("No expenses to export. Press Enter...")
        return
    try:
        with open(EXPORT_FILE, "w", newline="", encoding="utf-8-sig") as f:
            writer = csv.DictWriter(f, fieldnames=["name", "amount", "category", "date"])
            writer.writeheader()
            writer.writerows(expenses)
        input(f"Exported {len(expenses)} expenses to:\n{EXPORT_FILE}\n\nPress Enter...")
    except Exception as ex:
        input(f"[ERROR] Could not export: {ex}\nPress Enter...")

def main():
    expenses = load_expenses()
    while True:
        print("\n--- Expense Tracker ---")
        print("1.  Add Expense")
        print("2.  Show All Expenses")
        print("3.  Show Total")
        print("4.  Show Total by Category")
        print("5.  Delete Expense")
        print("6.  Search Expenses")
        print("7.  Show by Month")
        print("8.  Edit Expense")
        print("9.  Export to CSV")
        print("10. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_expense(expenses)
            save_expenses(expenses)
        elif choice == "2":
            show_expenses(expenses)
        elif choice == "3":
            show_total(expenses)
        elif choice == "4":
            show_total_by_category(expenses)
        elif choice == "5":
            delete_expense(expenses)
            save_expenses(expenses)
        elif choice == "6":
            search_expenses(expenses)
        elif choice == "7":
            show_expenses_by_month(expenses)
        elif choice == "8":
            edit_expense(expenses)
            save_expenses(expenses)
        elif choice == "9":
            export_to_csv(expenses)
        elif choice == "10":
            save_expenses(expenses)
            print("Goodbye!")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()