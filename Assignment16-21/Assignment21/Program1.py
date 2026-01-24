#1: Design a Python application that creates two threads named Prime and NonPrime.
#Both threads should accept a list of integers.
#The Prime thread should display all prime numbers from the list.
#The NonPrime thread should display all non-prime numbers from the list.

import threading

def isPrime(No):
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
        
def displayPrimeFromList(numList):
    print("Inside displayPrimeFromList.")
    primeList = list(filter(isPrime,numList))
    print("Printing Prime number list : ",primeList)

def displayNonPrimeFromList(numList):
    print("Inside displayNonPrimeFromList.")
    NonPrimeList = list(filter(lambda x : not isPrime(x),numList))
    print("Printing Non prime number list : ",NonPrimeList)

def main():
    print("Inside main")
    Data = [1,3,5,7,2,31,22,37,88,45,47]

    t1 = threading.Thread(target=displayPrimeFromList,name="Prime",args=(Data,))
    t2 = threading.Thread(target=displayNonPrimeFromList,name="NonPrime",args=(Data,))

    t1.start()
    t1.join()

    t2.start()
    t2.join()

    print("End of main")

if __name__ == "__main__":
    main()