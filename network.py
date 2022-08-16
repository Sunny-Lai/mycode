#!/usr/bin/env python

#importing netmiko to interact with it
from netmiko import Netmiko

#importing get pass to interact with getpass for password creation
from getpass import getpass

#host=cisco1.twb-tech.com, username=pyclass, password=extract using getpass, device type=cisco_ios
net_connect = Netmiko('cisco1.twb-tech.com', username='pyclass',
                      password=getpass(), device_type='cisco_ios')

#display the results
print(net_connect.find_prompt())

#terminate SSH connection
net_connect.disconnect()
