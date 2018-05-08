from appJar import gui
from threading import Thread
import server

def start(btn):
    port = app.getEntry("port")
    if(port == None):
        port = 8080
    server.PORT_NUMBER = int(port)
    thread = Thread(target=server.run_server)
    thread.start()
    new_app(port)
    
def new_app(port):
    logo = gui("PSAP")
    logo.addLabel("l1","Server Running on: " + port)
    logo.go()

app = gui("PSAP")
app.addButton("start", start)
app.addEntry("port")
app.setEntryDefault("port","Enter Port Number Here")
app.go()