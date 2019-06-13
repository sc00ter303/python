#iosv_l2_config file
vlan 2
name Management
#
int rang g0/1 - 3
swi trunk encap dot1q
swi mode trunk
swi nonegotiate
swi trunk allowe vlan 1,2,100,101
spanning-tree link-type point-to-point
#
int rang g1/0 - 1
swi trunk encap dot1q
swi mode trunk
swi nonegotiate
swi trunk allowe vlan 1,2,100,101
spanning-tree link-type point-to-point