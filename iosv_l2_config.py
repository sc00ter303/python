#iosv_l2_config file
vlan 2
name Management
#
int range g2/0 - 3
swi mod acc
swi mo acc vl 2
#
int rang g0/0 - 3
swi trunk encap dot1q
swi mode trunk
swi nonegotiate
swi trunk allowe vlan 1,2
#
int rang g1/0 - 1
swi trunk encap dot1q
swi mode trunk
swi nonegotiate
swi trunk allowe vlan 1,2