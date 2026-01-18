#3. Write a program which accepts one number and prints square of that number.
#Input: 5
#Output: 25
import math
def CalculateSquare(No):
    return No ** 2
def main():
    Result  = 0 
    Result = CalculateSquare(5)
    print(Result)

if __name__ == "__main__":
    main()
