#2. Write a program which accepts one number and prints that many numbers starting from 1.
#Input: 5
#Output: 123 4 5

def NumbersTillN(No):
    number = 0
    for i in range(1, No+1):
        number = number *10 + i
    return number


def main():
    Result = 0
    Result = NumbersTillN(5)
    print(Result)
    
if __name__ == "__main__":
    main()