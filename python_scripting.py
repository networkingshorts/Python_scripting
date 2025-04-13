from paramiko import client
import time

ssh_client = client.SSHClient()

ssh_client.set_missing_host_key_policy(client.AutoAddPolicy())

ssh_client.connect(hostname='sandbox-iosxr-1.cisco.com', port= 22, username = 'admin', password='C1sco12345', look_for_keys = False)

print("connected successfully")

device_access = ssh_client.invoke_shell()
device_access.send("terminal len 0\n")
device_access.send("show run\n")
time.sleep(5)



output = device_access.recv(65535)

print(output.decode())



ssh_client.close()