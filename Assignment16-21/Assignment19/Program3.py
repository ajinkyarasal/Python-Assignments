#3. Write a program which contains filter), map() and reduce() in it. Python application which contains
#  one list of numbers. List contains the numbers which are accepted from user. Filter should filter
#  out all such numbers which greater than or equal to 70 and less than or equal to
#90. Map function will increase each number by 10. Reduce will return product of all that numbers.
#Input List = [4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70]
#List after filter = [76, 89, 86, 90, 70]
#List after map = [86, 99, 96, 100, 80]
#Output of reduce = 6538752000
from functools import reduce
def main():
    ListSize = int(input("Enter the list size : "))
    Data = []
    for i in range(ListSize):
        Data.append(int(input()))
    print(Data)

    fData = list(filter(lambda a : a >= 70 and a<=90, Data))
    mData = list(map(lambda a : a+10,fData))
    rData = reduce(lambda a,b : a*b,mData)
    print(rData)

if __name__ == "__main__":
    main()
