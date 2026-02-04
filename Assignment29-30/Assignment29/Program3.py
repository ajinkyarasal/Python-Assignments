#Copy File Contents into a New File (Command Line)
# Problem Statement:
# Write a program which accepts an existing file name through command line arguments,
#  creates a new file named Demo. txt, and copies all contents from the given file into Demo. txt.
# Input (Command Line):
# ABC. txt
# Expected Output:
# Create Demo. txt and copy contents of ABC. txt into Demo. txt.

import sys
import os
def CopyFileContent(SourceFile):
    if os.path.exists(SourceFile):
        Sobj = open(SourceFile,"r")
        Data = Sobj.read()

        Tobj = open("Demo.txt", "w")
        Tobj.write(Data)

        Sobj.close()
        Tobj.close()

        print("Data copied successfully.")

def main():
    if len(sys.argv) == 2:
        Source = sys.argv[1]
        CopyFileContent(SourceFile=Source)
    
    else:
        print("Invalid number of arguments.")

if __name__ == "__main__":
    main()