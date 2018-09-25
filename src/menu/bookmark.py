from PyQt5.QtWidgets import QAction


class Bookmark:
    def __init__(self, master):
        self.FILE = {
            'new': QAction("&New File", master),
            'sep1': self.__get_separator(master),
            'save': QAction("&Save", master),
            'save_as': QAction("Save &As...", master),
            'sep2': self.__get_separator(master),
            'open': QAction("&Open File...", master),
            'sep3': self.__get_separator(master),
            'exit': QAction("&Exit", master),
        }
        self.EDIT = {
            'soon': QAction("&Soon", master),
        }
        self.VIEW = {
            'soon': QAction("&Soon", master),
        }
        self.PREFERENCES = {
            'soon': QAction("&Soon", master),
        }
        self.HELP = {
            'About': QAction("&About", master),
        }

    def __get_separator(self, master):
        separator = QAction(master)
        separator.setSeparator(True)
        return separator
