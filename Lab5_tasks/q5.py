def cpu_monitor(processes):
    """Calculate total CPU usage per process and alert if CPU usage > 100% and print this process"""
    process_cpu = {}    
    for process, cpu in processes:
        if process in process_cpu:
            process_cpu[process] += cpu
        else:
            process_cpu[process] = cpu
    return process_cpu    

def print_exceed_limit(processes):
    """Print processes that exceed CPU limit of 100%"""
    process_cpu = cpu_monitor(processes)
    for process, cpu in process_cpu.items():
        if cpu >= 100:
            print(f"ALERT: Process '{process}' CPU usage is {cpu}%")
          

processes = [ 
    ("nginx", 30), 
    ("python", 95), 
    ("mysql", 85), 
    ("redis", 20), 
    ("python", 90) 
] 
print(cpu_monitor(processes))
print_exceed_limit(processes)