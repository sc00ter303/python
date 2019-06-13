#!/usr/bin/env python  (chmod +x filename)  execute file ./filename

import getpass
import sys
import telnetlib

user = raw_input("Enter you telnet username: ")
password = getpass.getpass()

for n in range (72,77):
	HOST = "192.168.122." + str(n)
	tn = telnetlib.Telnet(HOST)

	tn.read_until("Username: ")
	tn.write(user + "\n")
	if password:
		tn.read_until("Password: ")
		tn.write(password + "\n")
	
	tn.write("conf t\n")

	for n in range (2,11):
		tn.write("vlan " + str(n) + "\n")
		tn.write("name Python_VLAN_" +str(n) + "\n")

	tn.write("end\n")
	tn.write("wr\n")
	tn.write("exit\n")

	print tn.read_all()
