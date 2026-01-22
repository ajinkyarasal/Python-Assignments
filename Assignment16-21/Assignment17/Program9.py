# Write a program which accept number from user and return number of digits in that number.
#Input : 5187934
#Output : 7

def NumberOfDigits(No):
    count = 0
    while No > 0:
        if No%10 >= 0:
            count += 1
        No = No//10
    return count
    
def main():
    No = int(input("Enter a number : "))
    Result = NumberOfDigits(No)
    print(Result)
if __name__ == "__main__":
    main()