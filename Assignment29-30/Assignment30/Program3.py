#Display File Line by Line
# Problem Statement:
# .
# Write a program which accepts a file name from the user and displays 
# the contents of the file line by line on the screen
# Input:
# Demo.txt
# Expected Output:
# Display each line of Demo. txt one by one.

def DisplayFileContent(FileName):
    try:
        fobj = open(FileName,"r")
        Data = fobj.readlines()
        for line in Data:
            print(line.replace("\n",""))
        fobj.close()
    except FileNotFoundError:
        print("File Does not exists.")

def main():
    FileName = input("Enter the file name : ")
    DisplayFileContent(FileName)

if __name__ == "__main__":
    main()