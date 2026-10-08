expenses = []

def add_expense():
    expense = {
        "name": input("Enter expense name: "),
        "amount": float(input("Enter amount: ")),
    }

    expenses.append(expense)
    print("Expense added successfully!")


def view_expense():
    if not expenses:
        print("No Expenses found.")
        return
    print("\n=== Expense ===")
    
    for expense in expenses:
        print(f"Name: {expense['name']} | Amount: ${expense["amount"]}")
    

def calculate_expense():
    # total = 0
    
    # for expense in expenses:
    #     total += expense['amount']
    
    total = sum(expense['amount'] for expense in expenses)
        
    print(f"Total Expense: ${total:.2f}")
     

while True:

    print("=== Expense Tracker ===")
    print("1. Add Expense")
    print("2. View Expense")
    print("3. Calculate Expense")
    print("4. Exit")
    choice = int(input("Choose your choice: "))

    if choice == 1:
        add_expense()

    elif choice == 2:
        view_expense()

    elif choice == 3:
        calculate_expense()
    
    elif choice == 4:
        print("Thank you for using Expense Tracker")
        break

    else:
        print("Invalid Choice")
