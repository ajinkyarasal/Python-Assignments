#1. Write a program which accepts one number and checks whether it is prime or not.
#Input: 11
#Output: Prime Number

def CheckPrime(No):
    if No < 2:
        return False
    elif No == 2:
        return True
    else:
        count = 0
        for i in range(2,No):
            if No % i == 0:
                count = count + 1
        if count > 0:
            return False
        else: return True

            
def main():
    Result = False
    Result = CheckPrime(72)
    print(Result)

if __name__ == "__main__":
    main()