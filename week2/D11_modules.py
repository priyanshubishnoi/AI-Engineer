"""
Day 11 Deliverable: Multi-file project with modules and .env
Covers: import system, package structure, pip, python-dotenv
"""
import os
from dotenv import load_dotenv
from utils import safe_divide, percentage, clamp, slugify, truncate
from utils.string_utils import word_count
from utils.math_utils import clamp as clamp_value  # alias import


# ── Load environment ──────────────────────────────────────────────────────

load_dotenv()

APP_NAME = os.getenv("APP_NAME", "Unknown App")
DEBUG    = os.getenv("DEBUG", "false").lower() == "true"
API_KEY  = os.getenv("OPENWEATHER_API_KEY")

print(f"App: {APP_NAME}")
print(f"Debug mode: {DEBUG}")
print(f"API key loaded: {'Yes' if API_KEY else 'NO — check .env'}")


# ── Use imported utilities ────────────────────────────────────────────────

if __name__ == "__main__":
    # Math utils
    print("\n=== Math Utils ===")
    print(safe_divide(10, 3))           # 3.333...
    print(safe_divide(10, 0))           # None
    print(percentage(45, 200))          # 22.5
    print(clamp(150, 0, 100))           # 100 — clamped to max
    print(clamp_value(-5, 0, 100))      # 0 — clamped to min

    # String utils
    print("\n=== String Utils ===")
    print(slugify("AI Engineer Roadmap 2026"))      # ai-engineer-roadmap-2026
    print(truncate("This is a very long description that should be cut short", 30))
    
    article = "the quick brown fox jumps over the lazy dog the fox"
    counts = word_count(article)
    # Sort by frequency
    for word, count in sorted(counts.items(), key=lambda x: x[1], reverse=True):
        print(f"  {word:<10} {count}")

    # Show module location
    print("\n=== Module Info ===")
    import utils
    print(f"utils package: {utils.__file__}")
    print(f"exported names: {utils.__all__}")