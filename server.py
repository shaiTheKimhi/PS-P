import time
import BaseHTTPServer
import socket
import json
import processor

'''import admin
if not admin.isUserAdmin():
    admin.runAsAdmin()'''

HOST_NAME = ""
PORT_NUMBER = 80

class handler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_HEAD(self, s):
        s.send_response(200)
        s.send_header("Content-type", "text/html")
        s.end_headers()
    def do_GET(self):
        #This is the general handler for GET request
        self.handleF(self.path)
        pass
    def do_POST(self):
        #This is the general handler for POST requests
        self.handle(self.path)
        pass

    def get_parameters(self, path):
        parts = path.split("/", 1)
        l = len(parts)
        if(l <= 1):
            return None, None
        last = parts[len(parts) - 1]
        arguments = last.split("?", 1)
        last = arguments[0]
        if(len(arguments) > 1):
            parameters = arguments[1]
            parameters = parameters.split("&")
            dict = {}
            for item in parameters:
                parts = item.split("=")
                dict[parts[0]] = parts[1]
            return last, dict
        else:
            return last, None


    def handleF(self, path):
        path, params = self.get_parameters(path)
        print path
        # Sending response
        self.send_response(200)
        if("html" in path.split(".")[1]):
            st = processor.process(path, params)
            self.send_header("Content-type", "text/html")
        elif("jpg" in path.split(".")[1].lower()):
            with open(path, "rb") as file:
                st = file.read()
            self.send_header("Content-type", "image/jpeg")
        elif("png" in path.split(".")[1].lower()):
            with open(path, "rb") as file:
                st = file.read()
            self.send_header("Content-type", "image/png")
        elif(path == "close" or path == "exit" or path == "stop"):
            raise KeyboardInterrupt()
        else:
            with open(path, "r") as file:
                st = file.read()
        
        
        self.end_headers()
        self.wfile.write(st)
        #self.wfile.write("You enetered path: " + path +" and parameters: " + json.dumps(params))

if __name__ == "__main__":
    server_class = BaseHTTPServer.HTTPServer
    httpd = server_class(('', 8080), handler)
    try:
        print("Server running on: 8080")
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    