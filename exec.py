from paramiko import client
import time

username = 'admin'
hostname = 'sandbox-iosxr-1.cisco.com'
password = 'C1sco12345'

ssh_client = client.SSHClient()

cisco_cmd_exec = 'show ip interface brief'

ssh_client.set_missing_host_key_policy(client.AutoAddPolicy())
ssh_client.connect(hostname = hostname, username = username, port = 22, password = password, look_for_keys=False)

print(f"Successfully connected to Cisco device {hostname}")
def cisco_device(hostname,cmd):
    #for command in cmd:
    stdin,stdout,stderr = ssh_client.exec_command(cmd)
    print(stdout.read().decode())
    err = stderr.read().decode()
    if err:
        print(f"Error Occured {err}")

    ssh_client.close()

cisco_device('sandbox-iosxr-1.cisco.com',cisco_cmd_exec)