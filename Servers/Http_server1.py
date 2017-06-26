from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer

PORT_NUMBER = 8081

class myHandler (BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.send_header('Connection','closed')
        self.end_headers()
        self.wfile.write("Hello Chenna Welcome!!!")
        return
try:
    server=HTTPServer(('',PORT_NUMBER),myHandler)
    print 'Started httpserver on port',PORT_NUMBER
    server.serve_forever()
except KeyboardInterrupt:
    print '^C received, shutting down the web server'
    server.socket.close()