#2. Write a program which accepts one number and prints sum of first N natural numbers.
#Input: 5
#Output: 15
def SumOfNaturalNumber(No):
    sum = 0
    for i in range(1,No+1):
        sum += i
    return sum

def main():
    No = 5
    Result = 0
    Result = SumOfNaturalNumber(No)
    print(f"sum of first {No} natural number is : ",Result)


if __name__ == "__main__":
    main()
