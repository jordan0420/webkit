#!/usr/bin/env python

class Color:
	PURPLE = '\033[95m'
	CYAN = '\033[96m'
	DARKCYAN = '\033[36m'
	BLUE = '\033[94m'
	GREEN = '\033[92m'
	YELLOW = '\033[93m'
	RED = '\033[91m'
	BOLD = '\033[1m'
	UNDERL = '\033[4m'
	ENDC = '\033[0m'
	backBlack = '\033[40m'
	backRed = '\033[41m'
	backGreen = '\033[42m'
	backYellow = '\033[43m'
	backBlue = '\033[44m'
	backMagenta = '\033[45m'
	backCyan = '\033[46m'
	backWhite = '\033[47m'
	def RED(self):
		print '\033[91m'
	def PURPLE(self):
		print '\033[95m'
	def CYAN(self):
		print '\033[96m'
	def DARKCYAN(self):
		print '\03336m'
	def BLUE(self):
		print '\033[94m'
	def GREEN(self):
		print'\033[92m'
	def YELLOW(self):
		print '\033[94m'
	def BOLD(self):
		print '\033[94m'
	def UNDERLINE(self):
		print '\033[4m'
	def ENDC(self):
		print '\033[0m'
	def backBlack(self):
		print '\033[40m'
		
