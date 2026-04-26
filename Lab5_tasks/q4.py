def command_monitor(commands):
    """Monitor each command whether each command succeeded or failed 
     & Count the number of failed commands """
    failed_count = 0
    for command, code in commands:
        if code != 0:
            print(f"Command '{command}' failed with status {code}")
            failed_count += 1
        else:
            print(f"Command '{command}' executed successfully.")

    print(f"\nTotal failed commands: {failed_count}")



commands = [ 
    ("ls", 0), 
    ("mkdir test", 0), 
    ("rm important.txt", 1), 
    ("cp file1 file2", 0) 
] 
command_monitor(commands)