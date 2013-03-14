from hashlib import *
from string import *
import sys
import itertools
import time
version="1.0b"
print "Hashbreaker",version
print "Written by Daniel Seiller ( earthnuker[at]googlemail.com )\n\tThis software/script is open source\n\tfeel free to modify and redistribute it\n\tbut please give credit to the author\n"
def printhelp():
    print "Usage:"
    print "hashbreaker.py <hash> -r <rounds> -Rt <'single'/'multi'> [-b/-w] (-O)"
    print "-b will brute force"
    print "-w will read wordlist from file or stdin"
    print "-r will use <rounds> rounds"
    print "-O enables dynamic charset changing(faster in some cases)"
    print "\tdefault is to always use full character set"
    print "-c defines a custom charset for cracking"
    print "-Rt sets round type (single/multi)"
    print "\tmulti: checks the hash after every round"
    print "\tsingle: checks the hash after <rounds> rounds\n"
    print "Examples:"
    print "\thashforce.py <hash> -Rt single -r 1 -b"
    print "\thashforce.py <hash> -Rt multi -r 9 -w wl.txt"
    print "\thashforce.py <hash> -c abcdef -r 9 -w wl.txt"
    print "\thashforce.py <hash> -r 3 -w wl.txt"
    print "Press Enter to exit!",
    """
    Needed:
        hash
        option
        rounds
        round type
        brute or wordlist
        dyn charset
        wordlist location
    """
    raw_input()
    exit()
if len(sys.argv)<5:
    printhelp()
charset=""
args=sys.argv[1:]
pwhsh=args[0]
arglst=[]
acceptedargs=['-Rt','-r','-b','-w','-c','-O']
boolargs=['-b','-O']
intargs=['-r']
reptable={'-Rt':'rtype','-r':'rounds','-w':'wfile','-b':'brutef','-c':'charset','-O':'notfullch'}
brutef=False
notfullch=False
rounds=0
hlens={32:md5vbn,40:sha1,56:sha224,64:sha256,96:sha384,128:sha512}
hlensstr={32:"md5",40:"sha1",56:"sha224",64:"sha256",96:"sha384",128:"sha512"}
num=0
pwhash=chrl=fullch=htype=""
end=1
maxlen=20
wfile=""
for arg in args:
    if arg.startswith("-"):
        if arg in boolargs:
            arglst.append([arg,"True"])
        else:
            arglst.append([arg,args[args.index(arg)+1]])
for arg in arglst:
    if len(arg)==2:
        if arg[0] in acceptedargs:
            if arg[0] in intargs:
                exec(reptable[arg[0]]+"="+arg[1])
            else:
                exec(reptable[arg[0]]+"='"+arg[1]+"'")
if brutef:
    wfile=""
if rtype not in ['single','multi']: printhelp()
if not wfile and not brutef: printhelp()
if not rounds: printhelp()
try:
    pwhash=sys.argv[1]
except IndexError:
    printhelp()
print "generating charbook"
l=0
d={}
if not notfullch:
    charbook=[digits+ascii_lowercase+ascii_uppercase+punctuation+" "]
elif charset:
    charbook=[charset]
else:
    stff=[digits,ascii_lowercase,ascii_uppercase,punctuation+" "]
    strlst=[]
    n=1
    while l<=len(stff):
        for i in itertools.permutations(stff, l):
            stri=""
            for k in i:
                stri=stri+k
            lst=[x for x in stri]
            lst.sort()
            strlst.append("".join(lst))
        l=l+1
    strlst=list(set(strlst))
    for i in strlst:
        d[str(len(i))+str(n)]=i
        n=n+1
    keys = d.keys()
    keys.sort()
    charbook=map(d.get, keys)[1:]
print "done!"
while htype=="":
    if pwhash!="":
        try:
            htype=hlens[len(pwhash)]
            hname=hlensstr[len(pwhash)]
        except KeyError:
            print "unknown hash type..."
            exit()
    else:
        print "unknown hash type..."
        exit()
def calchash(x):
    return htype(x).hexdigest()
print "detected",hname,"hash"
pwhash=pwhash.lower()
def brute(c,l):
    cmdlst=[]
    varis=""
    for varp1 in ascii_uppercase:
        for varp2 in ascii_uppercase:
            var=varp1+varp2
            cmd=(len(cmdlst)+1)*"\t"+"for "+var+' in """'+c+'""":\n'
            varis=varis+var+"+"
            cmdlst.append(cmd)
            if len(cmdlst)==l:
                break
        if len(cmdlst)==l:
                break
    varis=varis[:-1]
    cmdlst.append((len(cmdlst)+1)*"\t"+"yield "+varis)
    cmdlst=["def dobrute():\n"]+cmdlst
    exec("".join(cmdlst))
    for pwst in dobrute():
        yield pwst
def check(pwstr,hsh,rnds,rtype):
    plain=pwstr
    if rtype=="single":
        for q in range(1,rnds+1):
            pwstr=calchash(pwstr)
        if str(hsh)==str(pwstr):
            print "pwhash="+plain,"rounds="+str(q)
            print "took", time.clock(),"seconds to crack"
            raw_input()
            exit()
    elif rtype=="multi":
        for q in range(1,rnds+1):
            pwstr=calchash(pwstr)
            if str(hsh)==str(pwstr):
                print "pwhash="+plain,"rounds="+str(q)
                print "took", time.clock(),"seconds to crack"
                raw_input()
                exit()
time.clock()
if brutef:
    while 1:
        for i in charbook:
            print "bruting",pwhash,"(",hname,")","with set ["+i+"] lenght:",end
            for pwstr in brute(i,end):
                check(pwstr,pwhash,rounds,rtype)
        end=end+1
        if end>maxlen:
            exit("maximum password lenght reached... exiting")
elif wfile:
    wc=0
    print "starting wordlist attack!"
    stdin=0
    try:
        wlf=open(wfile,'r')
    except IndexError:
        print "No file given using stdin!"
        stdin=1
    except IOError:
        print "No such file using stdin!"
        stdin=1
    if stdin==0:
        word=wlf.readline()
    else:
        word="."
    while word!="":
        wc=wc+1
        if stdin==1:
            try:
                word=sys.stdin.readline()
            except EOFError:
                word=""
        word=word.replace("\n","")
        if not wc%10000:
            print wc,":",word
        check(word,pwhash,rounds,rtype)
        if stdin==0:
            word=wlf.readline()
    print "wordlist attack failed... bruteforcing!"
    while 1:
        for i in charbook:
            print "bruting",pwhash,"(",hname,")","with set ["+i+"] lenght:",end
            for pwstr in brute(i,end):
                check(pwstr,pwhash,rounds,rtype)
        end=end+1
        if end>maxlen:
            exit("maximum password lenght reached... exiting")