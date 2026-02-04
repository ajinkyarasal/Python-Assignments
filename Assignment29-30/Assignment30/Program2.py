#Count Words in a File
# Problem Statement:
# Write a program which accepts a file name from the user and counts the
#  total number of words in that file.
# Input:
# Demo.txt
# Expected Output:
# Total number of words in Demo. txt.
import os
def FileWordCount(FileName):
    try:
        fobj = open(FileName,"r")
        Data = fobj.read()
        return len(Data.split())
    except FileNotFoundError:
        return -1

def main():
    FileName = input("Enter the file name : ")
    Count = 0
    Count = FileWordCount(FileName)
    print(f"Total number of words in {FileName} : {Count}")

if __name__ == "__main__":
    main()