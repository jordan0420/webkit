###############################################################################
# This is for the URL BruteForcer
###############################################################################

def urlbrute():
    attack_domain = raw_input('Address to Brute: ')
    wordlist = raw_input('Wordlist: ')
    for word in wordlist:
        code = urlopen(attack_domain + str(word)).code
        if type(code) is int:
            #print "code == Digit"
            print code
            if ( code / 100 ) == 2:
                print attack_domain + str(word)        
    
