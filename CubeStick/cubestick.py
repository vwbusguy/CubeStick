from Utils.IO import *

import sys

class CubeStickSession(object):
    def __init__(self):
        self._data = {}
        self._router = CubeStickRouter()

    def handle_input(self, user_in:str):
        user_in = user_in.strip()
        if "'" in user_in: user_in = user_in.split("'",1)[0]
        if user_in == "": return
        if " " not in user_in:
            keyword = user_in
            args = ""
        else:
            keyword, args = user_in.split(" ",1)
        return self._router.route(keyword, args)

    def welcome(self) -> None:
        print("Welcome to the CubeStick tester.")

class CubeStickRouter(object):
    def __init__(self):
        self._IO = CubeStickIO()

    def route(self, keyword:str, args:str):
        keyword = keyword.upper()
        match keyword:
            case 'PRINT' : 
                return self._IO.out_print(args) 
            case _:
                # Replace catchable error
                print("We don't have a handler for that yet.")
                return
        return

if __name__ == 'cubestick':
    session = CubeStickSession()
    session.welcome()
    while True:
        print("] ", end='')
        cli_inp = input()
        if cli_inp.upper() in ('SYSTEM','EXIT'): sys.exit(0)
        session.handle_input(cli_inp)
