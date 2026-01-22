#Write a program which accept number from user and return addition of digits in that number.
#Input : 5187934
#Output : 37

def DigitSum(No):
    sum = 0
    while No > 0:
        if No%10 >= 0:
            sum += (No%10)
        No = No // 10
    return sum
def main():
    No = int(input("Enter a number : "))
    Result = DigitSum(No)
    print(Result)
if __name__ == "__main__":
    main()