'''
Created on Mar 17, 2018

@author: SYSTEM
'''

#if __name__ == '__main__':  pass

import socket
import sys

#Retrieving data from user_________________________________________________________________________________________________
if(len(sys.argv)-1 !=2):
        print "Incorrect number of arguments. (", len(sys.argv)-1, ")"
        print "Enter: port number"
        sys.exit()
TCP_PORT_NO = sys.argv[1]
TCP_PORT_NO_int = int(TCP_PORT_NO)
OUTPUT_FILE = sys.argv[2]
print "You entered: ", TCP_PORT_NO_int, OUTPUT_FILE


#Retrieving Server IP Address_______________________________________________________________________________________________
S = socket.socket()
TCP_HOST_NAME = socket.gethostname()
SERVER_IP_ADDRESS = socket.gethostbyname(TCP_HOST_NAME)
#SERVER_IP_ADDRESS = '127.0.0.1'

    
    
#Receiving data from Client_________________________________________________________________________________________________
BUFFER_SIZE = 1024  
ALL_DATA =""

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((SERVER_IP_ADDRESS, TCP_PORT_NO_int))
while True:
    s.listen(2)
    
    conn, addr = s.accept()
    print 'Connection address:', addr
    while 1:
         data = conn.recv(BUFFER_SIZE)
         if not data: break
         print >>sys.stderr, 'received %s bytes from %s' % (len(data), addr)
         print "received data:", data
         print "_________________________________"
         ALL_DATA = ALL_DATA + data
print "ALL_DATA:", ALL_DATA

FILE = open(OUTPUT_FILE, 'w')    
FILE.write(ALL_DATA)
conn.close()
