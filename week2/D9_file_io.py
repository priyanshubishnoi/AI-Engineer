import json
import csv
import os
from pathlib import Path

# ── Config Manager ────────────────────────────────────────────────────────

DEFAULT_CONFIG: dict = {
    "model":           "gpt-4o-mini",
    "temperature":     0.7,
    "max_tokens":      1000,
    "system_prompt":   "You are a helpful AI assistant.",
    "tags":            ["development"],
    "cost_per_1k_tokens": 0.00015,
}

CONFIG_PATH = Path("ai_config.json")


def save_config(config: dict, path: Path = CONFIG_PATH) -> None:
    """Save config dict to JSON file."""
    try:
        with open(path, "w", encoding="utf-8") as f:
            json.dump(config, f, indent=2)
        print(f"Config saved to {path}")
    except OSError as e:
        raise OSError(f"Could not write config: {e}") from e


def load_config(path: Path = CONFIG_PATH) -> dict:
    """Load config from JSON file. Returns default config if file missing."""
    if not path.exists():
        print(f"Config not found at {path} — using defaults.")
        return DEFAULT_CONFIG.copy()

    try:
        with open(path, "r", encoding="utf-8") as f:
            config = json.load(f)
        print(f"Config loaded from {path}")
        return config
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON in config file: {e}") from e


def update_config(updates: dict, path: Path = CONFIG_PATH) -> dict:
    """Load existing config, apply updates, save back."""
    config = load_config(path)
    config |= updates       # merge — updates override existing keys
    save_config(config, path)
    return config


# ── Expense Log — CSV ─────────────────────────────────────────────────────

EXPENSE_LOG = Path("expense_log.csv")
FIELDNAMES  = ["id", "amount", "category", "description"]


def log_expense(expense: dict) -> None:
    """Append one expense to CSV log."""
    file_exists = EXPENSE_LOG.exists()

    with open(EXPENSE_LOG, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        if not file_exists:
            writer.writeheader()        # write header only on first entry
        writer.writerow({k: expense.get(k, "") for k in FIELDNAMES})


def read_expense_log() -> list[dict]:
    """Read all expenses from CSV log."""
    if not EXPENSE_LOG.exists():
        return []

    with open(EXPENSE_LOG, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return [
            {**row, "amount": float(row["amount"])}   # cast amount to float
            for row in reader
        ]


def expense_summary_from_log() -> dict[str, float]:
    """Return total per category from CSV log."""
    expenses = read_expense_log()
    summary: dict[str, float] = {}
    for exp in expenses:
        cat = exp["category"]
        summary[cat] = round(summary.get(cat, 0) + exp["amount"], 2)
    return summary


# ── Runner ────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    # Config tests
    print("=== Config Manager ===")
    save_config(DEFAULT_CONFIG)
    config = load_config()
    print(f"Model: {config['model']}")
    print(f"Temperature: {config['temperature']}")

    updated = update_config({"temperature": 0.2, "model": "gpt-4o"})
    print(f"Updated model: {updated['model']}")
    print(f"Updated temperature: {updated['temperature']}")

    # Pretty print full config
    print("\nFull config:")
    print(json.dumps(updated, indent=2))

    # CSV tests
    print("\n=== Expense Log (CSV) ===")
    test_expenses = [
        {"id": 1, "amount": 250.0,  "category": "food",      "description": "Lunch"},
        {"id": 2, "amount": 50.0,   "category": "transport",  "description": "Auto"},
        {"id": 3, "amount": 999.0,  "category": "education",  "description": "Course"},
        {"id": 4, "amount": 150.0,  "category": "food",       "description": "Dinner"},
    ]

    for exp in test_expenses:
        log_expense(exp)

    all_expenses = read_expense_log()
    print(f"Total logged: {len(all_expenses)} expenses")

    summary = expense_summary_from_log()
    print("Summary:")
    for cat, total in sorted(summary.items()):
        print(f"  {cat:<15} ₹{total:.2f}")

    # Cleanup
    for f in [CONFIG_PATH, EXPENSE_LOG]:
        if f.exists():
            f.unlink()      # pathlib delete
    print("\nCleanup done.")






