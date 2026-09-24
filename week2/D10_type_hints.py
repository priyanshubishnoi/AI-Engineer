"""
Day 10 Deliverable: Week 1 functions retyped with full annotations
Covers: primitives, containers, TypedDict, dataclass, Callable, | union syntax
"""
from typing import Any, Callable, TypedDict
from dataclasses import dataclass, field


# ── TypedDict — replaces loose dicts from earlier days ───────────────────

class Expense(TypedDict):
    id:          int
    amount:      float
    category:    str
    description: str


class Config(TypedDict):
    model:        str
    temperature:  float
    max_tokens:   int
    system_prompt: str
    tags:         list[str]


class StatsResult(TypedDict):
    min:     float
    max:     float
    sum:     float
    average: float
    count:   int


# ── Dataclass — Student from Day 5/6, now properly typed ─────────────────

@dataclass
class Student:
    name:   str
    scores: list[float]
    city:   str
    grade:  str = ""
    tags:   list[str] = field(default_factory=list)

    @property
    def average(self) -> float:
        return round(sum(self.scores) / len(self.scores), 2)

    def is_passing(self) -> bool:
        return self.average >= 60

    def __str__(self) -> str:
        return f"{self.name} | Avg: {self.average} | {'PASS' if self.is_passing() else 'FAIL'}"


# ── Retyped utility functions from Week 1 ────────────────────────────────

def safe_divide(a: float, b: float) -> float | None:
    if b == 0:
        return None
    return a / b


def stats(*args: float) -> StatsResult:
    if not args:
        return {"min": 0, "max": 0, "sum": 0, "average": 0, "count": 0}
    return {
        "min":     min(args),
        "max":     max(args),
        "sum":     sum(args),
        "average": round(sum(args) / len(args), 2),
        "count":   len(args),
    }


def filter_expenses(
    expenses: list[Expense],
    predicate: Callable[[Expense], bool]
) -> list[Expense]:
    """Generic filter — accepts any function that takes Expense and returns bool."""
    return [e for e in expenses if predicate(e)]


def word_count(text: str) -> dict[str, int]:
    words = text.lower().split()
    counts: dict[str, int] = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    return counts


def format_name(
    first: str,
    last: str,
    title: str | None = None,
    suffix: str | None = None
) -> str:
    """Explicit keyword args replace **kwargs — fully typed."""
    name = f"{first} {last}"
    if title:
        name = f"{title} {name}"
    if suffix:
        name = f"{name}, {suffix}"
    return name


# ── Runner ────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    # TypedDict
    print("=== TypedDict ===")
    expenses: list[Expense] = [
        {"id": 1, "amount": 250.0, "category": "food",      "description": "Lunch"},
        {"id": 2, "amount": 50.0,  "category": "transport", "description": "Auto"},
        {"id": 3, "amount": 999.0, "category": "education", "description": "Course"},
    ]

    food_only = filter_expenses(expenses, lambda e: e["category"] == "food")
    print(f"Food expenses: {food_only}")

    expensive = filter_expenses(expenses, lambda e: e["amount"] > 100)
    print(f"Over ₹100: {[e['description'] for e in expensive]}")

    # Dataclass
    print("\n=== Dataclass ===")
    students: list[Student] = [
        Student("Priyanshu", [92, 88, 95], "Jaipur"),
        Student("Rahul",     [78, 82, 75], "Delhi"),
        Student("Sneha",     [55, 60, 58], "Mumbai"),
    ]

    for s in students:
        print(s)

    passing = [s for s in students if s.is_passing()]
    print(f"\nPassing: {[s.name for s in passing]}")

    # Stats
    print("\n=== Stats ===")
    all_scores = [s.average for s in students]
    result: StatsResult = stats(*all_scores)
    for key, val in result.items():
        print(f"  {key}: {val}")

    # Format name
    print("\n=== Name Formatter ===")
    print(format_name("Priyanshu", "Bishnoi"))
    print(format_name("Priyanshu", "Bishnoi", title="Mr."))
    print(format_name("Priyanshu", "Bishnoi", title="Dr.", suffix="PhD"))