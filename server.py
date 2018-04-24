#!/usr/bin/env python
"""
Very simple HTTP server in python.
Usage::
    ./dummy-web-server.py [<port>]
Send a GET request::
    curl http://localhost
Send a HEAD request::
    curl -I http://localhost
Send a POST request::
    curl -d "foo=bar&bin=baz" http://localhost


"""

import requests
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import SocketServer

import socket   

switch = 0


class S(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        self.wfile.write("<html><body><h1>hi!</h1></body></html>")

    def do_HEAD(self):
        self._set_headers()
        
    def do_POST(self):
        global switch
        # Doesn't do anything with posted data
        content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
        post_data = self.rfile.read(content_length) # <--- Gets the data itself
        if (post_data == "hue"):
            print "hue pressed"
        elif (post_data == "tp"):
            headers = {'Content-Type': 'application/json'}
            if (switch == 0): 
                print "switch 0"
                data = '{"method":"passthrough", "params": {"deviceId": "800655B6B068CE49D0B446E32F86F56C19311152", "requestData": "{\\"system\\":{\\"set_relay_state\\":{\\"state\\":1}}}" }}'
                switch = 1
            else: 
                print "switch 1"
                switch = 0
                data = '{"method":"passthrough", "params": {"deviceId": "800655B6B068CE49D0B446E32F86F56C19311152", "requestData": "{\\"system\\":{\\"set_relay_state\\":{\\"state\\":0}}}" }}'
            requests.post('https://use1-wap.tplinkcloud.com/?token=03546e31-A7XmhafFphGZ2NCjAYmzy1v', headers=headers, data=data)
        else:
            print post_data
        self._set_headers()
        self.wfile.write("<html><body><h1>POST!</h1></body></html>")
        
def run(server_class=HTTPServer, handler_class=S, port=8080):
    hostname = socket.gethostname()   
    IPAddr = socket.gethostbyname(hostname)   
    print("Your Computer Name is:" + hostname)   
    print("Your Computer IP Address is:" + IPAddr)
    server_address = ("localhost", port)
    httpd = server_class(server_address, handler_class)
    print server_address
    print port
    print 'Starting httpd...'
    httpd.serve_forever()

if __name__ == "__main__":
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()