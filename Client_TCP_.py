'''
Created on Mar 17, 2018

@author: SYSTEM
'''

#if __name__ == '__main__':
#    pass
import sys
import socket
import os

#Retrieving data from user______________________________________________________________
if(len(sys.argv)-1 !=3):
    print "Incorrect number of arguments.(", len(sys.argv)-1, ")"
    print "Enter: Servers IP address, port number, input file name"
    sys.exit()
    
SERVER_IP_ADDRESS = sys.argv[1]
TCP_PORT_NO = sys.argv[2]
TCP_PORT_NO_int = int(TCP_PORT_NO)
INPUT_FILE = sys.argv[3]

print "You entered: ", SERVER_IP_ADDRESS, TCP_PORT_NO_int,INPUT_FILE
    
#Retrieving Client IP Address_____________________________________________________________________________________
S = socket.socket()
TCP_HOST_NAME =socket.gethostname()
CLIENT_IP_ADDRESS=socket.gethostbyname(TCP_HOST_NAME)
#print ("Your Computer Name is: " + TCP_HOST_NAME)
#print ("Your Computer IP Address is: " +CLIENT_IP_ADDRESS)


#Reading in 1024 bytes at a time from the file and sending to Server______________________________________________________________________________
i=0
FILE = open(INPUT_FILE, 'rb')
FILE_INFO = os.stat(INPUT_FILE)
FILE_SIZE = FILE_INFO.st_size
print "The size of the file is: ", FILE_SIZE

#MESSAGE = "Hello, World!"
  
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((SERVER_IP_ADDRESS, TCP_PORT_NO_int))

BYTE_CHUNKS = 1024

NO_OF_CHUNKS = FILE_SIZE/BYTE_CHUNKS
REMAINDER = FILE_SIZE%BYTE_CHUNKS

while FILE:
    READ_FILE = FILE.read(BYTE_CHUNKS)
    s.send(READ_FILE)
    i=i+1
    print READ_FILE
    if i == NO_OF_CHUNKS:
        READ_FILE = FILE.read(REMAINDER)
        s.send(READ_FILE)
        #print "READ_FILE:",READ_FILE
        DATABACK = s.recv(BYTE_CHUNKS)
        print DATABACK
        s.close()
        break
    
