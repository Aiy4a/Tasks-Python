def log_analyzer(logs):
    """Count how many messages exist for each log level """
    count = {"INFO" : 0 , "ERROR" : 0 , "WARNING" : 0}
    
    for i in range(len(logs)):
        log_level = (logs[i].split())[0]
        if log_level in count:
            count[log_level] += 1
    return count

def log_notification(logs):
    """print only ERROR and WARNING messages"""
    for i in range(len(logs)):
        log_level = (logs[i].split())[0]
        if log_level == "ERROR" or log_level == "WARNING":
            print(f"{logs[i]}")


def log_summary(logs):
    """Print a summary of all log levels and their counts"""
    count = log_analyzer(logs)
    for key, value in count.items():
        print(f"{key}: {value}")


logs = [ 
    "INFO system boot", 
    "ERROR disk full", 
    "WARNING memory high", 
    "ERROR permission denied", 
    "INFO service started", 
    "WARNING cpu high" 
] 

print(f"{log_analyzer(logs)}\n")
log_notification(logs)
print("\n")
log_summary(logs)