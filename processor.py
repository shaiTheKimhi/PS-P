import sys
import StringIO
import contextlib
import os
import server
import json
import process

def get_indention(string):
    parts = string.split("\n")
    line = parts[len(parts) - 1]
    return len(line)

def remove_indent(code, indent):
    lines = code.split("\n")
    for i in range(len(lines)):
        lines[i] = lines[i][indent:]
    code = ""
    for line in lines:
        code += line
        code += "\n"
    return code

@contextlib.contextmanager
def stdoutIO(stdout=None):
    old = sys.stdout
    if stdout is None:
        stdout = StringIO.StringIO()
    sys.stdout = stdout
    yield stdout
    sys.stdout = old


def process(file_name, parameters, request):
    parts, path, origin = move_to(file_name)
    with open(parts[-1], "a+") as file:
        cont = file.read()
        parts = cont.split("<#")
        # Gets the tag indent
        indent = get_indention(parts[0])
        for i in range(1, len(parts), 1):
            # Gets the code
            code = parts[i].split("#>")[0]
            # Removes the indent
            new_code = remove_indent(code, indent)
            # Executes the code and gets the output
            with stdoutIO() as s:
                exec(new_code)
            # Prints the new content with code replaced
            cont = cont.replace("<#" + code + "#>", s.getvalue())
        cont = process_transcrypt(cont)
        os.chdir(origin)
        return cont


def process_transcrypt(content):
    parts = content.split("<transcrypt")
    cont = ""
    for i in range(1, len(parts)):
        inner = parts[i].split("/>")[0]
        #Getting file source
        inner = inner.replace(" ","")
        inner = inner.replace('"',"'")
        source = inner.split("src='")
        for item in source:
            if item != '':
                source = item
        source = source.split("'")[0]
        #Creating JS through transcrypts
        os.system("transcrypt -b -m -n " + source + ".py")
        
        #Removing the unecessary transcrypt tag
        parts[i] = parts[i].replace(inner, "")
        parts[i] = parts[i].replace("/>", "", 1)
        cont += "<script src='__javascript__/" + source + ".js'></script>"
        cont += parts[i]
    return cont

def move_to(file_name):
    #parts = (server.SOURCE.split("\\")[-1] + file_name).split("\\")
    parts = file_name.split("/")
    path = ""
    for i in parts[:-1]:
        path += i
        path += "\\"
    origin = os.getcwd()
    print("enter directory:" + path)
    if(path != ""):
        os.chdir(path)
    #REMOVE !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    print os.getcwd()
    print os.listdir(os.getcwd())
    return parts, path, origin