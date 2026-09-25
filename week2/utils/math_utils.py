"""Math utility functions."""

def safe_divide(a: float, b: float) -> float | None:
    if b == 0:
        return None
    return a / b

def percentage(part: float, total: float)-> float:
    """Return percentage of part over total, rounded to 2 decimal places."""
    if total == 0:
        return 0.0
    return round((part / total) * 100, 2)


def clamp(value: float, min_val: float, max_val: float) -> float:
    """Constrain value between min and max."""
    return max(min_val, min(max_val, value))




