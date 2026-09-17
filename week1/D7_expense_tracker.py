"""
Day 7 — Week 1 Project: CLI Expense Tracker
Uses: functions, loops, conditionals, lists, dicts, f-strings, type hints
"""

# ── Data Store ────────────────────────────────────────────────────────────
# Each expense is a dict — mirrors real API/JSON response structures


expenses: list[dict[str, str | float]] = []

VALID_CATEGORIES: set[str] = {
    "food", "transport", "education",
    "entertainment", "health", "other"
}

#Menu options
def show_menu() -> None:
    print("\n=== Expense Tracker ===")
    print("1. Add expense")
    print("2. List all expenses")
    print("3. Filter by category")
    print("4. Summary")
    print("5. Exit")

def get_float_input(prompt: str ) -> float | None:
   
    raw = input(prompt).strip()
    try:
        return float(raw)
    except ValueError:
        print("Invalid input. Please enter a number.")
        return None


# Expense functions
def add_expense(amount : float , category: str, discription:str) -> dict:
    category  = category.lower().strip()

    if category not in VALID_CATEGORIES:
        print(f"Invalid Category. Valid categories are {', '.join(VALID_CATEGORIES)}")
        return {}

    if amount <= 0 :
        print("Amount must be greater than zero")
        return {}

    expense: dict [str , str | float] = {
        "amount" : amount,
        "category" : category,
        "description" : discription,
        "id" : len(expenses) + 1
    }
    expenses.append(expense)
    print(f"Added {amount} to {category} - {discription}")
    return expense

def list_expenses(data : list[dict] | None = None )->None:
    tgt = data if data is not None else expenses

    if not tgt:
        print("No expenses to show.")
        return

    print("\nID | Amount | Category | Description")
    print("-" * 40)
    for exp in tgt:
        print(f"{exp['id']} {exp['amount']} {exp['category']} {exp['description']}")
    print("-" * 55)
    print(f"{'TOTAL'} ₹{get_total(tgt)}\n")

"""Return total amount for given list or all expenses."""
def get_total(data : list[dict] | None = None) -> float:
    tgt = data if data is not None else expenses
    #return sum(exp["amount"] for exp in tgt)
    return sum(float(exp["amount"]) for exp in tgt)


def filter_by_category(category: str) -> list[dict]:
    category = category.lower().strip()
    return [exp for exp in expenses if exp["category"] == category]

def summary() -> None:
    """Print total spending per category."""
    if not expenses:
        print("No expenses to summarise.")
        return

    categories = sorted(set(str(exp["category"]) for exp in expenses))
    totals = {cat: get_total(filter_by_category(cat)) for cat in categories}

    print("\n=== Summary by Category ===")
    for cat, total in sorted(totals.items(), key=lambda x: x[1], reverse=True):
        print(f"  {cat:<15} ₹{total:>9.2f}")
    print(f"  {'TOTAL':<15} ₹{get_total():>9.2f}\n")


# Main


def main() -> None:
    print("Welcome to Expense Tracker")
    print(f"Categories: {', '.join(sorted(VALID_CATEGORIES))}")

    while True:
        show_menu()
        choice = input("Choose (1-5): ").strip()

        if choice == "1":
            amount = get_float_input("Amount (₹): ")
            if amount is None:
                continue
            category    = input("Category: ")
            description = input("Description: ")
            add_expense(amount, category, description)

        elif choice == "2":
            list_expenses()

        elif choice == "3":
            category = input("Category to filter: ")
            filtered = filter_by_category(category)
            if not filtered:
                print(f"No expenses in '{category}'.")
            else:
                list_expenses(filtered)

        elif choice == "4":
            summary()

        elif choice == "5":
            print("Goodbye.")
            break

        else:
            print("Invalid choice. Enter 1 to 5.")


if __name__ == "__main__":
    main()



















