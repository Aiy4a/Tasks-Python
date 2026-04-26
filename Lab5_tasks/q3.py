def disk_usage(disks):
    """Check disk usage"""
    count = 0
    for disk, usage in disks.items():
        if usage >= 90:
            count += 1
            print(f"CRITICAL cleanup required!  disk ({disk}) usage at {usage}%")
        elif usage > 80 and usage < 90:
            print(f"Warning!  disk ({disk}) usage at {usage}%")
        elif usage <= 80:
            print(f"OK!  disk ({disk}) usage at {usage}%")
    print(f"\nTotal disks need cleanup: {count}")

disks = { 
    "/": 85, 
    "/home": 70, 
    "/var": 92, 
    "/tmp": 60 
} 

disk_usage(disks)