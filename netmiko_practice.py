from netmiko import ConnectHandler
#create a dictionary to represent a device
cisco_ios_xr = {
    'device_type':'cisco_xr',
    'host': 'sandbox-iosxr-1.cisco.com',
    'username':'admin',
    'password':'C1sco12345'
}

commands_list = ['show run','do show ip interface brief','do show ip bgp','do show ip ospf neighbor']
#context manager with device connector, no need to use disconnect line if we are using context manager
with ConnectHandler(**cisco_ios_xr) as net_connect:
    #net_connect = ConnectHandler(**cisco_ios_xr)
    print(f"Successfully Connected to a device: {cisco_ios_xr['device_type']}")
    for commands in commands_list:
        output = net_connect.send_config_set(commands)
        print(output)
#similarly send_config_from_file is used to execute the commands from the files
    #output = net_connect.send_command("show run")
    #print(output)
    #print(net_connect.find_prompt())
    #print(net_connect.config_mode())#enter to config mode
    #print(net_connect.find_prompt())
    #print(net_connect.check_config_mode())
    #print(net_connect.check_enable_mode())
    #print(net_connect.send_command("ping 8.8.8.8 repeat 5",read_timeout=20))
    #bydefault in netmiko readtimeout is 10 sec if it is taking more time for output to display so we need to increase the read timeout

#net_connect.disconnect()