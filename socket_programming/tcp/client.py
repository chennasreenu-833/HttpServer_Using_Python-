import socket
import sys
try:
	s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
except socket.error,msg:
	print 'Failed to create socket. Error code:'+str(msg[0])+',Error message:'+msg[1]
	sys.exit();
print 'socket created'
host ='localhost'
port =8888
try:
	remote_ip=socket.gethostbyname(host)
except socket.gaierror:
	print 'Hostname could not be resolved. Exiting'
	sys.exit()
print 'Ip address of '+host+' is '+ remote_ip
s.connect((host,port))
print 'Socket Connected to '+ host+' on ip '+ remote_ip
message=raw_input('pls enter any message')
while message:

	try:
		s.sendall(message)
	except socket.error:
		print 'Send failed'
		sys.exit()
	print 'Message sent successfully'

	reply = s.recv(4096)
	print reply
	message=raw_input('pls enter any message')
s.close()
