"""Day 3 Deliverable loop exercises
Covering: for loops, while loops, break, continue, pass"""

# Ex 1 Print numbers from 1 to 10 using a for loop
for i in range (1,11):
    print(i, end=" ") 
print() 

# Exercise 2 — Print even numbers from 1 to 50 using range step
for i in range (2,51,2): #do direcltly range(2,51,2) to get even numbers as 1 is not even
    print(i, end=" ")
print()

# Exercise 3 — Enumerate — print index + name with 1-based index
skills: list[str] = ["Python", "LangChain", "FastAPI", "RAG", "MCP"]
for i , skill in enumerate(skills, start=1): # start=1 to start index from 1 instead of 0, 0 makes no sense when printing a list
    print (f"{i}:{skill}")
print()

## Exercise 4 — zip — pair names with scores
names: list[str]  = ["Priyanshu", "Rahul", "Sneha"]
scores: list[float] = [92.5, 78.0, 55.0]
for name , score in zip(names , scores, strict=False): # strict is False to avoid error if lists are of different lengths
    print(f"{name} - {score}")
print()

# Exercise 5 — while loop — countdown from 10 to 1
count : int = 10
while count > 0:
    print (count, end=" ")
    count-=1
print()

# Exercise 6 — break — find first number divisible by 7 in range 1-100
for i in range (1,101):
    if i %7 ==0:
        print (f"First number divisible by 7 in range 1-100 is: {i}")
        break

# Exercise 7 — continue — print all numbers 1-20, skip multiples of 3
for i in range(1,21):
    if i%3==0:
        continue
    print(i, end=" ")
print()

# Exercise 8 — list comprehension — squares of odd numbers 1-20
odd_Squares: list[int] = [n**2 for n in range(1,21) if n%2 !=0]
print (odd_Squares)

# Exercise 9 — nested loop — multiplication table (3x3)
for i in range (1,4):
    for j in range(1,4):
        print(f"{i}x{j}={i*j}", end=" ")
    print()


# pass — empty block placeholder (code won't break)
numbers = [1, 3, 7, 4, 9, 2]
for n in numbers:
    if n > 5:
        pass                        # TODO: handle large numbers later
    else:
        print(n)

# Nested — flatten 2D list
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [n for row in matrix for n in row]
print(flat)     # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Exercise 10 — while + break — retry simulation (used in AI API calls)
print("=== Ex 10: retry simulation ===")
import random
random.seed(45) # for reproducibility

MAX_RETRIES: int = 5
attempt: int = 0

while attempt < MAX_RETRIES:
    attempt += 1
    success: bool = random.choice([True, False])
    print(f"Attempt {attempt}: {'Success' if success else 'Failed'}")
    if success:
        print("Done.")
        break
else:
    # while...else — runs only if loop completed WITHOUT hitting break
    # Rare Python feature — useful for retry exhaustion
    print(f"All {MAX_RETRIES} attempts failed.")