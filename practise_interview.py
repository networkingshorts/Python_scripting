from paramiko import client

import time

username = 'admin'
hostname='sandbox-iosxr-1.cisco.com'
password = 'C1sco12345'


ssh_client = client.SSHClient()
ssh_client.set_missing_host_key_policy(client.AutoAddPolicy())
ssh_client.connect(hostname=hostname,username=username,port=22,password=password,look_for_keys=False)
print(f'Successfully Connected to a device: {hostname}')
device_access = ssh_client.invoke_shell()


device_access.send('terminal length 0 \n')
time.sleep(2)
device_access.send('show ip interface brief\n')
time.sleep(2)
output = device_access.recv(65535)
print(output.decode())

ssh_client.close()