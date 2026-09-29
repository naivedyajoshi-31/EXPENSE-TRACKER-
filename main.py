from expense import add_expense, show_expenses, delete_expense
from file import save, load
from report import total, category_report

expenses = load()

while True:
    print("\n--- EXPENSE TRACKER ---")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Delete Expense")
    print("4. Total Expense")
    print("5. Category Report")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_expense(expenses)

    elif choice == "2":
        show_expenses(expenses)

    elif choice == "3":
        delete_expense(expenses)

    elif choice == "4":
        print("Total: ₹", total(expenses))

    elif choice == "5":
        category_report(expenses)

    elif choice == "6":
        save(expenses)
        print("Thank you!")
        break

    else:
        print("Invalid choice.")