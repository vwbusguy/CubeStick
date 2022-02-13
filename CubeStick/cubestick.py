from Utils.IO import *
from Utils.OS import *

import sys

class CubeStickSession(object):
    """Handles current session data and input.
    """

    def __init__(self):
        """Constructor method.  Initializes session data.
        """
        self._data = {}
        self._router = CubeStickRouter()

    def handle_input(self, user_in:str):
        """Parse user input and hand off to :class:`CubeStickRouter`.

        :param user_in: String from user input
        :type user_in: string
        :return: Routes output of eventual handler.  Likely None.
        """
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
        """Print welcome message in CLI mode.
        """
        print("Welcome to the CubeStick tester.")

class CubeStickRouter(object):
    """Class to route inputs to their proper internal handlers.
    """
    def __init__(self):
        """Constructor.  Instantiate potential route paths
        """
        self._IO = CubeStickIO()
        self._OS = CubeStickOS()

    def route(self, keyword:str, args:str=""):
        """Route arguments to handler based on keyword.

        :param keyword: BASIC function as PRINT
        :type keyword: string
        :param args: Any arguments passed to the keyword
        :type args: string, optional
        """
        keyword = keyword.upper()
        match keyword:
            case 'PRINT' : 
                return self._IO.out_print(args) 
            case '_OS$()':
                os_info = self._OS.get_OS_info()
                print(os_info)
                return os_info
            case 'FILES':
                if args.strip() == "": args = "*"
                files = self._IO.current_path_files(args)
                print('\n'.join(files))
                return
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
