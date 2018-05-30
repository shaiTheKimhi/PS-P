import os

#This function also exists in processor.py
def process_transcrypt(content):
    parts = content.split("<transcrypt")
    cont = ""
    print parts
    for i in range(1, len(parts)):
        inner = parts[i].split("/>")[0]
        #Getting file source
        inner = inner.replace(" ","")
        inner = inner.replace('"',"'")
        source = inner.split("src='")
        for i in source:
            if i != '':
                source = i
        source = source.split("'")[0]
        #Creating JS through transcrypts
        os.system("transcrypt -b -m -n " + source + ".py")
        
        #Removing the unecessary transcrypt tag
        parts[i] = parts[i].replace(inner, "")
        parts[i] = parts[i].replace("/>", "", 1)
        cont += parts[i]
        cont += "<script src='__javascript__/" + source + ".js'>"
    return cont