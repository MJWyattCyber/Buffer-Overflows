# Buffer-Overflows
Full credit to TheCyberMentor as these scripts feature in his Practical Ethical Hacking course, I've simply split them out and made a seperate script for each step rather than overwriting the script each time.
Some useful files and scripts used to help work through a basic buffer overflow following the process of:

1. Spiking the vulnerable program
2. Fuzzing the command
3. Finding the Offset
4. Overwriting the EIP
5. Finding Bad Characters
6. Finding the right module
7. Generating shellcode and executing the overflow

NOTE: The 'TRUN /.:/' command used within the 's.send' function relate to the program 'VulnServer' it is returned to us within ImmunityDebugger when we first crashed the program.

NOTE #2: Any shellcode will vary from application to application. The shellcode in these scripts works with 'VulnServer' only and will need to be edited for other applications.
