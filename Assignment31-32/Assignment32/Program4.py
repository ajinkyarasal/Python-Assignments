#Design automation script which accept directory name and delete all duplicate files 
# from that directory. Write names of duplicate files from that directory into log file 
# named as Log.txt.
#Log.txt file should be created into current directory. Display execution time required 
# for the script.
#Usage : DirectoryDusplicateRemoval.py "Demo"
#Demo is name of directory.

import sys
import os
import time
from calculate_checksum import calculate_checksum

def find_duplicates(directory_name):
    ret = os.path.exists(directory_name)
    if ret == False:
        print("The given path does not exists.")
        return
    ret = os.path.isdir(directory_name)
    if ret == False:
        print("The given path is not a directory.")
        return
    
    start_time = time.time()
    border = "-"*35
    timestamp = time.ctime()
    log_file_name = "Log%s.txt" %(timestamp)
    log_file_name = log_file_name.replace(" ","_").replace(":","_")
    log_file = open(log_file_name,"w")
    log_file.write(border)
    log_file.write("-------------------- Script to  Delete Duplicate files in Directory --------------------\n")

    file_check_sum_dictionary = {}
    for folder,subfolder,files in os.walk(directory_name):
        for f in files:
            file_path = os.path.join(folder,f)
            file_check_sum = calculate_checksum(file_path)
            if file_check_sum in file_check_sum_dictionary:
                file_check_sum_dictionary[file_check_sum].append(file_path)
            else:
                file_check_sum_dictionary[file_check_sum] = [file_path]

    duplicate_files = list(filter(lambda f : len(f) > 1,file_check_sum_dictionary.values()))
    log_file.write("Below are the duplicates found in the file\n")
    log_file.write(border+"\n")
    for f in duplicate_files:
        log_file.write(str(f)+"\n")

    log_file.write(border+"\n")
    log_file.write("--------- Below duplicate files were identified and removed ---------\n")
    removed_files = []
    for entry in duplicate_files:
        count = 0
        for file in entry:
            if count > 0:
                removed_files.append(file)
                os.remove(file)
            count = count + 1
    
    log_file.write(str(removed_files)+"\n")
    end_time = time.time()
    log_file.write(border+"\n")
    log_file.write(f"Time taken to execute the script : {end_time - start_time}\n")
    log_file.write("-------------- End of Script --------------\n")
    log_file.write("-------------- Thank you for using our Script --------------\n")
    


    




def main():
    argv_len = len(sys.argv)
    print(argv_len)
    if argv_len != 2:
        print("Invalid number of arguments.Please give 2 arguments.")
    else:
        directory_name = sys.argv[1]
        find_duplicates(directory_name)

if __name__ == "__main__":
    main()