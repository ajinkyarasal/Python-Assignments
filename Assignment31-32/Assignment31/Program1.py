#Design automation script which accept directory name and file extension from user. 
# Display all files with that extension.
# Usage : DirectoryFileSearch.py "Demo" "
# •txt"
# Demo is name of directory and .txt is the extension that we want to search.
import sys
import os
import time
def FileSearch(DirectoryName,FileExtension):
    Border = "*" * 45
    timestamp = time.ctime()
    logfile = "FileSearchScript_%s.log" %(timestamp)
    logfile = logfile.replace(" ","_").replace(":","_")
    logfileobj = open(logfile,"w")
    logfileobj.write(Border+"\n")
    logfileobj.write("*********** File Search Script ***********"+"\n")
    Ret = False
    Ret = os.path.exists(DirectoryName)
    if Ret == False:
        print("Given Directory name does not exist.")
        return
    
    Ret = os.path.isdir(DirectoryName)
    if Ret == False:
        print("The given name is not a Directory.")
        return
    
    for folders,subfolders,files in os.walk(DirectoryName):
        for file in files:
            if file.endswith(FileExtension):
                logfileobj.write(file+"\n")
    
    logfileobj.write(Border+"\n")
    logfileobj.write("***** Thank you for using the script *****")
    logfileobj.close()

def main():
    if len(sys.argv) == 3:
        DirectoryName = sys.argv[1]
        FileExtension = sys.argv[2]

        FileSearch(DirectoryName,FileExtension)
    else:
        print("Invalid number of arguments.")

if __name__ == "__main__":
    main()