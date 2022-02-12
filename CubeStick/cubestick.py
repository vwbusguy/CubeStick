import sys

class CubeStickSession(object):
    def __init__(self):
        self._data = {}
        self._router = CubeStickRouter()

    def handle_input(self,user_in):
        user_in = user_in.strip()
        if user_in == "": return
        if " " not in user_in:
            keyword = user_in
            args = ""
        else:
            keyword, args = user_in.split(" ",1)
        return self._router.route(keyword, args)

class CubeStickRouter(object):
    def __init__(self):
        self._IO = CubeStickIO()

    def route(self, keyword, args):
        keyword = keyword.upper()
        match keyword:
            case 'PRINT' : 
                return self._IO.out_print(args) 
            case _:
                # Throw catchable error
                print("We don't have a handler for that yet.")

class CubeStickIO(object):
    def __init__(self):
        pass

    def out_print(self,args):
        print(args)

if __name__ == 'cubestick':
    print("Welcome to the CubeStick tester.")
    session = CubeStickSession()
    while True:
        print("] ", end='')
        cli_inp = input()
        if cli_inp.upper() in ('SYSTEM','EXIT'): sys.exit(0)
        session.handle_input(cli_inp)
