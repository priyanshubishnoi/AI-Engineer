"""String utility functions."""


def slugify(text: str) -> str:
    """Convert text to URL-friendly slug."""
    return text.lower().strip().replace(" ", "-")


def truncate(text: str, max_length: int = 100, suffix: str = "...") -> str:
    """Truncate text to max_length, appending suffix if truncated."""
    if len(text) <= max_length:
        return text
    return text[:max_length - len(suffix)] + suffix


def word_count(text: str) -> dict[str, int]:
    words = text.lower().split()
    return {word: words.count(word) for word in set(words)}