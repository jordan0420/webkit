#!/usr/bin/env python
#class Interface():
#    def __init__():
#        pass
import Colors
import Handler
#class sample():
#    def __init__(self, output):
#        self.output = output
#    def printer(self):
#        print self.output 
#    def second_printer(self, arg):
#        print arg
#Color = Colors
Color = Colors.Color()
Handler = Handler.Handler()
Color.GREEN()
x = True
# Processes user input
# Sends the input to the backend of the interface
# Should be in a class

while x == True:
#    def show_modules(self):
#        print 'show modules'
#    def use_module(self):
#        print 'use module'
#    def show_options(self):
#        print "Show_options"
#    def set_option(self):
#        print 'set option'
#    def set_option_multi(self):
#        print 'Set options Multi'
    #Handler = Handler.Handler()
    input = raw_input('Input: ')
    input = input.lower()
    if input.split(' ')[0] == 'help':
        if input.split(' ')[1]:
            arg.input.split(' ')[1]
            Handler.help(arg)
        else:
            Handler.help()
    if input.split(' ')[0] == 'show' and input.split(' ')[1] == 'modules':
        if input.split(' ')[2]:
            print 'arguement given: ' + input.split(' ')[2]
            arg = input.split(' ')[2]
            Handler.show_modules(arg)
        else:
            print 'show modules'
            Handler.show_modules()
    if input.split(' ')[0] == 'use' and input.split(' ')[1] == 'module':
        if input.split(' ')[2]:
            arg = input.split(' ')[2]
            Handler.use_module(arg)
        else:
            print "Not enough arguments given"
#        print 'use module'
#        Handler.use_module()
    if input.split(' ')[0] == 'show' and input.split(' ')[1] == 'options':
        print 'show options'
        Handler.show_options()
    if input.split(' ')[0] == 'set' and input.split(' ')[1] == 'options':
        if input.split(' ')[2]:
            if input.split(' ')[3]:
                arg_1 = input.split(' ')[2]
                arg_2 = input.split(' ')[3]
                Handler.set_uption(arg_1, arg_2)
            else:
                print 'No options set'
        else:
            print "No arguements given"
        print 'set options'
        Handler.set_option()
    if input.split(' ')[0] == 'set' and input.split(' ')[1] == 'multi':
        print 'set multi'
        Handler.set_options_multi()
    if input.split(' ')[0] == 'change' and input.split(' ')[1] == 'workspace':
        if input.split(' ')[2]:
            arg = input.split(' ')[2]
            Handler.change_workspace(arg)
        else:
             Handler.change_workspace()
    if input.split(' ')[0] == 'quit':
        print 'quit'
        x = False
    if input.split(' ')[0] == 'printer':
        Handler.second_printer('awesome its fucking working')
        print 'printer'
# there are two ends of the interface, the front end and the back end
# the front end just passes arguements to the backend
# the backend will take the arguments and then return the result
# it will be a cake like structure
# the backend will also handle the XML structure

 