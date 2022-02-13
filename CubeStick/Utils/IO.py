from pathlib import Path

class CubeStickIO(object):
    def __init__(self):
        pass

    def current_path_files(self, filter:str="*") -> tuple:
        return (path.name for path in Path('.').glob(filter))

    def out_print(self, args:str) -> None:
        print(args)
        return

