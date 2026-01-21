#Write a program which contains one function that accept one number from user and returns true if number is divisible by 5 otherwise return false.
#Input : 8
#Output : False
#Input : 25
#Output : True

def isDivisibleBy5(No):
    if No%5 == 0:
        return True
    else:
        return False
    
def main():
    print(isDivisibleBy5(8))
    print(isDivisibleBy5(25))

if __name__ == "__main__":
    main()