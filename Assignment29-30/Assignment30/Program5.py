#Search a Word in File
# Problem Statement:
# Write a program which accepts a file name and a word from the user and 
# checks whether that word is present in the file or not.
# Input:
# Demo.txt Marvellous
# Expected Output:
# Display whether the word Marvellous is found in Demo. txt or not.

def SearchStringInFile(Source,TargetWord):
    try:
        sObj = open(Source,"r")
        SourceData = sObj.read()
        Data = SourceData.split()
        sObj.close()
        for word in Data:
            if word == TargetWord:
                print(f"{TargetWord} word found in file {Source}")
                return
        print("Word not found.")
            
        
    except FileNotFoundError:
        print("Source file Does not exists.")

def main():
    File1 = input("Enter source file name : ")
    SearchString = input("Enter text to find in file : ")

    SearchStringInFile(Source=File1,TargetWord=SearchString)

if __name__ == "__main__":
    main()
