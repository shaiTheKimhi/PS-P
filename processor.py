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


def process(file_name):
    with open(file_name, "a+") as file:
        cont = file.read()
        parts = cont.split("<#")
        # Gets the code
        code = parts[1].split("#>")[0]
        # Executes the code and gets the output
        with stdoutIO() as s:
            exec(code)
        # Prints the new content with code replaced
        cont = cont.replace("<#" + code + "#>", s.getvalue())
        return cont

print(process("example/example.html"))