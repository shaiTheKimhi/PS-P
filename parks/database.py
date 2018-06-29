import json
import time

'''
def sign_park(client, park_id = 0):
    with open("parks.json" ,"a+") as file:
        data = json.loads(file.read())
        if (data == None):
            data = {}
        if(park_id in data.keys()):
            data[park_id].append(client)
        else:
            data[park_id] = [client]
        file.write(json.dumps(data))

def check_park(client, park_id):
    with open("parks.json", "r") as file:
        data = json.loads(file.read())
        if(data == None):
            return False
        for park in data.keys():
            if(park == park_id):
                return client in data
'''

def get_table_json(table):
    with open(table + ".json", "r+") as file:
        return file.read()

def sign_park(client, buy_time):
    with open("parks.json", "w+") as file:
        data = json.loads(file.read())
        if(data == None):
            data = {}
        if(client in data.keys()):
            if(data[client] < time.time()):
                data[client] = time.time() + buy_time
            else:
                data[client] += buy_time
        else:
            data[client] = time.time() + buy_time
        file.write(json.dumps(data))

def check_park(client):
    with open("parks.json" ,"r") as file:
        data = json.loads(file.read())
        if(client in data.keys()):
            return data[client] < time.time(), time.time() - data[client] 
        else:
            return False, None

def add_report(client, money, desc):
    file = open("reports.json", "r")
    cont = file.read()
    file.close()
    if(cont == ''):
        cont = '{}'
    data = json.loads(cont)
    if(client in data.keys()):
        data[client].appned({"report size": money, "description" : desc})
    else:
        data[client] = [{"report size": money, "description" : desc}]
    file =  open("reports.json", "w+")
    file.write(json.dumps(data))
    file.close()