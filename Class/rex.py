class Newtorkerror(RuntimeError):
    def __init__(self,arg):
        self.args=arg

try:
    raise Newtorkerror("Bad Hostname")
except Newtorkerror as e:
    print(e.args)