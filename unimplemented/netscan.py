#! usr/bin/env python
###############################################################################
# This is for the network Scanner
###############################################################################
from threading import Thread
import socket
import subprocess
import time
def split_seq(seq, num_pieces):
    start = 0
    for i in range(num_pieces):
        stop = start + len(seq[i::num_pieces])
        yield seq[start:stop]
        start = stop

def net_scan():
    a = socket.gethostbyname(socket.gethostname())
    b = a.split('.')
    num_threads = raw_input('Thread Count Max 128')
    if num_threads == '':
        num_threads = 128
    num_threads = int(num_threads)
    print 'Currently connected to: ', a
    ip_stem = raw_input('IP Stem: ')
    if ip_stem == '':
        ip_stem = str(b[0] + '.' + b[1] + '.' + b[2])
    filename = raw_input('filename: ')
    ips = ['%s.%i' % (ip_stem, ip_end) for ip_end in range(256)]
    #ip_buckets = split_seq(ips, num_threads)
    # ip_buckets = []
    #for seq in split_seq(ips, num_threads):
    #    ip_buckets.append(seq)
    #print 'ip buckets: '
    #print ip_buckets
    for ip in ips:
        print 'ping ', ip                
        ret = subprocess.call("ping -c 1 %s" % ip,
                    shell=True,
                    stdout=open('/dev/null', 'w'),
                    stderr=subprocess.STDOUT)
        ret
        if ret == 0:
            f = open(filename, 'a')
            print "%s: is alive" % ip
            f.write(str(ip) + '\n')
            f.close()
    print time.ctime()
net_scan()
