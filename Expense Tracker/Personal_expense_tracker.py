#Personal Expense Tracker

expenses=[]

#---File handling---
def load_expenses():
    try:
        with open("expenses.txt","r") as file:
            for line in file:
                amount,category,date=line.strip().split(",")
                expenses.append({
                    "amount":float(amount),
                    "category":category,
                    "date":date
                })
    except FileNotFoundError:
        print("File not exist")

def save_expenses():
    with open("expenses.txt","w") as file:
        for expense in expenses:
            file.write(f"{expense['amount']},{expense['category']},{expense['date']}\n")

#---Functions---
def add_expense(): #Add expense
    amount = float(input("Enter amount: "))
    category = input("Enter category: ")
    date = input("Enter date (DD-MM-YYYY): ")

    expenses.append({
        "amount": amount,
        "category": category,
        "date": date
    })
    print("✅ Expense added successfully!")

def view_expenses(): #view expense
    if not expenses:
        print("No expenses to show.")
        return

    print("\nAmount      Category        Date")
    print("-" * 35)
    for exp in expenses:
        print(f"{exp['amount']:<10} {exp['category']:<15} {exp['date']}")
    print()

def search_expenses(): #search expense
    choice = input("Search by Category or Date? (c/d): ").lower()

    if choice == 'c':
        cat = input("Enter category: ")
        for exp in expenses:
            if exp["category"].lower() == cat.lower():
                print(f"Amount:{exp['amount']}  Category:{exp['category']}  Date:{exp['date']}")

    elif choice == 'd':
        date = input("Enter date (DD-MM-YYYY): ")
        for exp in expenses:
            if exp["date"] == date:
                print(f"Amount:{exp['amount']}  Category:{exp['category']}  Date:{exp['date']}")

    else:
        print("Invalid choice!")


def total_spent(): #total expense
    total = sum(exp["amount"] for exp in expenses)
    print(f"💰 Total Amount Spent: {total}")

#---Main---
load_expenses()

while True:
    print("\n--- Personal Expense Tracker ---")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. Search Expenses")
    print("4. Show Total Spent")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        search_expenses()
    elif choice == "4":
        total_spent()
    elif choice == "5":
        save_expenses()
        print("📁 Expenses saved. Goodbye!")
        break
    else:
        print("❌ Invalid choice. Try again.")