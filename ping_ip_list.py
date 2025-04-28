import os

ips = ["8.8.8.8","192.168.1.1","9.9.9.9","0.0.0.0"]


for ip in ips:
    response = os.system(f'ping -n 1 {ip} > null 2>&1')

    '''Part	Meaning
>	:   Redirect standard output (stdout).
nul	:   Special device in Windows that discards anything written to it (like a "trash bin" or "black hole").
2>&1 :	Redirect standard error (stderr) to standard output (stdout) — meaning, errors will also go to the trash (nul).


Syntax	Meaning
> nul	Hide normal output (stdout).
2>&1	Also hide error output (stderr).
> nul 2>&1	Hide both normal and error outputs.

'''




    if response == 0:
        print(f"{ip} is Reachable")
    else:
        print(f"{ip} is UnReachable")