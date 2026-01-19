#3. Write a program which accepts one number and prints sum of digits.
#Input: 123
#Output: 6

def digitSum(No):
    sum = 0
    while No > 0:
        if No % 10 >= 0:
            sum += No%10
        No = No // 10
    return sum


def main():
    Result = 0 
    Result = digitSum(123)
    print(Result)


if __name__ == "__main__":
    main()