###########################################
# This is the web crawler
###########################################
import re
import urllib
import sys
# Check for Index.html
# Check for robots.txt
def crawlermain(attack_domain, Depth, filename):
    textfile = file('depth_2.txt','wt')
    for i in re.findall('''href=["'](.[^"']+)["']''', urllib.urlopen(sys.argv[1]).read(), re.I):
        print i
#        for ee in re.findall('''href=["'](.[^"']+)["']''', urllib.urlopen(i).read(), re.I):
#            print ee
        textfile.write(i+'\n')
    textfile.close()

def crawlersetup(attack_domain):
    code = urllib.urlopen(attack_domain + str('/robots.txt')).code
    if type(code) is int:
       # print "code == Digit"
       # print code
        if ( code / 100 ) == 2:
            print "/robots.txt exists... \n Downloading now..."
            f = urllib.urlopen(attack_domain + str('/robots.txt'))
            s = f.read()
            print s
            f.close()
            print"Downloading complete... \n Saving to 'robots.txt'"
            fich=open('robots.txt','w')
            fich.write(s)
            fich.close()
        else:
            print "Error in finding", attack_domain, + '/robots.txt'
    code = urllib.urlopen(attack_domain + str('/index.html'))
    if type(code) is int:
        print code
        if ( int(code) / 100 ) == 2:
            print "/index.html exists... \n Downloading now..."
            f = urllib.urlopen(attack_domain + str('/index.html'))
            s = f.read()
            print s
            f.close()
            print"Downloading complete... \n Saving to 'index.txt'"
            fich=open('index.txt','w')
            fich.write(s)
            fich.close()
    else:
        print "Index.html could not be found..."        
    
#DEPTH = raw_input('Depth to Crawl: ')
#attack_domain = raw_input('Attack Domain: ')
#crawlermain(attack_domain, DEPTH, 'file.txt')
#crawlermain('www.uasdubai.ae', 2, 'file.txt')
crawlersetup('http://www.uasdubai.ae')
#    os.system('python crawler.py -d %s %s' %(DEPTH, attack_domain))


