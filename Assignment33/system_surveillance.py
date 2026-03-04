import schedule
import sys
import time
import os
import psutil

def process_scan():
    list_process = []
    #warm up 
    for proc in psutil.process_iter():
        try:
            proc.cpu_percent()
        except:
            pass

    time.sleep(0.2)
    for proc in psutil.process_iter():
        try:
            info = proc.as_dict(attrs = ["pid","name","username","status","create_time","num_threads","open_files"])
            #convert create_time
            try:
                info["create_time"] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(info["create_time"]))
            except:
                info["create_time"] = "NA"
            
            info["cpu_percent"] = proc.cpu_percent(None)
            info["memory_percent"] = proc.memory_percent()
            info["rss"] = proc.memory_info().rss
            info["vms"] = proc.memory_info().vms

            list_process.append(info)
        except (psutil.NoSuchProcess,psutil.AccessDenied,psutil.ZombieProcess):
            pass

    return list_process




def create_log(folder_name):
    if len(folder_name) == 0:
        print("No folder path given.")
        return
    
    ret = os.path.exists(folder_name)
    if ret == True:
        ret = os.path.isdir(folder_name)
        if ret == False:
            print("Unable to create folder")
            return
        else:
            print("Directory already exists. Using the existing directory for log generation.")
    else:
        os.mkdir(folder_name)
        print("Directory for log files created successfully.")


    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    file_name = "Marvellous_%s.log" %timestamp
    log_file_path = os.path.join(folder_name,file_name)
    border = "-"*66
    file_obj = open(log_file_path,"w")
    file_obj.write(border+"\n")
    file_obj.write("------------------- System Surveillance Script -------------------\n")
    file_obj.write(border+"\n\n")

    file_obj.write("-------------------------- System Report --------------------------\n")

    #CPU Percent
    file_obj.write("CPU Usage : %s %%\n" %psutil.cpu_percent())

    #RAM Usage
    mem = psutil.virtual_memory()
    file_obj.write("RAM usage : %s %%\n" %mem.percent)

    file_obj.write("\nDisk Usage Report\n")
    for part in psutil.disk_partitions():
        try:
            usage = psutil.disk_usage(part.mountpoint)
            file_obj.write("%s -> %s %% used\n" %(part.mountpoint,usage.percent))
        except:
            pass
    
    file_obj.write(border+"\n")

    file_obj.write("\nNetwork Usage Report\n")
    
    netwrk = psutil.net_io_counters()
    file_obj.write("Sent : %.2f MB\n" %(netwrk.bytes_sent / (1024 * 1024)))
    file_obj.write("Received : %.2f MB\n" %(netwrk.bytes_recv / (1024 * 1024)))
    file_obj.write(border+"\n")

    #Process Log
    data = process_scan()
    file_obj.write("Process Scan Report\n")
    file_obj.write(border+"\n")
    for info in data:
        file_obj.write("PID : %s\n" %info.get("pid"))
        file_obj.write("Name : %s\n" %info.get("name"))
        file_obj.write("Username : %s\n" %info.get("username"))
        file_obj.write("Status : %s\n" %info.get("status"))
        file_obj.write("Start time : %s\n" %info.get("create_time"))
        file_obj.write("CPU %% : %.2f\n" %info.get("cpu_percent"))
        file_obj.write("Memory %% : %.2f\n" %info.get("memory_percent"))
        file_obj.write("Number of threads : %s\n" %(info.get("num_threads")))
        file_obj.write("Number of open files : %s\n" %(len(info.get("open_files") or [])))
        file_obj.write("rss : %s\n" %(info.get("rss")))
        file_obj.write(border+"\n")

    file_obj.write(" ----------------- End of process Report ----------------- \n")

    file_obj.write("----------------- Top 10 memory consuming process : -----------------\n")
    new_data = sorted(data, key = lambda x : x.get("rss"),reverse=True)
    for p in new_data[:10]:
        file_obj.write(f"PID : {p.get("pid")} rss : {p.get("rss")} vms : {p.get("vms")} memory percent: {p.get("memory_percent")}\n")
    


    

def main():
    print(psutil.cpu_percent())
    border = "-"*66
    print(border)
    print("------------------- System Surveillance Script -------------------")
    print(border)

    #python3 system_surveillance.py 5 surveillance_logs
    argv_len = len(sys.argv)
    if argv_len != 3:
        print("Invalid arguments. Please give 3 arguments.")
        return
    else:
        script_interval = int(sys.argv[1])
        script_log_folder = sys.argv[2]

        create_log(script_log_folder)

        # #create schedule
        # schedule.every(script_interval).minutes.do(create_log,script_log_folder)

        # while True:
        #     schedule.run_pending()
        #     time.sleep(1)

if __name__ == "__main__":
    main()