#!/usr/bin/env python
from netmiko import Netmiko
from netmiko import ConnectHandler
import re

cisco = {
     'device_type': 'cisco_ios',
     'host': '10.145.0.11',
     'username': 'cisco',
     'password': 'cisco',
                'timeout': 35 * 60,
}


print()
print("running commands...")
net_connect = ConnectHandler(**cisco)


output = (net_connect.send_command('sh run | i hostname ').split()[1])
 
print()
print()   
print ('HOSTNAME:')
print()   
print(output)

output = (net_connect.send_command('sh run | i ip address 10 ').split()[2])  
print(output)

output = net_connect.send_command('sh clock')
  
print()
print()   
print ('CURRENT TIME:')
print()
print(output)

output = net_connect.send_command('sh int status | i connected')
 
print()
print()   
print ('CONNECTED INTERFACES:')
print()
print('Port      Name               Status       Vlan       Duplex  Speed Type')
print()
print(output)

output = net_connect.send_command('sh int | i Vlan|FastEther|GigabitEther|Last input.*00:')

print()
print()
print('LAST INPUT:')        
print()
print(output)
 
