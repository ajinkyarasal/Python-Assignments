#Write a program which accept N numbers from user and store it into List. 
# Return Maximum number from that List.

def maxInList(list):
    return max(list)
def main():
    No = int(input("Enter the size of list : "))
    NumList = []
    for i in range(No):
        NumList.append(int(input()))
    Max = maxInList(NumList)
    print("Max is : ",Max)


if __name__ == "__main__":
    main()