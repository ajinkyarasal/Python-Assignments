#4. Write a program which accepts one number and prints reverse of that number.
#Input: 123
#Output: 321

def reverse(No):
    reversedNum = 0
    digit = 0
    while No > 0:
        if No % 10 >= 0:
            digit = No % 10
            reversedNum = (reversedNum * 10) + digit
        No = No // 10
    return reversedNum

def main():
    Result = 0
    No = 12345
    Result = reverse(No)
    print(Result)
    
if __name__ == "__main__":
    main()
