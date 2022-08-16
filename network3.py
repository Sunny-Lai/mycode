#!/usr/bin/env python
from netmiko import Netmiko
from getpass import getpass

#password key
password = getpass()

#dictionary of connection info
cisco1 = {
    'host': 'cisco1.twb-tech.com', 
    'username': 'pyclass', 
    'password': password,
    'device_type': 'cisco_ios',
}

#dictionary of connection info
cisco2 = {
    'host': 'cisco2.twb-tech.com', 
    'username': 'pyclass', 
    'password': password,
    'device_type': 'cisco_ios',
}

#dictionary of connection info
nxos1 = {
    'host': 'nxos1.twb-tech.com', 
    'username': 'pyclass', 
    'password': password,
    'device_type': 'cisco_nxos',
}

#dictionary of connection info
srx1 = {
    'host': 'srx1.twb-tech.com', 
    'username': 'pyclass', 
    'password': password,
    'device_type': 'juniper_junos',
}

#looping across dictionaries, unpacking the dictionary, issue command, and show results
for device in (cisco1, cisco2, nxos1, srx1):
    net_connect = Netmiko(**device)
    print(net_connect.find_prompt())
