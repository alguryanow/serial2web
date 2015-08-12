# -*- coding: utf-8 -*-

#-- based on: https://raw.githubusercontent.com/Jonty/RemoteSensors/master/remoteSensors.py

SERIAL_PORT_NAME = 'COM7'
SERIAL_PORT_SPEED = 115200

WEB_SERVER_PORT = 8000

import time, BaseHTTPServer, urlparse
import serial

ser = None

def main():

    global ser
    
    httpd = BaseHTTPServer.HTTPServer(("", WEB_SERVER_PORT), Handler)

    #-- workaround for getting IP address at which serving
    import socket
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('google.co.uk', 80))
    sData = s.getsockname()

    print "Serving at '%s:%s'" % (sData[0], WEB_SERVER_PORT)
    
    ser = serial.Serial(SERIAL_PORT_NAME, SERIAL_PORT_SPEED, timeout=0.02)

    
    httpd.serve_forever()

    
class Handler(BaseHTTPServer.BaseHTTPRequestHandler):

    # Disable logging DNS lookups
    def address_string(self):
        return str(self.client_address[0])

    def do_GET(self):

        # url = urlparse.urlparse(self.path)
        
        if self.path == '/' or self.path == '/index.html':
            self.process_index()
        elif self.path == '/get_serial':
            self.process_get_serial()
        else:
            self.process_unknown()
        

    def process_index(self):            
    
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()

        # f = open('index.html')
        # lines = f.readlines();

        # answer = ''.join(lines)

        # self.wfile.write(answer)
        self.wfile.write(open('index.html').read())
        self.wfile.write("\n\n")
        self.wfile.flush()

        
    def process_get_serial(self):

        self.send_response(200)
        self.send_header("Content-type", "text/event-stream")
        self.end_headers()

        try:
            while True:
                
                new_serial_line = get_full_line_from_serial()
                if new_serial_line is not None:
                
                    self.wfile.write('data: ' + new_serial_line)
                    self.wfile.write("\n\n")
                    self.wfile.flush()


        except socket.error, e:
            print "Client disconnected.\n"


    def process_unknown(self):
        self.send_response(404)
        
            

captured = ''
def get_full_line_from_serial():
    """ returns full line from serial or None 
        Uses global variables 'ser' and 'captured'
    """
    global captured
    part = ser.readline()
    if part:
        captured += part
        parts = captured.split('\n', 1);
        if len(parts) == 2:
            captured = parts[1]
            return parts[0]
            
    return None
    
    
if __name__ == '__main__':
    main()