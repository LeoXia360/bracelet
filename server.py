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

fan = 0
vinyl = 0 
lamp = 0 
disco = 0


class S(BaseHTTPRequestHandler):
    protocol_version = "HTTP/1.1"
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.send_header('Content-length', 1)
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        self.wfile.write("<html><body><h1>hi!</h1></body></html>")

    def do_HEAD(self):
        self._set_headers()
        
    def do_POST(self):
        global fan
        global vinyl
        global lamp
        global disco 
        # Doesn't do anything with posted data
        content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
        post_data = self.rfile.read(content_length) # <--- Gets the data itself
        if (post_data == "hue"):
            print "hue pressed"    
        elif (post_data == "5"):
            headers = {'Content-Type': 'application/json'}
            if (fan == 0): 
                print "fan 0"
                data = '{"method":"passthrough", "params": {"deviceId": "800655B6B068CE49D0B446E32F86F56C19311152", "requestData": "{\\"system\\":{\\"set_relay_state\\":{\\"state\\":1}}}" }}'
                fan = 1
            else: 
                print "fan 1"
                fan = 0
                data = '{"method":"passthrough", "params": {"deviceId": "800655B6B068CE49D0B446E32F86F56C19311152", "requestData": "{\\"system\\":{\\"set_relay_state\\":{\\"state\\":0}}}" }}'
            requests.post('https://use1-wap.tplinkcloud.com/?token=03546e31-A7XmhafFphGZ2NCjAYmzy1v', headers=headers, data=data)
        elif( post_data == "4"): 
            headers = {'Content-Type': 'application/json'}
            if (vinyl == 0): 
                print "vinyl 0"
                data = '{"method":"passthrough", "params": {"deviceId": "80062719800D1D795128282B0F90B1C319627F43", "requestData": "{\\"system\\":{\\"set_relay_state\\":{\\"state\\":1}}}" }}'
                vinyl = 1
            else: 
                print "vinyl 1"
                vinyl = 0
                data = '{"method":"passthrough", "params": {"deviceId": "80062719800D1D795128282B0F90B1C319627F43", "requestData": "{\\"system\\":{\\"set_relay_state\\":{\\"state\\":0}}}" }}'
            requests.post('https://use1-wap.tplinkcloud.com/?token=03546e31-A7XmhafFphGZ2NCjAYmzy1v', headers=headers, data=data)
        elif(post_data == "3"): 
            headers = {'Content-Type': 'application/json'}
            if (disco == 0): 
                print "disco 0"
                data = '{"method":"passthrough", "params": {"deviceId": "80069EE14C503E31F28413E5453C53231962507E", "requestData": "{\\"system\\":{\\"set_relay_state\\":{\\"state\\":1}}}" }}'
                disco = 1
            else: 
                print "disco 1"
                disco = 0
                data = '{"method":"passthrough", "params": {"deviceId": "80069EE14C503E31F28413E5453C53231962507E", "requestData": "{\\"system\\":{\\"set_relay_state\\":{\\"state\\":0}}}" }}'
            requests.post('https://use1-wap.tplinkcloud.com/?token=03546e31-A7XmhafFphGZ2NCjAYmzy1v', headers=headers, data=data)
        elif(post_data == "0"): # on 
            headers = {'Content-Type': 'application/json'}
            if(disco==0): 
                data = '{"method":"passthrough", "params": {"deviceId": "80069EE14C503E31F28413E5453C53231962507E", "requestData": "{\\"system\\":{\\"set_relay_state\\":{\\"state\\":1}}}" }}'
                requests.post('https://use1-wap.tplinkcloud.com/?token=03546e31-A7XmhafFphGZ2NCjAYmzy1v', headers=headers, data=data)
                disco = 1
            if(vinyl==0): 
                data = '{"method":"passthrough", "params": {"deviceId": "80062719800D1D795128282B0F90B1C319627F43", "requestData": "{\\"system\\":{\\"set_relay_state\\":{\\"state\\":1}}}" }}'
                requests.post('https://use1-wap.tplinkcloud.com/?token=03546e31-A7XmhafFphGZ2NCjAYmzy1v', headers=headers, data=data)
                vinyl = 1
            if(fan == 0 ): 
                data = '{"method":"passthrough", "params": {"deviceId": "800655B6B068CE49D0B446E32F86F56C19311152", "requestData": "{\\"system\\":{\\"set_relay_state\\":{\\"state\\":1}}}" }}'
                requests.post('https://use1-wap.tplinkcloud.com/?token=03546e31-A7XmhafFphGZ2NCjAYmzy1v', headers=headers, data=data)
                fan = 1
            if(lamp == 0): 
                lamp = 1
        elif(post_data == "1"):  #off
            headers = {'Content-Type': 'application/json'}
            if(disco==1): 
                data = '{"method":"passthrough", "params": {"deviceId": "80069EE14C503E31F28413E5453C53231962507E", "requestData": "{\\"system\\":{\\"set_relay_state\\":{\\"state\\":0}}}" }}'
                requests.post('https://use1-wap.tplinkcloud.com/?token=03546e31-A7XmhafFphGZ2NCjAYmzy1v', headers=headers, data=data)
                disco = 0
            if(vinyl==1): 
                data = '{"method":"passthrough", "params": {"deviceId": "80062719800D1D795128282B0F90B1C319627F43", "requestData": "{\\"system\\":{\\"set_relay_state\\":{\\"state\\":0}}}" }}'
                requests.post('https://use1-wap.tplinkcloud.com/?token=03546e31-A7XmhafFphGZ2NCjAYmzy1v', headers=headers, data=data)
                vinyl = 0
            if(fan == 1 ): 
                data = '{"method":"passthrough", "params": {"deviceId": "800655B6B068CE49D0B446E32F86F56C19311152", "requestData": "{\\"system\\":{\\"set_relay_state\\":{\\"state\\":0}}}" }}'
                requests.post('https://use1-wap.tplinkcloud.com/?token=03546e31-A7XmhafFphGZ2NCjAYmzy1v', headers=headers, data=data)
                fan = 0
            if(lamp == 1): 
                lamp = 0
        elif(post_data == "random"): 
            lamp = 1
        elif(post_data == "study"): 
            lamp = 1
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
