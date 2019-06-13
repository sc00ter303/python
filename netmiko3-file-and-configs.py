#!/usr/bin/env python

from netmiko import ConnectHandler

iosv_l2_s1 = {
	'device_type': 'cisco_ios',
	'ip': '192.168.122.71',
	'username': 'scott',
	'password': 'cisco',
}

iosv_l2_s2 = {
	'device_type': 'cisco_ios',
	'ip': '192.168.122.72',
	'username': 'scott',
	'password': 'cisco',
}

iosv_l2_s3 = {
	'device_type': 'cisco_ios',
	'ip': '192.168.122.73',
	'username': 'scott',
	'password': 'cisco',
}

iosv_l2_s3 = {
	'device_type': 'cisco_ios',
	'ip': '192.168.122.74',
	'username': 'scott',
	'password': 'cisco',
}

iosv_l2_s3 = {
	'device_type': 'cisco_ios',
	'ip': '192.168.122.75',
	'username': 'scott',
	'password': 'cisco',
}

#config file with configuration
with open('iosv_l2_config') as f:
	lines = f.read().splitlines()
print lines


all_devices = [iosv_l2_s5, iosv_l2_s4, iosv_l2_s3, iosv_l2_s2, iosv_l2_s1]

for devices in all_devices:
	net_connect = ConnectHandler(**devices)
    output = net_connect.send_config_set(config_commands)
    print output

#iosv_l2_config file
# vlan 2
# name Management
# int range g2/0 - 3
# swi mod acc
# swi mo acc vl 2
#
# int rang g0/0 - 3
# swi trunk encap dot1q
# swi mode trunk
# swi nonegotiate
# swi trunk allowe vlan 1,2
#
# int rang g1/0 - 1
# swi trunk encap dot1q
# swi mode trunk
# swi nonegotiate
# swi trunk allowe vlan 1,2