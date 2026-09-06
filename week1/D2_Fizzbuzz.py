
def fizzbuzz(n:int) -> list[str]:
    """fizz when div 3, buzz when div 5, fizzbuzz when div 15"""
    ans =[]
    for i in range(1, n+1):
        if i %15 ==0:
            ans.append("FizzBuzz")
        elif i %5 == 0:
            ans.append("Buzz")
        elif i % 3 == 0:
            ans.append("Fizz")
        else:
            ans.append(str(i))
    return ans


if __name__ == "__main__":
    print(fizzbuzz(100))
