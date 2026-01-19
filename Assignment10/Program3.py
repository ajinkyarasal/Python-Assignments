#3. Write a program which accepts one number and prints factorial of that number.
#Input: 5
#Output: 120


def factorial(No):
    factorial = 1
    for i in range(1 , No+1):
        factorial *= i
    return factorial

def main():
    No = 5
    Result = 0 
    Result = factorial(No)
    print(f"factorial of {No} is : ",Result)


if __name__ == "__main__":
    main()