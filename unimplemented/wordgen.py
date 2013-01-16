###############################################################################
# This is for the word generator
###############################################################################
def wordgen():
    filename = raw_input('Please enter the Filename: ')
    minimum=input('Please enter the minimum length: ')
    maximum=input('Please enter the maximum length: ')
    wmaximum=input('Please enter the max number of words: ')
    input_alphabet = raw_input('please enter the alphabet')
    alphabet = []
    for x in input_alphabet:
        alphabet.append(x)
        #print alphabet
    if wmaximum == 'all':
        string=''
        print 'all'
        FILE = open(str(filename), "w")
        for x in random.sample(alphabet,random.randint(minimum,maximum)):
            string+=x
            FILE.write(string+'\n')

        string=''

    else:
        #alphabet = string.letters[0:52] + string.digits + string.punctuation
        string=''
        FILE = open(str(filename),"w")
        for count in xrange(0,wmaximum):
            for x in random.sample(alphabet,random.randint(minimum,maximum)):
                string+=x
            FILE.write(string+'\n')

        string=''

    FILE.close()
