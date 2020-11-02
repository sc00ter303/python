f = open('myswitches')

for line in f:
	print("sh ip route " + line)
	
f.close()