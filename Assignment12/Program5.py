#Write a program which accepts one number and prints that many numbers in reverse order.
#Input: 5
#Output: 54 32 1

def NumbersTillNReversed(No):
    number = 0
    for i in range(No,0,-1):
        number = number*10 + i
    return number

def main():
    Result = 0
    Result = NumbersTillNReversed(9)
    print(Result)

    
if __name__ == "__main__":
    main()