def login_attempts(logins, name):
    """Monitors login attempts for a specific user and alerts on 3 failed attempts"""
    flag = 0
    for user, status in logins:
        if user == name and status == "fail":
            flag += 1
    print(f"failed attempts: {flag}")

    if flag >= 3:
        print("Alert! 3 fail attempts suspicious!")
    elif flag == 0:
        print(f"No fail attempts for {name}")
    elif flag <3:
        print(f"Warning! {flag} fail attempts! for {name}")
            

logins = [ 
    ("ahmed", "success"), 
    ("root", "fail"), 
    ("root", "fail"), 
    ("root", "fail"), 
    ("sara", "success"), 
    ("root", "fail"), 
    ("ahmed", "fail") 
]         
login_attempts(logins, "sara")
login_attempts(logins, "ahmed")
login_attempts(logins, "root")

