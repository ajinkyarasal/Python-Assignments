#Copy File Contents into Another File
# Problem Statement:
# Write a program which accepts two file names from the user.
#   First file is an existing file
#   Second file is a new file
# Copy all contents from the first file into the second file.
# Input:
# ABC.txt Demo.txt
# Expected Output:
# Contents of ABC. txt copied into Demo. txt.

def CopyContentFromSourceToTarget(Source,Target):
    try:
        sObj = open(Source,"r")
        SourceData = sObj.readlines()
        tObj = open(Target,"w")
        tObj.writelines(SourceData)
        sObj.close()
        tObj.close()
        print(f"Content of {Source} copied into {Target}")
        
    except FileNotFoundError:
        print("Source file Does not exists.")

def main():
    File1 = input("Enter source file name : ")
    File2 = input("Enter target file name : ")

    CopyContentFromSourceToTarget(Source=File1,Target=File2)

if __name__ == "__main__":
    main()
