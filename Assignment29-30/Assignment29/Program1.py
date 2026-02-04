#Write a program which accepts a file name from the user and checks whether that 
# file exists in the current directory or not.
# Input:Demo.txt
# Expected Output:
# Display whether Demo. txt exists or not.
import os

def CheckIfFileExists(FileName):
    if len(FileName) == 0:
        print("FileName cannot be empty")
        return False
    
    if os.path.exists(FileName):
        return True
    else:
        return False


def main():
    FileName = input("Enter the file name : ")
    Ret  = False
    Ret = CheckIfFileExists(FileName)
    if Ret:
        print("File exists")
    else:
        print("File Does not exist.")

if __name__ == "__main__":
    main()