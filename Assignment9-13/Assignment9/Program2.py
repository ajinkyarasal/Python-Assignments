#2. Write a program which contains one function ChkGreater () that accepts two numbers and prints the greater number.
#Input: 10 20
#Output: 20 is greater

def ChkGreater(No1,No2):
    if No1 == No2:
        return 0
    elif No1 > No2:
        return No1
    else:
        return No2

def main():
    Result  = 0
    Result = ChkGreater(10, 20)
    if(Result == 0):
        print("Both the numbers are same")
    else:
        print(Result , " is greater")
    
if __name__ == "__main__":
    main()