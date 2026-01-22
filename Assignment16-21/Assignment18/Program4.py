#Write a program which accept N numbers from user and store it into List. 
# Accept one another number from user and return frequency of that number from List.

def NumFrequencyCounter(data,target):
    count = 0
    for num in data:
        if num == target:
            count += 1
    return count

def main():
    frequency = 0
    target = 0
    Data = []
    No = int(input("Enter the size of list : "))

    for _ in range(No):
        Data.append(int(input()))
    print(f"{No} numbers entered successfully.")
    target = int(input("Enter the number to be found in list: "))
    frequency = NumFrequencyCounter(Data,target)
    print(frequency)
if __name__ == "__main__":
    main()