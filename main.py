#!/usr/bin/env python
import os
import sys
#import banner
#import portscanner

#from core import banner
from core import Colors
from core import prompts
from core import Interface
#from core import targetfinder
#from core import dos
#from core import netscan
#from core import nmapparser
#from core import nullforce
#from core import portscanner
#from core import urlbrute
#from core import usercreater
#from core import wordgen

Color = Colors.Color()
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
#    """ The following code is used to determine a choice for the user"""
#    answer = raw_input("Answer: ")
#    x = prompts.Prompts(answer)
#    #print x.yes_no(answer)
#    if x.yes_no() is True:
#        #print x.yes_no
#        print "True"
#    else: 
#        print x.yes_no()
#        print "False"
    Color.CYAN()
    print'\t \t Welcome to Webkit \n \n'
    session_choice()
def session_choice():
    os.chdir('sessions')
    if os.listdir('.') == []:
        Color.RED()
        print 'No previous sessions found'
        Color.GREEN()
        print 'Creating new session'
        new_session()
    Color.GREEN()
    a = 0
    print'\nChoose between a previous session'
    print'or press enter for a new session\n'
    Color.BLUE()
    for session_dir in os.walk('.').next()[1]:
        a += 1 
        print a,'.....', session_dir
    session = raw_input("Session Directory: ")
    if session == '':
        new_session()
    else:
        a = os.walk('.').next()[1]
        session = (int(session) - 1)
        session_select(session)
def session_select(session_directory):
        #session_directory = a[session]
        # print "Session Directory: ", session_directory
        os.chdir(str(session_directory))
        os.system('pwd')
        framework(session_directory)
def new_session(session_name = None):
    if session_name == None:
        session_name = raw_input("Name of the new session: ")
    if os.path.exists(session_name):
        print "This directory already exists"
        print "do you want to use the existing session [y]"
        print "or use a different name [n]"
        answer = raw_input("Answer: ")
        x = prompts.Prompts(answer)
        #print x.yes_no(answer)
        if x.yes_no() is True:
            os.chdir(session_name)
        else: 
            new_session()
    else:
        os.mkdir(session_name)
        os.chdir(session_name)
        os.system('pwd')
        framework(session_name)
def framework(session_directory):
    print session_directory
def interactivemode():
    print "Interactive mode"
    main()
def graphical_mode():
    print "graphical mode"
def console_mode():
    print "console mode"
    for index in range(arg_count):
        print sys.argv[index]
def help():
    print "help mode entered"
    print "Arguments: "
    print (
            "\t -g graphical mode " + 
            "\n\t -i interactive mode " +
            "\n\t -c console mode" +
            "\n\t -s [Session_directory] Specify a sesion directory" +
            "\n\t -h prints this help menu"
            )
def module_count():
    attack_vector_count = 0
    module_counter = 0
    for file in os.walk('core').next()[1]:
        print file
        attack_vector_count += 1
    print attack_vector_count
def info():
    print "info"
    print "Author: " + "Terminal Illness"
    print "Version: " + "1.0b"
    print "Modules: " + '1'
    module_count()
if __name__ == '__main__':
#    for arg in sys.argv:
#        print arg
#    print sys.argv[0]
    arg_count = len(sys.argv)
    if arg_count == 1:
        Color.RED()
        print "No arguements given, Defaulting to interactive mode"
        Color.GREEN()
        main()
    for index in range(arg_count):
        #print "index "+ str(index) + "sys.argv[index] " + str(sys.argv[index])
        if str(sys.argv[index])[1] == "g":
            print "graphical mode selected"
        if str(sys.argv[index])[1] == "s":
            #os.path.isdir
            os.chdir('sessions')
            if os.path.exists(str(sys.argv[(index + 1)])):
                #print "Session Exists"
                session_select(str(sys.argv[(index + 1)]))
            else:
                new_session(str(sys.argv[(index + 1)]))
#            print "session name given: "
#            print str(sys.argv[(index+1)])
        if str(sys.argv[index])[1] == 'h':
            help()
        if str(sys.argv[index])[1] == "c":
            print "console mode entered"
            console_mode()
        if str(sys.argv[index])[1:] == "info":
            info()
        #print sys.argv[index]
#        if arg_count[index] == '-i':
#            print "counter works!"
#    if sys.argv[1] == '-i':
#        print 'Interactive mode'
#    elif sys.argv[1] == '-g':
#        print 'graphical mode'
#    elif sys.argv[1] == '-c':
#        print 'console mode'
#    main()
    
