###############################################################################
# This is for the username creator
###############################################################################

def user_creator():
    name_file = raw_input('File to create list from: ')
    save_file = raw_input('Name to save file as: ')
    savelist = []
    for line in open(name_file):
        name = ''.join([c for c in line if  c == " " or  c.isalpha()])

        tokens = name.lower().split()
        fname = tokens[0]
        lname = tokens[-1]

        savelist.append(fname + lname)             # johndoe            # doejohn
        savelist.append(lname + fname)        
        savelist.append(fname + "." + lname)       # john.doe
        savelist.append(lname + "." + fname)       # doe.john
        savelist.append(fname[0] + lname)          # jdoe
        savelist.append(lname[0] + fname)          # doej
        savelist.append(fname[0] + "." + lname)    # j.doe
        savelist.append(lname[0] + "." + fname)    # d.john

#  This is for the web directories, it can be moved to a new file later
        savelist.append('~'+ fname + lname)             # ~johndoe
        savelist.append('~'+ lname + fname)             # ~doejohn
        savelist.append('~'+ fname + "." + lname)       # ~john.doe
        savelist.append('~'+ lname + "." + fname)       # ~doe.john
        savelist.append('~'+ fname[0] + lname)          # ~jdoe
        savelist.append('~'+ lname[0] + fname)          # ~doej
        savelist.append('~'+ fname[0] + "." + lname)    # ~j.doe
        savelist.append('~'+ lname[0] + "." + fname)    # ~d.john
    for name in savelist:
        save_file.write(name + '\n')
    save_file.close()

