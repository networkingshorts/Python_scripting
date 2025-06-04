
from netmiko import ConnectHandler

class NetworkDevice:
    def __init__(self,device):
        self.device = device
        self.connect = ConnectHandler(**self.device)
    
    def push_config(self):
        config_command = ["router ospf 1",
        "network 10.1.1.1",
        "0.0.0.255 area 0"]
        output = self.connect.send_config_set(config_command)
        print(output)
        print(f"Configuration Pushed to {self.device['host']}")

devices = [{ 'device_type':'cisco_xr',
    'host': 'sandbox-iosxr-1.cisco.com',
    'username':'admin',
    'password':'C1sco12345'
},
 {'device_type':'cisco_xr',
    'host': 'sandbox-iosxr-1.cisco.com',
    'username':'admin',
    'password':'C1sco12345'
},
 {'device_type':'cisco_xr',
    'host': 'sandbox-iosxr-1.cisco.com',
    'username':'admin',
    'password':'C1sco12345'
}]

for dev in devices:
    configurator = NetworkDevice(dev)
    configurator.push_config()
    #configurator.disconnect()


