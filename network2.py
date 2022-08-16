#!/usr/bin/env python
from netmiko import Netmiko
from getpass import getpass

#dictionary of connection info
cisco1 = {
    'host': 'cisco1.twb-tech.com', 
    'username': 'pyclass', 
    'password': getpass(), 
    'device_type': 'cisco_ios',
}


#unpack the dictionary
net_connect = Netmiko(**cisco1)

#display
print(net_connect.find_prompt())

#terminate SSH connection
net_connect.disconnect()
