#Display File Contents
# Problem Statement:
# 
# Write a program which accepts a file name from the user,
#  opens that file, and displays the entire contents on the console.
# Input:
# Demo.txt
# Expected Output:
# Display contents of Demo. txt on console.

import os
def DisplayFileContents(FileName):
    if os.path.exists(FileName):
        fobj = open(FileName,"r")
        Data = fobj.read()
        fobj.close()
        print(Data)
    else:
        print("The file does not exists.")

def main():
    FileName = input("Enter the File name : ")
    DisplayFileContents(FileName)

if __name__ == "__main__":
    main()
