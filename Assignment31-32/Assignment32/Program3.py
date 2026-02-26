# Design automation script which accept directory name and
#  delete all duplicate files from that directory. Write names of 
# duplicate files from that directory into log file named as Log.txt.
#Log.txt file should be created into current directory.
#Usage: DirectoryDusplicateRemoval.py "Demo"
#Demo is name of directory.

import sys
import os
from calculate_checksum import calculate_checksum
import time

def find_duplicate_file(directory_name):
    ret = False
    ret = os.path.exists(directory_name)
    if ret == False:
        print("Given directory name does not exists")
        return
    
    ret = os.path.isdir(directory_name)
    if ret == False:
        print("Given name is not a directory.")
        return
    
    border = ("*" * 45)
    timestamp = time.ctime()
    log_file_name = "Log%s.log" %(timestamp)
    log_file_name = log_file_name.replace(" ","_").replace(":","_")
    log_file_obj = open(log_file_name,"w")
    log_file_obj.write(border+"\n")
    log_file_obj.write("******** Duplicate File Tracker Script ************"+"\n")

    duplicate_files = {}
    for folder,subfolders,files in os.walk(directory_name):
        for f in files:
            checksum = calculate_checksum(os.path.join(folder,f))
            if checksum in duplicate_files:
                duplicate_files[checksum].append(f)
            else:
                duplicate_files[checksum] = [f]

    only_duplicates = list(filter(lambda x : len(x) > 1,duplicate_files.values()))
    for values in only_duplicates:
        log_file_obj.write(f"Duplicate files : {values}"+"\n")

    log_file_obj.write("*********** End of Report ***********")
    log_file_obj.close()

def main():

    if len(sys.argv) == 2:
        directory_name = sys.argv[1]
        find_duplicate_file(directory_name)

    else:
        print("Invalid number of arguments.")


if __name__ == "__main__":
    main()