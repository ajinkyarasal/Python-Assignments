#Write a program which accept N numbers from user and store it into List.
#  Return addition of all prime numbers from that List. Main python file accepts N numbers 
# from user and pass each number to ChkPrime() function which is part of our user defined 
# module named as MarvellousNum. Name of the function from main python file should be ListPrime().

from MarvellousNum import ChekPrime
def ListPrime():
    Data = []
    primeSum = 0
    ListSize = int(input("Enter the size of list : "))
    for _ in range(0,ListSize):
        Data.append(int(input()))

    for num in Data:
        if ChekPrime(num):
            primeSum += num
    print("The sum of prime is. : ",primeSum)
    
if __name__ == "__main__":
    ListPrime()