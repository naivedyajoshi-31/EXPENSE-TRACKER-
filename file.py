def save(expenses):
    with open("expenses.txt", "w") as f:
        for e in expenses:
            f.write(
                f"{e['amount']}|{e['category']}|{e['note']}\n"
            )


def load():
    expenses = []

    try:
        with open("expenses.txt", "r") as f:
            for line in f:
                amount, category, note = line.strip().split("|")
                expenses.append({
                    "amount": float(amount),
                    "category": category,
                    "note": note
                })
    except FileNotFoundError:
        pass

    return expenses