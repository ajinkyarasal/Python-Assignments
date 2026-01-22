#Write a program which accept N numbers from user and store it into List. Return addition of all elements from that List.
#Input : Number of elements : 6
#Input elements : 13 5 45 7 4 56
# output : 130

def addListElements(NumList):
    sum = 0
    for num in NumList:
        sum += num
    return sum

def main():
    No = int(input("Enter the size of list : "))
    NumList = []
    for i in range(No):
        NumList.append(int(input()))
    print(NumList)
    Result = addListElements(NumList)
    print(Result)
if __name__ == "__main__":
    main()
