#Write a program which contains filter(), map() and reduce) in it. 
# Python application which contains one list of numbers. 
# List contains the numbers which are accepted from user. 
# Filter should filter out all prime numbers.
#  Map function will multiply each number by 2. 
# Reduce will return Maximum number from that numbers. 
# (You can also use normal functions instead of lambda functions).
#Input List = [2, 70 , 11, 10, 17, 23, 31, 77]
#List after filter = [2, 11, 17, 23, 31]
#List after map = [4, 22, 34, 46, 62]
#Output of reduce = 62
from functools import reduce
def ChekPrime(No):
    if No < 2:
        return False
    elif No == 2:
        return True
    else:
        count = 0
        for i in range(2,No):
            if No % i == 0:
                count += 1
        if count > 0:
            return False
        else:
            return True 
        
def main():
    Data = []
    ListSize = int(input("Enter the size of list : "))
    for _ in range(ListSize):
        Data.append(int(input()))
    print(Data)

    FilteredData = list(filter(ChekPrime,Data))
    print("List after filter : ",FilteredData)
    MapData = list(map(lambda a : a * 2,FilteredData))
    print("List after map : ",MapData)
    reduceData = reduce(lambda a,b:max(a,b),MapData)
    print("Output of reduce : ",reduceData)

if __name__ == "__main__":
    main()