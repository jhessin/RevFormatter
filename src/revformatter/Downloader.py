"""
    This is the Downloader portion of the formatter. It simply downloads the
    REV bible into a binary readable format that we can use to search the
    bible, commentary, and appendix texts.

    Upon creation a file is given (by default REV.dat) and read. It will check
    the date of the file with the date on the server and if the server date is
    later then it will download the REV. Otherwise it will simply return a
    message stating that the REV is ready.

        >>> from RevFormatter.Downloader import Downloader
        >>> d = Downloader('REV.dat')
        >>> d.download()
        Downloading REV - this may take a while...
        >>> d.download()
        REV ready!
        >>> d.ready()
        True
"""

import os


class Downloader:
    def __init__(self, filepath: str = 'REV.dat', auto_flush: bool = True) -> None:
        mode = 'w+b' if not os.path.exists(filepath) else 'r+b'
        self.__file =  open(filepath, mode)
        self.auto_flush = auto_flush


    @property
    def filename(self) -> str:
        return self.__file.name
