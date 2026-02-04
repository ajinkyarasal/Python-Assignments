#Compare Two Files (Command Line)
# Problem Statement:
# Write a program which accepts two file names through command line arguments 
# and compares the contents of both files.
# 	If both files contain the same contents, display Success
# 	Otherwise display FailureInput (Command Line):
# Input: Demo.txt Hello.txt
# Expected Output: Success OR Failure

import sys
import os

def CompareFileContents(File1,File2):
    if os.path.exists(File1) and os.path.exists(File2):
        f1obj = open(File1,"r")
        f1Data = f1obj.read()

        f2obj = open(File2,"r")
        f2Data = f2obj.read()

        if f1Data == f2Data:
            print("Success")
        else:
            print("Failure")
    else:
        print("File/s does not exists.")
def main():
    if len(sys.argv) == 3:
        File1 = sys.argv[1]
        File2 = sys.argv[2] 

        CompareFileContents(File1,File2)

if __name__ == "__main__":
    main()