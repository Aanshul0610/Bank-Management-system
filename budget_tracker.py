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
def main():
    data = load_from_file("budget.json")
    while True:
        print("\n1. Add transaction")
        print("2. Display transactions")
        print("3. Delete transaction")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")
        if choice == "1":
            data = add_transaction(data)
            #display_transactions(data)
        elif choice == "2":
            display_transactions(data)
        elif choice == "3":
            delete_transaction(data)
        elif choice == "4":
            break
if __name__ == "__main__":
    main()
