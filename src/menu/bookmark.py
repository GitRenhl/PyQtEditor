from PyQt5.QtWidgets import QAction


class Bookmark:
    def __init__(self, master):
        self.FILE = {
            'new': QAction("&New File", master),
            'sep1': self.__get_separator(master),
            'save': QAction("&Save", master),
            'save_as': QAction("Save &As...", master),
            'sep2': self.__get_separator(master),
            'open_file': QAction("&Open File...", master),
            'sep3': self.__get_separator(master),
            'close_tab': QAction("Close window", master),
            'sep4': self.__get_separator(master),
            'exit': QAction("&Exit", master),
        }
        self.EDIT = {
            'undo': QAction("&Undo", master),
            'redo': QAction("&Redo", master),
            'sep1': self.__get_separator(master),
            'cut': QAction("Cu&t", master),
            'copy': QAction("&Copy", master),
            'paste': QAction("&Paste", master),
            'sep2': self.__get_separator(master),
            'replace_in_file': QAction("&Replace in file", master),
        }
        self.VIEW = {
            'status_bar': QAction("Show s&tatus bar", master),
        }
        self.PREFERENCES = {
            'soon': QAction("&Soon", master),
        }
        self.HELP = {
            'about': QAction("&About", master),
        }

    def __get_separator(self, master):
        separator = QAction(master)
        separator.setSeparator(True)
        return separator
