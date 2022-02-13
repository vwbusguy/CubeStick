import platform

class CubeStickOS(object):
    """Operating System level info and calls.
    """

    def __init__(self):
        """Contructor
        """
        pass

    def get_OS_info(self) -> str:
        """Return OS info like [OS][Arch]
        """
        return "[{0}][{1}]".format(platform.system().upper(),platform.machine().upper())
