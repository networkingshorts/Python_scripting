from paramiko import client
import time

ssh_client = client.SSHClient()

ssh_client.set_missing_host_key_policy(client.AutoAddPolicy())

juniper_cmd = ['conf t', 'router ospf 1', 'commit','end']
cisco_cmd = ['show ip interface brief','conf t','int g0/0/0/0','ip address 100.100.100.1 255.255.255.255','no shut','end']


username = 'admin'
hostname = 'sandbox-iosxr-1.cisco.com'
password = 'C1sco12345'

def cisco_ios_xr(hostname,cmd):
    

    ssh_client.connect(hostname = hostname, username = username, password = password, port = 22, look_for_keys= False)
    print(f"Device is successfully connected to {hostname}")
    device_access = ssh_client.invoke_shell()
    device_access.send("terminal len 0 \n")
    for command in cmd:

        device_access.send(f"{command}\n")
        time.sleep(2)
        output = device_access.recv(65535)
        print(output.decode())
    device_access.send("show ip interface brief")
    time.sleep(5)
    output = device_access.recv(65535)
    print(output.decode(),end="")
    ssh_client.close()


cisco_ios_xr('sandbox-iosxr-1.cisco.com',cisco_cmd)

def juniper():
    username = 'admin'
    hostname = 'sandbox-iosxr-1.cisco.com'
    password = 'C1sco12345'

    ssh_client.connect(hostname = hostname, username = username, password = password, port = 22, look_for_keys= False)
    print(f"Device is successfully connected to Juniper")
    device_access = ssh_client.invoke_shell()
    device_access.send("terminal len 0 \n")
    for cmd in juniper_cmd:

        device_access.send(f"{cmd}\n")
        time.sleep(1)
        output = device_access.recv(65535)
        print(output.decode(), end='')
    device_access.send("show running-config router ospf")
    time.sleep(5)
    output = device_access.recv(65535)
    print(output.decode(),end="")
    ssh_client.close()

#juniper()



