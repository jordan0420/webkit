import os
#import banner
#import portscanner

from core import banner
from core import colors
from core import targetfinder
#from core import dos
#from core import netscan
#from core import nmapparser
#from core import nullforce
#from core import portscanner
#from core import urlbrute
#from core import usercreater
#from core import wordgen
def webmenu():
    print "web"
def networkmenu():
    print "networks"
def wirelessmenu():
    print "Wireless"
def miscmenu():
    print "misc"
def initial():
    """ A menu to prompt the user for an attack vector"""
    print '1...Web'
    print ''
    print '2...Network'
    print ''
    print '3...Wireless'
    print ''
    print '4...Misc'
    print ''
    print '5...quit'
    user_choice = raw_input('>')
    if user_choice == '1':
        webmenu()
    elif user_choice == '2':
        networkmenu()
    elif user_choice == '3':
        wirelessmenu()
    elif user_choice == '4':
        miscmenu()
    elif user_choice == '5':
        print "Exiting now"
#def initial():
#    print'1...Initiate a crawl'
#    print'2...Launch a Denial of Service'
#    print'3...Generate Proxies'
#    print'4...Brute Force A Website Login'
#    print'5...Run a Port Scan'
#    print'6...Generate a word list'
#    print'7...Scan a network for alive hosts'
#    print'8...create possible users from a firstname lastname file'
#    #This is an incomplete method needs to save the output rather than print it
#    print'9...bruteforce hidden pages on a website'
#    # This method is unfinnished, it needs a wordlist
#    
#    user_choice = raw_input('>')
#    if user_choice == '1':
#        crawlersetup()
#    elif user_choice == '2':
#        dos.DOS()
#    elif user_choice == '3':
#        proxies()
#    elif user_choice == '4':
#        nullforce.nullforce()
#    elif user_choice == '5':
#        portscan.portscan()
#    elif user_choice == '6':
#        wordgen.wordgen()
#    elif user_choice == '7':
#        targetfinder.start_scan()
#    elif user_choice == '8':
#        'Incomplete Method'
##        file in ice 210
#    elif user_choice == '9':
#        urlbrute.urlbrute()

def main():
    print colors.color.RED
    banner.initial()
    print colors.color.GREEN
    
    print'Welcome to Webkit'
    print'\nChoose between a previous session'
    print'or press enter for a new session\n'
    print'Previous Sessions:'
    print colors.color.BLUE
    a = 0
    for session_dir in os.walk('.').next()[1]:
        a = a + 1    
        print a,'.....', session_dir
    session = raw_input("Session Directory: ")
    if session == '':
        name = raw_input('Name of the new session: ')
        os.mkdir(str(name))
        os.chdir((name))
        os.system('clear')
        os.system('pwd')
        initial()
    else:
        a = os.walk('.').next()[1]
        session = (int(session) - 1)
        session_directory = a[session]
        print "Session Directory: ", session_directory
        os.chdir(str(session_directory))
        os.system('clear')
        os.system('pwd')
        initial()


if __name__ == '__main__':
    main()
