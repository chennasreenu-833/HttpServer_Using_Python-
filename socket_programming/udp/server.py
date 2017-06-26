import socket
import sys

HOST='localhost'
PORT=8888
try:
	s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
	print 'Socket created'
except socket.error,msg:
	print 'Failed to create socket. Error Code:'+str(msg[0])+'Message '+msg[1]
	sys.exit()
print 'Socket bind complete'
while 1:
	d=s.recvfrom(1024)
	data=d[0]
	addr=d[1]
	if not data:
		break
	reply ='Ok... '+data
	s.sendto(reply,addr)
	print 'Message['+addr[0]+':'+str(addr[1])+']-'+data.strip()
s.close()
