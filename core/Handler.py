import os
class Handler:
#    def __init__(self, output):
#        self.output = output
    def __init__(self):
        print "Handler"
    def printer(self):
        print self.output 
    def second_printer(self, arg):
        print arg
    def help(self):
        print "\t \t \t Help Options"
        print "\t \t " + "="*30
        print "\n Command \t\t Descriptions"
        print " ------- \t\t ------------"
        print "show modules \t\t shows all the modules available"
        print "use [module] \t\t use the selected module"
        print "show options \t\t shows the options for the selected modules"
        print "set <option> [option] \t\t sets the selected option"
    def show_modules(self):
        print 'show modules'
    def use_module(self):
        print 'use module'
    def show_options(self):
        print "Show_options"
    def set_option(self):
        print 'set option'
    def set_options_multi(self):
        print 'Set options Multi'
    def change_workspace(self):
        print "change workspace"
    