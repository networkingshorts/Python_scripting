from paramiko import client, ssh_exception
import time
import sys
import socket
username = 'admin'
hostname = 'sandboxx-iosxr-1.cisco.com'
password = 'C1sco12345'


cisco_cmd = ['conf t','int lo101','ip address 101.101.101.1 255.255.255.0','no shut','commit','end','show ip interface brief']

ssh_client = client.SSHClient()

ssh_client.set_missing_host_key_policy(client.AutoAddPolicy())


def cisco_device(hostname,cmd):
    try:
        ssh_client.connect(hostname=hostname,username=username,port=22,password=password,look_for_keys=False)

        print(f"Device is successfully connected to {hostname}")
        device_access = ssh_client.invoke_shell()
        device_access.send('terminal length 0 \n')
        for commands in cmd:
            device_access.send(f'{commands}\n')
            time.sleep(2)
            output = device_access.recv(65535)
            print(output.decode(), end='')
        ssh_client.close()
    
    except ssh_exception.AuthenticationException:
        print("Authentication Failed, Check is your credentials are correct")

    except socket.gaierror:
        print("Check if your hostname is correct")
    
    except ssh_exception.NoValidConnectionsError:
        print("SSH Port not reachable")
    except:
        print("Exception Occured")
        print(sys.exc_info())

cisco_device('sandboxx-iosxr-1.cisco.com',cisco_cmd)
