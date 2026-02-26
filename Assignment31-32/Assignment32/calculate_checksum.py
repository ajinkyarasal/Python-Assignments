import os
import hashlib
def calculate_checksum(file):
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