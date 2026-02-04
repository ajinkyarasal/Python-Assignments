#Frequency of a String in File
# Problem Statement:
# Write a program which accepts a file name and one string from the user and returns 
# the frequency (count of occurrences) of that string in the file.
# Input:
# Demo.txt Marvellous
# Expected Output:
# Count how many times "Marvellous" appears in Demo.txt.
import sys
import os
def WordCountInFile(FileName,SearchString):
    if os.path.exists(FileName):
        fobj = open(FileName,"r")
        Data = fobj.read()
        count = 0
        if len(Data) > 0:
            for word in Data.split():
                if word == SearchString:
                    count += 1
            return count
        else:
            return -1

def main():
    if len(sys.argv) == 3:
        File = sys.argv[1]
        Str = sys.argv[2] 

        WordCount = WordCountInFile(File,Str)
        if WordCount > 0:
            print(f"The frequency of {Str} in {File} is : ",WordCount)
        else:
            print("There is no such word or the file is empty.")

if __name__ == "__main__":
    main()