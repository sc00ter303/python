vtp mode transparent
sapnning-tree mode rapid-pvst
udld enable
errdisable recovery cause all
port-channel load-balance src-dst-ip
ip name-server 8.8.8.8
no ip http server
ip http secure-server

snmp-server community pythonRO RO
snmp-server community pythonRW RW

ntp server 87.81.181.2
ntp update-calendar

clock timezone PST -8
clock summer-time PDT recurring
service timestamps debug datetime msec localtime
service timestamps log datetime msec localtime

vlan 100
 name Data
vlan 101
 name Voip

int vlan 2
 desc In-Band Management

ip default-gateway 192.168.122.1
ip dhcp snooping vlan 100,101

no ip dhcp snooping information option
ip dhcp snooping
ip arp inspection vlan 100,101
spanning-tree portfast bpduguard default
ipv6 nd raguard policy HOST_POLICY
 device-role host

interface range Gig 2/0 - 3
 switchport acc vlan 100
 switchport voice vlan 101
 switchport host
 switchport port-security maximum 2
 switchport port-security
 switchport port-security aging time 2
 switchport port-security aging type inactivity
 switchport port-security violation restrict
 ip arp inspection limit rate 100
 ip dhcp snooping limit rate 100
 ip verify source
 ipv6 nd raguard attach-policy HOST_POLICY

 
