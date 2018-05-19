from appJar import gui
from threading import Thread
import server

def start(btn):
    port = app.getEntry("port")
    if(port == ''):
        port = "8080"
    server.PORT_NUMBER = int(port)
    thread = Thread(target=server.run_server)
    thread.start()
    app.stop()
    new_app(port)
    
def stop_server(btn):
    raise KeyboardInterrupt()
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
app.go()