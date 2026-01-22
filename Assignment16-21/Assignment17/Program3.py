#Write a program which accept one number from user and return its factorial.
#Input : 5
#Output : 120

def FactorialOfNum(No):
    factorial = 1
    for i in range(1,No+1):
        factorial *= i
    return factorial

def main():
    No = int(input("Enter a number : "))
    Result = FactorialOfNum(No)
    print(Result)

if __name__ == "__main__":
    main()