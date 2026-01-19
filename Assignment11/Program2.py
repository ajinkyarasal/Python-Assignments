#2. Write a program which accepts one number and prints count of digits in that number.
#Input: 7521
#Output: 4
def CountOfDigits(No):
    count = 0
    while No > 0:
        if No % 10 >=0:
            count = count + 1
        No = No // 10
    return count
    

def main():
    Result = 0
    Result = CountOfDigits(7521)
    print(Result)

if __name__ == "__main__":
    main()