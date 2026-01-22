#Write a program which accept one number form user and return addition of its factors.
#Input : 12
#Output : 16
#(1+2+3+4+6)

def AdditionOfFactors(No):
    sum = 0
    for i in range(1,No+1):
        if No % i == 0:
            sum += i
    return sum


def main():
    No = int(input("Enter a number : "))
    Result = AdditionOfFactors(12)
    print(Result)
if __name__ == "__main__":
    main()