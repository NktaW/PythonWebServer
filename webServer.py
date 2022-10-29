#Import the HTTP Server Module.

#BaseHTTPRequestHandler is gonna handle all the get request & post request what the server recives
#The HTTPServer and ThreadingHTTPServer must be given a RequestHandlerClass on instantiation, of which this module provides three different variants.
from http.server import HTTPServer, BaseHTTPRequestHandler

#Creating helloHandler class witch will used to handle all the get request the server recives
class echoHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('content-type', 'text/html')
        self.end_headers()
        self.wfile.write(self.path[1:].encode()) #The encode() method encodes the string, using the specified encoding.
#Send respond with status quote 200
#The HTTP 200 OK success status response code indicates that the request has succeeded.

def main():
    PORT = 8000
    server = HTTPServer(('', PORT), echoHandler)
    print('Server running on port %s' % PORT)
    server.serve_forever() #Will run the server forever until you stop it from the terminal with cntl + c command.

if __name__ == '__main__':
    main()