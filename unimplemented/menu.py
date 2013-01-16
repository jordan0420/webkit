
def menu()
    print'1...Initiate a crawl'
    print'2...Launch a Denial of Service'
    print'3...Generate Proxies'
    print'4...Brute Force A Website Login'
    print'5...Run a Port Scan'
    print'6...Generate a word list'
    print'7...Scan a network for alive hosts'
    print'8...create possible users from a firstname lastname file'
    #This is an incomplete method needs to save the output rather than print it
    print'9...bruteforce hidden pages on a website'
    # This method is unfinnished, it needs a wordlist
    
    user_choice = raw_input('>')
    if user_choice == '1':
        crawlersetup()
    elif user_choice == '2':
        DOS()
    elif user_choice == '3':
        proxies()
    elif user_choice == '4':
        nullforce()
    elif user_choice == '5':
        portscan()
    elif user_choice == '6':
        wordgen()
    elif user_choice == '7':
        print 'Unfinnished Method'
        net_scan()
    elif user_choice == '8':
        'Incomplete Method'
#        file in ice 210
    elif user_choice == '9':
        urlbrute()
    print'Welcome to Webkit'
    print'\nChoose between a previous session'
    print'or press enter for a new session\n'
    print'Previous Sessions:'

