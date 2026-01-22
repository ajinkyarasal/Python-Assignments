#Write a program which accept N numbers from user and store it into List. 
# Return Minimum number from that List.

def minInList(list):
    return min(list)
def main():
    No = int(input("Enter the size of list : "))
    NumList = []
    for i in range(No):
        NumList.append(int(input()))
    Min = minInList(NumList)
    print("Mix is : ",Min)


if __name__ == "__main__":
    main()