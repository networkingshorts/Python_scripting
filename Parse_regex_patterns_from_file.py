import re
hostname = re.compile(r'your favorite (.*)')
interfaces = re.compile(r'interface (.*)')
ip_address = re.compile(r'interface (.*)\n\n ipv4 address (\d.+)')
with open('show_running-config.txt') as running_config:
    output=running_config.read()
    hostname_parse=hostname.search(output)
    print("Hostname".ljust(18)+":" +str(hostname_parse.group(1)))
    interface_parse=interfaces.finditer(output)
    interface_list = list()
    for interface in interface_parse:
        interface_list.append(interface.group(1))
    print(interface_list)


