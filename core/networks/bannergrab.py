import socket
def retBanner(ip, port):
    socket.setdefaulttimeout(2)
    s = socket.socket()
    s.connect((ip) + (port))
    ans = s.recv(1024)