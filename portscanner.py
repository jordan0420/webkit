def scan_server(address, port):
    s = socket.socket()
    #print 'Attempting to connect to %s on port %s' %(address, port)
    try:
        s.connect((address, port))
        #print 'Connected to server %s on port %s' %(address, port)
        return True
    except socket.error, e:
        #print ' Connecting to %s on port %s failed with the following error: %s' %(address, port, e)
        return False


def portscan():
    target = raw_input('Target IP:')
    ports = raw_input('Target Port:')
    if ports == 'all':
        print'Checking all ports...'
        for x in range(65535):
            #print 'Checking pors %s on %s' %(x, target)
            check = scan_server(target, x)
            if check == True:        
                print 'scan_server returned %s on port %s' %(check, x)
    else:
        port = int(ports)
        #print 'options: %s, args: %s' %(options, args)
        check = scan_server(target, port)
        print 'scan_server returned %s' %(check)
        sys.exit(not check)
    print 'Scan Complete'

