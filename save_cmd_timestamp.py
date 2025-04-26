from paramiko import client
import time
import datetime

now = datetime.datetime.now().replace(microsecond=0)

ssh_client = client.SSHClient()
username = 'admin'
hostname = 'sandbox-iosxr-1.cisco.com'
password = 'C1sco12345'

ssh_client.set_missing_host_key_policy(client.AutoAddPolicy())
ssh_client.connect(hostname=hostname, username=username, port =22, password=password,look_for_keys=False)


device_access = ssh_client.invoke_shell()
device_access.send(f'terminal length 0\n')
time.sleep(2)
print(f"Conncted to {hostname} Sucessfully")


with open ('save_cmd_timestamp.txt') as filename:
    command = filename.readlines() # convert it into list
    for commands in enumerate(command,start=1):
        file_name = (f"{str(now).replace(':','_')}_{str(commands[0])}_{str(commands[1]).replace(" ","_").strip()}.txt")
        #print(file_name)
        with open (file_name,'w') as cmd_data:
            #it will create a folder of that name.
           device_access.send(commands[1])
           #send the commnds 1 by 1 
           time.sleep(2)
           output = device_access.recv(65535)
           cmd_data.write(output.decode())
           # this code will write the output into the text files
           print(output.decode(), end ='')

ssh_client.close()