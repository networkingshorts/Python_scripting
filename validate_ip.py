import re
validate_ip = input(f"Enter IP to validate IP Address: ")

my_pattern = (r'^(25[0-5]|2[0-4][0-9]|1?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|1?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|1?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|1?[0-9][0-9]?)$')




if re.fullmatch(pattern=my_pattern,string=validate_ip):
    print(f"{validate_ip} is a valid IP Address")
else:
    print(f"{validate_ip} Not a Valid IP Address")