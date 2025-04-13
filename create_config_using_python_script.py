from paramiko import client
import time

username = 'admin'
hostname='sandbox-iosxr-1.cisco.com'
password = 'C1sco12345'
ssh_client = client.SSHClient()

ssh_client.set_missing_host_key_policy(client.AutoAddPolicy())
ssh_client.connect(hostname=hostname, username = username, port = 22, password= password, look_for_keys=False)


config = ['conf t', 'int lo100', 'ip address 100.100.100.1 255.255.255.255', 'commit', 'end']
print("You have been logged in Successfully")


device_access = ssh_client.invoke_shell()

for cmd in config:

    device_access.send(f"{cmd}\n")
    output = device_access.recv(65535)
    time.sleep(1)
    print(output.decode())

device_access.send("show run int lo100\n")
time.sleep(2)
output = device_access.recv(65535)
print(output.decode())
ssh_client.close()