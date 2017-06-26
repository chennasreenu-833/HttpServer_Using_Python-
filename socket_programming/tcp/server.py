import socket
import sys
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
while True:

	conn,addr=s.accept()
	print 'connected with '+addr[0]+':'+str(addr[1])
	data=conn.recv(1024)
	print data
	conn.sendall(data)
conn.close()
s.close()
