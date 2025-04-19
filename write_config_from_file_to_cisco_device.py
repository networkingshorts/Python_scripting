from paramiko import client, ssh_exception
import time
import os
import socket
username = 'admin'
hostname = 'sandbox-iosxr-1.cisco.com'
password = 'C1sco12345'


print(f'Current Working Directory is: {os.getcwd()}')



def device_cisco(hostname):
    try:
        ssh_client = client.SSHClient()

        ssh_client.set_missing_host_key_policy(client.AutoAddPolicy())
        ssh_client.connect(hostname=hostname,username=username,password=password,port=22,look_for_keys=False)


        device_access = ssh_client.invoke_shell()
        device_access.send('terminal len 0\n')
        with open ('write_to_device.txt','r') as write_to_device:
            cmd = write_to_device.readlines()
            for command in cmd:
                device_access.send(f'{command}\n')
                time.sleep(2)
                output = device_access.recv(65535)
                print(output.decode())
    except ssh_exception.AuthenticationException:
        print("Authentication Failed, Check Credentials")
    except socket.gaierror:
        print("Check the hostname")

    
    ssh_client.close()

device_cisco('sandbox-iosxr-1.cisco.com')

