"""
Day 4 Deliverable: Utility Functions Library
Covers: def, return, defaults, *args, **kwargs, scope, lambda
"""

#Math

def add (a:float, b:float) -> float:
    return a+b 

def sub (a:float, b:float) -> float:
    return a-b 

def multiply (a:float, b:float) -> float:
    return a*b 

def divide (a:float, b:float) -> float| None:
    if b==0:
        return None
    return a/b 

def power(a:float, exp:float=2) -> float:
    return a**exp

def stats(*args:float) -> dict[str, float]:
    if not args:
        return{}
    return{
        "min":     min(args),
        "max":     max(args),
        "sum":     sum(args),
        "average": sum(args) / len(args),
    }

#String

def reverse_string(s:str)->str:
    return s[::-1]

def is_palindrome(s:str)->bool:
    clean_txt = s.replace(" ","").lower()
    return clean_txt == clean_txt[::-1]

def word_count (txt:str)->dict[str,int]:
    words = txt.lower().split()
    counts : dict[str, int] = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    return counts

def format_name(first: str, last: str, **kwargs: str) -> str:
    """Format a name with optional title and suffix."""
    title  = kwargs.get("title", "")
    suffix = kwargs.get("suffix", "")
    name   = f"{first} {last}"
    if title:
        name = f"{title} {name}"
    if suffix:
        name = f"{name}, {suffix}"
    return name

if __name__ == "__main__":
    # Math
    print("=== Math ===")
    print(add(10, 5))
    print(divide(10, 0))
    print(power(3))             # 9  — default exp=2
    print(power(2, 10))         # 1024
    print(stats(10, 20, 30, 40, 50))

    # Strings
    print("\n=== Strings ===")
    print(reverse_string("Priyanshu"))
    print(is_palindrome("racecar"))
    print(is_palindrome("hello"))
    print(word_count("the quick brown fox jumps over the lazy dog"))

    # kwargs
    print("\n=== Name Formatter ===")
    print(format_name("Priyanshu", "Bishnoi"))
    print(format_name("Priyanshu", "Bishnoi", title="Mr."))
    print(format_name("Priyanshu", "Bishnoi", title="Dr.", suffix="PhD"))

    # Lambda
    print("\n=== Lambda ===")
    score:list[tuple[str, int]] = [("Jitesh",85),("Priyanshu",75),("Rahul",67)]
    score.sort(key = lambda s:s[1], reverse=True)
    for rank, (name,marks) in enumerate(score, start= 1):
        print(f"{rank}. {name}:{marks}")
    








