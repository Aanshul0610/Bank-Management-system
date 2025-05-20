import json
from datetime import datetime, date
from unicodedata import category


def load_from_file(filename):
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}
def save_to_file(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f)
def add_transaction(data):
    t_type = input("Type (income/expense): ").strip().lower()
    category = input("Category (e.g., food, rent): ").strip()
    amount = float(input("Amount: ").strip())
    date = input("Date (YYYY-MM-DD) or leave blank for today: ").strip()
    note = input("Optional note: ").strip()
    if not date:
        date = datetime.now().strftime("%d/%m/%Y")

    transaction = {
        "category": category,
        "amount": amount,
        "date": date,
        "note": note,
        "type": t_type
    }
    data[date] = data.get(date, []) + [transaction]
    save_to_file(data, "budget.json")
    print("Transaction added successfully!")
    return data
def display_transactions(data):
    for date, transactions in data.items():
        print(f"{date}:")
        for transaction in transactions:
            print(f"  {transaction['category']}: {transaction['amount']}")
        return data
    else:
        print("No transactions found.")
def delete_transaction(data):
    date = input("Enter the date of the transaction to delete: ")
    if date in data:
        del data[date]
        save_to_file(data, "budget.json")
        print("Transaction deleted successfully!")
        return data
    else:
        print("No transaction found for the given date.")
        return data
def view_balance(transactions):

    print("\n--- View Balance Options ---")
    print("1. View Total Balance")
    print("2. View Total Income")
    print("3. View Total Expenses")

    choice = input("Enter your choice (1/2/3): ").strip()

    total_income = sum(t['amount'] for t in transactions if t['type'] == 'income')
    total_expense = sum(t['amount'] for t in transactions if t['type'] == 'expense')
    balance = total_income - total_expense

    if choice == '1':
        print("\n====== Total Balance ======")
        print(f"Total Income   : ${total_income:.2f}")
        print(f"Total Expenses : ${total_expense:.2f}")
        print(f"Current Balance: ${balance:.2f}")

    elif choice == '2':
        print("\n====== Total Income ======")
        print(f"Total Income: ${total_income:.2f}")

    elif choice == '3':
        print("\n====== Total Expenses ======")
        print(f"Total Expenses: ${total_expense:.2f}")

    else:
        print("Invalid choice. Please select 1, 2, or 3.")
def main():
    data = load_from_file("budget.json")
    while True:
        print("\n1. Add transaction")
        print("2. Display transactions")
        print("3. Delete transaction")
        print("4. View Balance")
        print("5. Exit")
        choice = input("Enter your choice (1-4): ")
        if choice == "1":
            data = add_transaction(data)
            #display_transactions(data)
        elif choice == "2":
            display_transactions(data)
        elif choice == "3":
            delete_transaction(data)
        elif choice == "4":
            view_balance(data.get("transactions", []))
        elif choice == "5":
            break
if __name__ == "__main__":
    main()
