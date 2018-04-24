import sys
import StringIO
import contextlib

@contextlib.contextmanager
def stdoutIO(stdout=None):
    old = sys.stdout
    if stdout is None:
        stdout = StringIO.StringIO()
    sys.stdout = stdout
    yield stdout
    sys.stdout = old

code = """
print('hello')
"""
with stdoutIO() as s:
    exec(code)

print ("out:"+s.getvalue())

def process(file_name):
    with open(file_name, "a+") as file:
        cont = file.read()
        parts = cont.split("<#")
        code = parts[1].split("#>")[0]
        with stdoutIO() as s:
            exec(code)
        # TODO : add code to source file
        