#Design automation script which accept two directory names. 
# Copy all files from first directory into second directory. 
# Second directory should be created at run time.
#Usage : DirectoryCopy.py "Demo" "Temp"
#Demo is name of directory which is existing and contains files in it. 
# We have to create new Directory as Temp and copy all files from Demo to Temp.
import sys
import os
import time
import shutil
def directory_copy(from_dir, to_dir):
    ret = False
    ret = os.path.exists(from_dir)
    if ret == False:
        print("There is no such directory")
        return
    
    ret = os.path.isdir(from_dir)
    if ret == False:
        print("The given name is not a directory.")
        return
    
    if len(to_dir) == 0:
        print("Invalid name of target directory.")
        return
    try:
        os.mkdir(to_dir)
    except FileExistsError:
        print(f"The {to_dir} directory already exists.")
    border = ("*" * 45)
    timestamp = time.ctime()
    log_file_name = "directory_copy_script_%s" %(timestamp)
    log_file_name = log_file_name.replace(" ","_").replace(":","_")
    log_file_obj = open(log_file_name,"w")
    log_file_obj.write(border+"\n")
    log_file_obj.write("******** Directory Copy Script ************"+"\n")

    files_copied = []
    for folder,subfolders,files in os.walk(from_dir):
        for file in files:
            files_copied.append(file)
            shutil.copy(os.path.join(folder,file),to_dir)
        
    log_file_obj.write(f"Below files were copied from {from_dir} to {to_dir}"+"\n")

    for f in files_copied:
        log_file_obj.write(f+"\n")

    log_file_obj.write("*********** End of Report ***********")
    log_file_obj.close()
    
def main():
    if len(sys.argv) == 3:
        from_directory = sys.argv[1]
        to_directory = sys.argv[2]

        directory_copy(from_dir=from_directory,to_dir=to_directory)
    else:
        print("Invalid number of arguments.")

if __name__ == "__main__":
    main()