#1. Design automation script which accept directory name and display checksum of all files.
#Usage : DirectoryChecksum.py "Demo"
#Demo is name of directory.
import sys
import os
import hashlib
import time
def calculcate_checksum(file):
    ret = False
    ret =  os.path.exists(file)
    if ret == False:
        print("File does not exists")
        return
    
    file_obj = open(file, "rb")
    buffer = file_obj.read(1024)
    hash_obj = hashlib.md5()
    while len(buffer) > 0:
        hash_obj.update(buffer)
        buffer = file_obj.read(1024)

    file_obj.close()
    return hash_obj.hexdigest()

def directory_watcher(directory_name):
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
    log_file_name = "directory_watcher_%s" %(timestamp)
    log_file_name = log_file_name.replace(" ","_").replace(":","_")
    log_file_obj = open(log_file_name,"w")
    log_file_obj.write(border+"\n")
    log_file_obj.write("******** Directory Watcher Script ************"+"\n")

    for folder,subfolders,files in os.walk(directory_name):
        for f in files:
            checksum = calculcate_checksum(os.path.join(folder,f))
            log_file_obj.write(f"checksum of {f} is {checksum}"+"\n")

    log_file_obj.write("*********** End of Report ***********")
    log_file_obj.close()

def main():

    if len(sys.argv) == 2:
        directory_name = sys.argv[1]
        directory_watcher(directory_name)

    else:
        print("Invalid number of arguments.")


if __name__ == "__main__":
    main()