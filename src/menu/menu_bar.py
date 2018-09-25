from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QMenuBar
from .bookmark import Bookmark


class MenuBar(QMenuBar):

    # file tab
    new_file = pyqtSignal()
    save_file = pyqtSignal()
    save_file_as = pyqtSignal()
    open_file = pyqtSignal()
    close_window = pyqtSignal()
    # edit tab
    undo = pyqtSignal()
    redo = pyqtSignal()
    cut = pyqtSignal()
    copy = pyqtSignal()
    paste = pyqtSignal()
    # view tab
    # settings tab
    # help tab
    about = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.menu_file = self.addMenu("&File")
        self.menu_edit = self.addMenu("&Edit")
        self.menu_view = self.addMenu("&View")
        self.menu_preferences = self.addMenu("&Preferences")
        self.menu_help = self.addMenu("&Help")

        self.bookmarks = Bookmark(self)

        self._set_file_menu()
        self._set_edit_menu()
        self._set_view_menu()
        self._set_preferences_menu()
        self._set_help_menu()

    def _set_file_menu(self):
        self.bookmarks.FILE['new'].setShortcut("Ctrl+N")
        self.bookmarks.FILE['new'].triggered.connect(
            lambda: self.new_file.emit()
        )

        self.bookmarks.FILE['save'].setShortcut("Ctrl+S")
        self.bookmarks.FILE['save'].triggered.connect(
            lambda: self.save_file.emit()
        )

        self.bookmarks.FILE['save_as'].setShortcut("Ctrl+Shift+S")
        self.bookmarks.FILE['save_as'].triggered.connect(
            lambda: self.save_file_as.emit())

        self.bookmarks.FILE['open'].setShortcut("Ctrl+O")
        self.bookmarks.FILE['open'].triggered.connect(
            lambda: self.open_file.emit()
        )

        self.bookmarks.FILE['exit'].triggered.connect(
            lambda: self.close_window.emit()
        )

        for key in self.bookmarks.FILE:
            self.menu_file.addAction(self.bookmarks.FILE[key])

    def _set_edit_menu(self):
        for key in self.bookmarks.EDIT:
            self.menu_edit.addAction(self.bookmarks.EDIT[key])

    def _set_view_menu(self):
        for key in self.bookmarks.VIEW:
            self.menu_view.addAction(self.bookmarks.VIEW[key])

    def _set_preferences_menu(self):
        for key in self.bookmarks.PREFERENCES:
            self.menu_preferences.addAction(self.bookmarks.PREFERENCES[key])

    def _set_help_menu(self):
        for key in self.bookmarks.HELP:
            self.menu_help.addAction(self.bookmarks.HELP[key])
