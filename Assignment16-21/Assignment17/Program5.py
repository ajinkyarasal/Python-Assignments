#Write a program which accept one number for user and check whether number is prime or not.
#Input :5
#Output : It is Prime Number
def isPrime(No):
    Result = False
    count = 0
    if No < 2:
        return False
    elif No == 2:
        return True
    else:
        for i in range (2,No):
            if No % i == 0:
                count += 1
        
        if count > 0:
            return False
        else:
            return True
            
    
def main():
    No = int(input("Enter a number : "))
    Result = isPrime(No)
    if Result:
        print("It is Prime Number")
    else:
        print("It is not a Prime Number")
if __name__ == "__main__":
    main()