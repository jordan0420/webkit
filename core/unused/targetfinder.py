
###############################################################################
# Standard imports
###
import Queue
import threading
from threading import Thread
import socket
import subprocess
import time

queue = Queue.Queue(0)
num_threads = 128
filename = 'targets.txt'
def start_scan():
 
    a = socket.gethostbyname(socket.gethostname())
    print "Currently connected as: " + a
    b = a.split('.')
    base_address = ''
    for addr in b[:3]:
        base_address += addr + '.'
        # print base_address, "Base Address"

    list_address = []
    for x in range(256):
        list_address.append(base_address + str(x))
        #print "list_address",list_address
    for address in list_address:
        queue.put(address)
    counter = len(list_address)
    print counter, 'nodes found'   
#list_address = ['www.google.com']
    #for ip in list_address:
#        ret = subprocess.call('ping -c 1 %s' %(ip),
#                              shell = True,
#                              stdout = open('/dev/null', 'w'),
#                              stderr = subprocess.STDOUT)
#        if ret == 0:
#            f = open(filename, 'a')
#            print "%s: is alive" % ip
#            #print queue.qsize(), 'remaining'
#            f.writelines(str(ip) + '\n')
#            f.close()
#        #threading.activeCount()

    for thread_run in range(num_threads):
        a = queue.get()
        t = Thread(target=ping, args=(a,))
        t.start()
    
def ping(ip):
    #queue

    #print 'pinging ip', ip, '\n'
    ret = subprocess.call('ping -c 1 %s' %(ip),
                          shell = True,
                          stdout = open('/dev/null', 'w'),
                          stderr=subprocess.STDOUT)
    ret
    #print ip, ret
    if ret == 0:
        f = open(filename, 'a')
        print "%s: is alive" % ip
        #print queue.qsize(), 'remaining'
        f.writelines(str(ip) + '\n')
        f.close()
#        if threading.activeCount() == 2:
#            print "starting to scan ports"
#            thread_scan()
#    else:
#        if threading.activeCount() == 2:
#            print "starting to scan ports"
#            thread_scan()
#        #threading.activeCount()
#    #else:
#    #    print threading.activeCount()
#        #for x in range(65535):
#            #print 'Checking pors %s on %s' %(x, target)
#        #    check = scan_server(ip, x)
#        #    if check == True:        
#        #        print '%s returned %s on port %s' %( ip, check, x)
#        #counter -= 1
##        print counter
##    else:
##        counter -= 1
##        print counter
#
#def scan_server(address, port):
#    s = socket.socket()
##    print 'Attempting to connect to %s on port %s' %(address, port)
#    print threading.activeCount()
#    try:
#        s.connect((address, port))
#        print 'Connected to server %s on port %s' %(address, port)
#        return True
#    except socket.error, e:
#        #print ' Connecting to %s on port %s failed with the following error: %s' %(address, port, e)
#        return False
#
#
#def portscan(target, port):
#
##    for target, port in pair:
##        for x in range(65535):
##    print 'Checking pors %s on %s' %(port, target)
##    print threading.activeCount()
#    check = scan_server(target, port)
#    if check == True:        
#        print 'scan_server returned %s on port %s is open ' %(target, port)
#def thread_scan():
#    targets = open('targets.txt')
#    load = targets.readlines()
#    targets.close()
#    port_targets = []
#    for target in load:
#        target = target.strip('\n')
#        for port in range(65535):
#            port_targets.append((target, port))
##    print port_targets
##    queue.queue.clear()
##    for pair in port_targets:
##        queue.put(pair)
##    test_pairs = len(port_targets)
##    for new_thread in range(num_threads):
##    for test_pair in test_pairs:
##    print 'test_pair', test_pairs
##    print 'queue.get()', queue.get()
##    print threading.activeCount()
#    #line = int(len(port_targets))    
#    #while line != 0:
#        for x in range(num_threads):
#            for (target, port) in port_targets:
#                try:
#                    t = Thread(target=portscan, args=(target,port))
#                    t.start()
#                except:
#                    print 'too bad'
#    #            line = line - 1
#    #            print line
#    #for (target, port) in port_targets:
#    #    portscan(target, port)
#queue = Queue.Queue(0)
#filename = 'targets.txt'
#num_threads = 128
#start_scan()