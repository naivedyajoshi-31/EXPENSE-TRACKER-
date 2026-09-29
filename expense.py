def add_expense(expenses):
    try:
        amount = float(input("Amount: "))
        category = input("Category: ")
        note = input("Description: ")

        expenses.append({
            "amount": amount,
            "category": category,
            "note": note
        })
        print("Expense added!")
    except ValueError:
        print("Invalid amount.")


def show_expenses(expenses):
    if not expenses:
        print("No expenses.")
        return

    for i, e in enumerate(expenses, 1):
        print(i, e["amount"], e["category"], e["note"])


def delete_expense(expenses):
    show_expenses(expenses)

    try:
        n = int(input("Enter number to delete: "))
        if 1 <= n <= len(expenses):
            expenses.pop(n - 1)
            print("Deleted!")
        else:
            print("Invalid number.")
    except ValueError:
        print("Invalid input.")