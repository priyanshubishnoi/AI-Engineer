"""
Day 1 — hello.py
Covering: variables, numeric types, string operations, f-strings
Type hints included from Day 1 — Pydantic and LangChain require them.
"""
from __future__ import annotations
from typing import Union



# Union is used to indicate that a variable can be of multiple types. In this case, 
# it can be either an int or a float. 

def add_num(a:Union[int,float] ,b :Union[int,float]) -> Union[int,float]:
    """Add two numbers together."""
    return a + b

# in 3.10, you can use the built-in type hinting syntax for Union types, which is more concise.
def add_num_310(a:int|float, b:int|float) -> float:
    """Add two numbers together."""
    return a + b    

y: float = 0.1 + 0.2  
print({y}) # This will print {0.30000000000000004} due to floating-point precision issues in Python. 

print (7//2) # floor division, returns 3
print (-7//2) # floor division, returns -4


import re
##data 















