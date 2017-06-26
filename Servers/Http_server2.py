from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
from os import curdir,sep
import socket
import cgi

PORT_NUMBER=8081

class myHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print self.path
        #if self.path=="/my_html":
         #   self.path="/my_html/svuce_mine.html"
        try:
            sendReply=False
            if self.path.endswith(".html"):
                mimetype='text/html'
                sendReply=True
            if self.path.endswith(".jpg"):
                mimetype='image/jpg'
                sendReply=True
            if self.path.endswith(".gif"):
                mimetype='image/gif'
                sendReply=True
            if self.path.endswith(".png"):
                mimetype='image/png'
                sendReply=True
            if self.path.endswith(".js"):
                mimetype = 'application/javascript'
                sendReply = True
            if self.path.endswith(".css"):
                mimetype = 'text/css'
                sendReply = True

            if sendReply==True:
                f=open(curdir+sep+self.path)
                self.send_response(200)
                self.send_header('Content-Type',mimetype)
                self.end_headers()
                self.wfile.write(f.read())
                f.close()
            return
        except IOError:
            self.send_error(404,"file Not Found:%s"%self.path)
            # Handler for the POST requests

    def do_POST(self):
        #if self.path == "/send":
            form = cgi.FieldStorage(fp=self.rfile,headers=self.headers,environ={'REQUEST_METHOD': 'POST','CONTENT_TYPE': self.headers['Content-Type'],})

            print "Your name is: %s" % form["your_name"].value
            self.send_response(200)
            self.end_headers()
            self.wfile.write("Thanks %s !" % form["your_name"].value)
            return


try:
    server=HTTPServer(('',PORT_NUMBER),myHandler)
    print 'Started httpserver on port',PORT_NUMBER
    server.serve_forever()
except KeyboardInterrupt:
    print '^C received ,shutting down the web server'
    server.socket.close()