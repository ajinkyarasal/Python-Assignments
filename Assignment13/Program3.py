#3. Write a program which accepts one number and checks whether it is perfect number or not.
#Input: 6
#Output: Perfect Number

#Positive integer that equals the sum of its own proper divisor(all its divisors excluding the number itself)

def isPerfectNumber(No):
    if No<=0:
        return False
    else:
        divisor = 0
        for i in range(1,No):
            if No % i == 0:
                divisor += i
        if No == divisor:
            return True
        else:
            return False

def main():
    Result = 0
    Result = isPerfectNumber(8128)
    print(Result)
    
 
if __name__ == "__main__":
    main()