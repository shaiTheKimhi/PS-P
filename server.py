import time
import BaseHTTPServer
import socket
import json

HOST_NAME = "HP-450"
PORT_NUMBER = 80

class handler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_HEAD(s):
        s.send_response(200)
        s.send_header("Content-type", "text/html")
        s.end_headers()
    def do_GET(s):
        #This is the general handler for GET request
        handle(s)

    def get_parameters(path):
        parts = path.split("/")
        last = parts[len(parts) - 1]
        arguments = last.split("?", 1)
        last = arguments[0]
        parameters = arguments[1]
        parameters = parameters.split("&")
        dict = {}
        for item in parameters:
            parts = item.split("=")
            dict[parts[0]] = parts[1]
        return last, dict

    def handle(s):
        path, params = get_parameters(s.path)
        s.send_response(200)
        s.send_header("Content-type", "text/html")
        s.end_headers()
        s.wfile.write("You enetered path: " + file +" and parameters: " + json.dumps(params))

if __name__ == "__main__":
    server_class = BaseHTTPServer.HTTPServer
    httpd = server_class((HOST_NAME, PORT_NUMBER), handler)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    
