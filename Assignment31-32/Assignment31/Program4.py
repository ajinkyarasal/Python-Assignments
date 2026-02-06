#Design automation script which accept two directory names and one file extension. Copy all
# extension from
# files with the specified extension from first directory into second directory.
#  Second directory should be created at run time.
# Usage : DirectoryCopyExt.py "Demo" "Temp" " exe"
# Demo is name of directory which is existing and contains files in it. We have to create new
# ectory as Temp and copy all files with extension .exe from Demo to Temp.

import sys
import os
import time
import shutil
def directory_copy_extension(source,target,extension):
    ret = False
    ret = os.path.exists(source)
    if ret == False:
        print("There is no such directory")
        return
    
    ret = os.path.isdir(source)
    if ret == False:
        print("The given name is not a directory.")
        return
    
    if len(target) == 0:
        print("Invalid name of target directory.")
        return
    
    if len(extension) == 0:
        print("Invalid extension name.")
        return
    try:
        os.mkdir(target)
    except FileExistsError:
        print("The directory name already exists.")

    border = ("*" * 45)
    timestamp = time.ctime()
    log_file_name = "directory_copy_extension_%s" %(timestamp)
    log_file_name = log_file_name.replace(" ","_").replace(":","_")
    log_file_obj = open(log_file_name,"w")
    log_file_obj.write(border+"\n")
    log_file_obj.write("******** Directory Copy Extension Script ************"+"\n")

    target_files = []
    for folder, subfolders,files in os.walk(source):
        for f in files:
            if f.endswith(extension):
                target_files.append(f)
                shutil.copy(os.path.join(folder,f),target)

    log_file_obj.write(f"Below files were copied from {source} to {target}"+"\n")

    for f in target_files:
        log_file_obj.write(f+"\n")

    log_file_obj.write("*********** End of Report ***********")
    log_file_obj.close()


def main():
    argv_len = len(sys.argv)
    if argv_len == 4:
        source_directory = sys.argv[1]
        target_directory = sys.argv[2]
        target_extension = sys.argv[3]

        directory_copy_extension(source_directory, target_directory, target_extension)

    else:
        print(f"Invalid number of arguments : provided {argv_len} required 4.")

if __name__ == "__main__":
    main()