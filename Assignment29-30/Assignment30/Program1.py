#Count Lines in a File
# Problem Statement:
# Write a program which accepts a file name from the user and counts how many lines 
# are present in the file.
# Input: Demo. txt
# Expected Output:
# Total number of lines in Demo. txt.
import os
def LineCountInFile(FileName):
    if os.path.exists(FileName):
        fobj = open(FileName,"r")
        Data = fobj.readlines()
        fobj.close()
        print(Data)
        return len(Data)
    
    else:
        print("The file does not exists")
        return -1


def main():
    FileName = input("Enter the file name : ")
    Count = 0
    Count = LineCountInFile(FileName)
    print(f"Total number of lines in {FileName} : {Count}")

if __name__ == "__main__":
    main()