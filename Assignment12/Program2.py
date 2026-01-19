#Write a program which accepts one number and prints its factors.
#Input: 12
#Output: 123 4 6 12


def FactorsOfANumber(No):
    factorsList = []
    for i in range(1,No+1):
        if No % i == 0:
            factorsList.append(i)
    return factorsList


def main():
    Result = []
    Result = FactorsOfANumber(15)
    print(Result)
    
    
if __name__ == "__main__":
    main()