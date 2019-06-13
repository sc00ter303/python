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


#config file for access switches

all_devices = [iosv_l2_s5, iosv_l2_s4, iosv_l2_s3]

with open('iosv_l2_access') as f:
	lines = f.read().splitlines()
print lines


#config file for core switches

all_devices = [iosv_l2_s2, iosv_l2_s1]

with open('iosv_l2_core') as f:
	lines = f.read().splitlines()
print lines



for devices in all_devices:
	net_connect = ConnectHandler(**devices)
    output = net_connect.send_config_set(config_commands)
    print output
