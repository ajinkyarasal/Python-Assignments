#2. Design automation script which accept directory name and two file extensions from user.
# Rename all files with first file extension with the second file extention.
# Usage : DirectoryRename.py "Demo"" txt" " doc"
# Demo is name of directory and txt is the extension that we want to search 
# and rename with .doc.
# After execution this script each txt file gets renamed as doc.


import sys
import os
import time
def file_extension_changer(directory_name, from_extension,to_extension):
    ret = False
    ret = os.path.exists(directory_name)
    if ret == False:
        print("Given directory does not exists")
        return
    
    ret = os.path.isdir(directory_name)
    if ret == False:
        print("Given name is not a directory.")
        return
    
    border = ("*" * 45)
    timestamp = time.ctime()
    log_file_name = "file_extension_changer_%s" %(timestamp)
    log_file_name = log_file_name.replace(" ","_").replace(":","_")
    log_file_obj = open(log_file_name,"w")
    log_file_obj.write(border+"\n")
    log_file_obj.write("******** File Extension Changer Script ************"+"\n")

    target_files = []
    for folders,subfolders,files in os.walk(directory_name):
        for file in files:
            if file.endswith(from_extension):
                file = os.path.join(folders,file)
                target_files.append(file)
                new_file_name = file.replace(from_extension,to_extension)
                os.rename(file,new_file_name)
    
    log_file_obj.write(f"Below {from_extension} files extension are now changed to extension {to_extension}"+"\n")
    for f in target_files:
        log_file_obj.write(f+ "\n")
    
    log_file_obj.write("*********** End of Report ***********")
    log_file_obj.close()

    


def main():
    if len(sys.argv) == 4:
        directory_name = sys.argv[1]
        from_file_extension = sys.argv[2]
        to_file_extension = sys.argv[3]

        file_extension_changer(directory_name=directory_name,from_extension=from_file_extension,to_extension=to_file_extension)
    else:
        print("Invalid number of arguments.")

if __name__ == "__main__":
    main()
