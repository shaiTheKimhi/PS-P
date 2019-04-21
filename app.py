from threading import Thread
from time import sleep
import server
import os
import sys

try:
    from appJar import gui
except:
    os.system("pip install appJar")
    sleep(1)
    from appJar import gui
    

def start(btn):
    port = app.getEntry("port")
    if(port == ''):
        port = "8080"
    source = app.getEntry("source")
    if("C:\\" not in source):
        source = os.getcwd() + '\\' + source
    source += "\\"
    server.PORT_NUMBER = int(port)
    server.SOURCE = source
    thread = Thread(target=server.run_server)
    thread.start()
    app.stop()
    new_app(port)
    
def stop_server(btn):
    sys.exit()
#TODO : Add Image for Logo on app background
def new_app(port):
    logo = gui("PSAP")
    logo.addLabel("l1","Server Running on: " + port)
    logo.addButton("Stop Server", stop_server)
    logo.go()

app = gui("PSAP")
app.addButton("Start", start)
app.addEntry("port")
app.setEntryDefault("port","Enter Port Number Here")
app.addEntry("source")
app.setEntryDefault("source", "Enter Source Path")
app.go()
