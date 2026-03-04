#Add Thread monitoring feature
# For each running process , display
#   Process Name
# PID
# Number of Threads created by that process
# Requirement
# Store information in log file along with timestamp.

import psutil
import time
import os
import sys
import schedule
from mail_sender import send_email

def process_scan():
    list_process = []
    #warm up 
    for proc in psutil.process_iter():
        try:
            proc.cpu_percent()
        except:
            pass

    #calculate actual values now
    for proc in psutil.process_iter():
        try:
            info = proc.as_dict(attrs=["pid","name","num_threads","create_time","open_files"])
            try:
                info["create_time"] = time.strftime("%Y-%m-%d %H:%M:%S" , time.localtime(info["create_time"]))
            except:
                info["create_time"] = "NA"
            
            info["cpu_percent"] = proc.cpu_percent()
            info["memory_percent"] = proc.memory_percent()
            info["rss"] = proc.memory_info().rss
            info["vms"] = proc.memory_info().vms
        except (psutil.NoSuchProcess, psutil.AccessDenied,psutil.ZombieProcess) as e:
            info["error"] = e
        
        list_process.append(info)
    
    return list_process
    

def create_log(folder_name):
    #folder validation
    ret = False
    ret = os.path.exists(folder_name)
    if ret:
        ret = os.path.isdir(folder_name)
        if ret == False:
            print("Unable to create folder")
            return
        else:
            print("Folder already exists. Using the same.")
    else:
        #create the path
        print(f"Creating {folder_name}")
        os.mkdir(folder_name)
        print(f"{folder_name} created successfully.")

    timestamp = time.strftime("%Y-%m-%d_%H:%M:%S")
    log_file = "Marvellous_%s.log" %(timestamp)
    log_file_path = os.path.join(folder_name,log_file)
    
    border = "-"*50
    with open(log_file_path,'w') as file:
        file.write(border+"\n")
        file.write(" -------------------- System Surveillance Script -------------------- \n")
        file.write(border+"\n")
        file.write(" --------------------- Process Scan Report --------------------- \n")
        file.write(border+"\n\n")
        
        data = process_scan()

        for info in data:
            file.write(border+"\n")
            file.write(f"Create time : {info.get("create_time")}\n")
            file.write(f"Process Name : {info.get("name")}\n")
            file.write(f"PID : {info.get("pid")}\n")
            file.write(f"Number of threads : {info.get("num_threads")}\n")
            file.write(f"Number of files opened : {len(info.get("open_files") or [])}\n")
            file.write(f"Errors : {info.get("error")}\n")
            file.write(f"RSS : {info.get("rss")}\n")
            file.write(f"VMS : {info.get("vms")}\n")
            file.write(f"Memory Percentage : {info.get("memory_percent")}\n")
        
        file.write(" ----------- Top 10 Memory Consuming Process ----------- \n")
        
        data_sorted = sorted(data,key= lambda x : x.get("rss") or 0,reverse=True)
        for p in data_sorted[:10]:
            file.write(f"PID : {p.get("pid")} rss : {p.get("rss")} vms : {p.get("vms")} memory percent: {p.get("memory_percent")}\n")

        file.write(" ----------- End of Script ----------- \n")

    return log_file_path

def create_and_email_logs(folder_path,receivers_email):
    log_file_path = create_log(folder_path)
    timestamp = time.ctime()
    sender = "studentajinkya@gmail.com"
    app_password = "fxgo ogum yalb gvfy"
    receivers_email = receivers_email
    subject = f"System Surveillance Report {timestamp}"
    body = """Hello,
        Please find attached report in the email
        
        Kind regards,
        System Admin
        """
    send_email(sender,app_password, receivers_email,subject,body,log_file_path)
    

def main():
    len_argv = len(sys.argv)
    if len_argv != 4:
        print("Invalid number of arguments. Please give the command as  below: \n")
        print("python3 filename.py log_folder_path receivers_email schedule_time in minutes")
    else:
        folder_path = sys.argv[1]
        receivers_email = sys.argv[2]
        script_interval = int(sys.argv[3])

        schedule.every(script_interval).minutes.do(create_and_email_logs,folder_path,receivers_email)

        while True:
            schedule.run_pending()
            time.sleep(1)
    


if __name__ == "__main__":
    main()