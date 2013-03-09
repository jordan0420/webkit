#!/usr/bin/env python
class Prompts():
    def __init__(self,answer):
        self.answer = answer
#        print "answer "+ answer

    
    def yes_no(self):
        values = ('y','ye','yes', '')
        if self.answer.lower() in values:
            return True
        else:
            return False
#        print "!"
#        x = True
#        print x
#        return True
#        True if raw_input("%s (y/N) " % msg).lower() == 'y' else False
        
    def yn_choice(message, default='y'):
        choices = 'Y/n' if default.lower() in ('y', 'yes') else 'y/N'
        choice = raw_input("%s (%s) " % (message, choices))
        values = ('y', 'yes', '','ye') if default == 'y' else ('y', 'yes')
        return True if choice.strip().lower() in values else False