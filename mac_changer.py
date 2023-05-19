#!/user/bin/env python

import subprocess

print("[+] new mac address :")
mac_add = input()
print("[+] Choose Inter face below to change inter face mac address")
subprocess.call("iwconfig", shell=True)
print("[+] enter here: ")
interface_name = input()
print("[+] changing mac address for "+interface_name+" to "+mac_add)
subprocess.call("ifconfig "+interface_name+" down", shell=True)
subprocess.call("ifconfig "+interface_name+" hw ether "+mac_add, shell=True)
subprocess.call("ifconfig "+interface_name+" up", shell=True)
subprocess.call("ifconfig "+interface_name, shell=True)
