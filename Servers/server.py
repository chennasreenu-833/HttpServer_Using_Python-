import socket
import sys
from thread import *
from os import curdir,sep

HOST='localhost'
PORT=8888
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print 'Socket Created'

try:
	s.bind((HOST,PORT))
except socket.error,msg:
	print 'Bind failed. Error Code :' +str(msg[0])+'Message '+msg[1]
	sys.exit()


print 'Socket bind complete'
s.listen(10)


print 'Socket now listening'

def clientthread(conn):
   ## conn.send('Welcome to the server. Type something and hit enter\n')

    while True:
        data=conn.recv(4096)
        print data
        conn.send('HTTP/1.1 200 OK')
        conn.send('Content-Type:text/html')
        conn.send('\n')
        f = open(curdir + sep +'index_example2.html')
        conn.send(f.read())
        conn.close
        reply='OK...'+data

	break
        ##if not data:
          ##  break
        ##conn.sendall(reply)

while 1:
    conn,addr=s.accept()
    print 'connected with '+addr[0]+':'+str(addr[1])
    start_new_thread(clientthread,(conn,))
s.close()
