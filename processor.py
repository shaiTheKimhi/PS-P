import sys
import io
import contextlib
import os
import server
import json

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
        stdout = io.StringIO.StringIO()
    sys.stdout = stdout
    yield stdout
    sys.stdout = old


def process(file_name, parameters, request):
    parts = (server.SOURCE.split("\\")[-1] + file_name).split("\\")
    path = ""
    for i in parts[:-1]:
        path += i
        path += "\\"
    origin = os.getcwd()
    print("enter directory:" + json.dumps(parts))
    if(path != ""):
        os.chdir(path)
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
        os.chdir(origin)
        return cont


#(process("example/example.html"))

