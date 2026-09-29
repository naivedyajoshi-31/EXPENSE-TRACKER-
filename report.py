def total(expenses):
    return sum(e["amount"] for e in expenses)


def category_report(expenses):
    report = {}

    for e in expenses:
        category = e["category"]
        report[category] = report.get(category, 0) + e["amount"]

    for category, amount in report.items():
        print(category, ":", amount)