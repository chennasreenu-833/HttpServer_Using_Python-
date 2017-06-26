import socket
import sys
try:
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
except socket.error,msg:
    print 'Failed to create socket. Error code:'+str(msg[0])+',Error message:'+msg[1]
    sys.exit()

print 'socket created'

HOST='localhost'
PORT=8888
s.connect((HOST,PORT))
message=raw_input('Please enter ur message')
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