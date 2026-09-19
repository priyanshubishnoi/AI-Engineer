"""
Day 8 Deliverable: Safe division + file reader with full error handling
Covers: try/except/else/finally, specific exceptions, raise, chaining
"""
import json
import os


# ── Custom Exceptions ─────────────────────────────────────────────────────

class AppError(Exception):
    """Base exception for this project."""
    pass

class ValidationError(AppError):
    """Invalid input data."""
    pass

class FileProcessingError(AppError):
    """File read/parse failure."""
    pass


# ── Safe Division ─────────────────────────────────────────────────────────

def safe_divide(a: float, b: float) -> float:
    """Divide a by b with full error handling."""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError(f"Expected numbers, got {type(a).__name__} and {type(b).__name__}")
    if b == 0:
        raise ValidationError("Denominator cannot be zero.")
    return a / b


def run_division_tests() -> None:
    test_cases: list[tuple] = [
        (10, 2),        # valid
        (10, 0),        # ZeroDivisionError
        ("10", 2),      # TypeError
        (9.5, 3),       # valid float
    ]

    print("=== Division Tests ===")
    for a, b in test_cases:
        try:
            result = safe_divide(a, b)
        except ValidationError as e:
            print(f"  Validation: {e}")
        except TypeError as e:
            print(f"  Type error: {e}")
        else:
            print(f"  {a} / {b} = {result:.4f}")
        finally:
            pass    # cleanup would go here — close DB connection etc.


# ── Safe File Reader ──────────────────────────────────────────────────────

def read_json_file(filepath: str) -> dict:
    """Read and parse a JSON file with full error handling."""
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"File not found: {filepath!r}")

    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
    except PermissionError as e:
        raise FileProcessingError(f"Cannot read file: {filepath}") from e

    try:
        return json.loads(content)
    except json.JSONDecodeError as e:
        raise FileProcessingError(
            f"Invalid JSON in {filepath!r} at line {e.lineno}"
        ) from e


def write_json_file(filepath: str, data: dict) -> None:
    """Write dict to JSON file safely."""
    try:
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
        print(f"Written: {filepath}")
    except OSError as e:
        raise FileProcessingError(f"Could not write {filepath}") from e


def run_file_tests() -> None:
    print("\n=== File Tests ===")

    # Write a valid JSON file
    test_data = {"name": "Priyanshu", "score": 92.5, "grade": "A"}
    write_json_file("test_config.json", test_data)

    # Read it back — should succeed
    try:
        data = read_json_file("test_config.json")
    except FileProcessingError as e:
        print(f"  Error: {e}")
    else:
        print(f"  Read success: {data}")

    # Read missing file — should fail gracefully
    try:
        read_json_file("missing.json")
    except FileNotFoundError as e:
        print(f"  Expected: {e}")

    # Write bad JSON manually and try to read it
    with open("bad.json", "w") as f:
        f.write("{ not valid json }")
    try:
        read_json_file("bad.json")
    except FileProcessingError as e:
        print(f"  Expected: {e}")
        print(f"  Caused by: {e.__cause__}")

    # Cleanup
    for f in ["test_config.json", "bad.json"]:
        if os.path.exists(f):
            os.remove(f)


# ── Runner ────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    run_division_tests()
    run_file_tests()