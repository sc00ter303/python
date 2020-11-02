
#!/usr/bin/env python

from netmiko import Netmiko
from netmiko import ConnectHandler
import time
import re

# 10.145.32.1
print()
ipaddr = input ('Enter the hostname or IP Address:  ')
interface = input ('Enter the switchport number to be tested:  ')

cisco = {
     'device_type': 'cisco_ios',
     'host': ipaddr,
     'username': '169344',
     'password': '5t0mper123!',
     'timeout': 35 * 60,
	 'global_delay_factor': 12,
}


net_connect = ConnectHandler(**cisco)
# testdr = 'test cable-diagnostic tdr int'
# shtdr = 'show cable-diagnostic tdr int'

output1 = net_connect.send_command('test cable tdr int ' + interface)

output2 = net_connect.send_command('sh cable tdr int ' + interface)
print()
print('TDR TEST RESULTS FOR INTERFACE:  ')
print()
print(output2)
