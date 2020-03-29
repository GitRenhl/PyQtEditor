from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QMenuBar
from .bookmark import Bookmark


class MenuBar(QMenuBar):

    # FILE tab
    new_file = pyqtSignal()
    save_file = pyqtSignal()
    save_file_as = pyqtSignal()
    open_file = pyqtSignal()
    close_tab = pyqtSignal()
    close_program = pyqtSignal()
    # EDIT tab
    undo = pyqtSignal()
    redo = pyqtSignal()
    cut = pyqtSignal()
    copy = pyqtSignal()
    paste = pyqtSignal()
    replace_in_file = pyqtSignal()
    # VIEW tab
    hideshow_status_bar = pyqtSignal(bool)

    # SETTINGS tab

    # HELP tab
    about = pyqtSignal()

    __file = ("save", "save_as", "close_tab")
    __edit = ("undo", "redo", "cut", "copy", "paste", "replace_in_file")

    def __init__(self):
        super().__init__()
        self.menu_file = self.addMenu("&File")
        self.menu_edit = self.addMenu("&Edit")
        self.menu_view = self.addMenu("&View")
        self.menu_preferences = self.addMenu("&Preferences")
        self.menu_help = self.addMenu("&Help")

        self.bookmarks = Bookmark(self)
        self.__is_editing_enable = True

        self.__setup()

    def __setup(self):
        self.__set_file_menu()
        self.__set_edit_menu()
        self.__set_view_menu()
        self.__set_preferences_menu()
        self.__set_help_menu()

    def __set_file_menu(self):
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

        self.bookmarks.FILE['open_file'].setShortcut("Ctrl+O")
        self.bookmarks.FILE['open_file'].triggered.connect(
            lambda: self.open_file.emit()
        )

        self.bookmarks.FILE['close_tab'].setShortcut("Ctrl+W")
        self.bookmarks.FILE['close_tab'].triggered.connect(
            lambda: self.close_tab.emit()
        )

        self.bookmarks.FILE['exit'].triggered.connect(
            lambda: self.close_program.emit()
        )

        for key in self.bookmarks.FILE:
            self.menu_file.addAction(self.bookmarks.FILE[key])

    def __set_edit_menu(self):
        self.bookmarks.EDIT['undo'].setShortcut("Ctrl+Z")
        self.bookmarks.EDIT['undo'].triggered.connect(
            lambda: self.undo.emit())

        self.bookmarks.EDIT['redo'].setShortcut("Ctrl+Y")
        self.bookmarks.EDIT['redo'].triggered.connect(
            lambda: self.redo.emit())

        self.bookmarks.EDIT['cut'].setShortcut("Ctrl+X")
        self.bookmarks.EDIT['cut'].triggered.connect(
            lambda: self.cut.emit())

        self.bookmarks.EDIT['copy'].setShortcut("Ctrl+C")
        self.bookmarks.EDIT['copy'].triggered.connect(
            lambda: self.copy.emit())

        self.bookmarks.EDIT['paste'].setShortcut("Ctrl+V")
        self.bookmarks.EDIT['paste'].triggered.connect(
            lambda: self.paste.emit())

        self.bookmarks.EDIT['replace_in_file'].setShortcut("Ctrl+H")
        self.bookmarks.EDIT['replace_in_file'].triggered.connect(
            lambda: self.replace_in_file.emit())

        for key in self.bookmarks.EDIT:
            self.menu_edit.addAction(self.bookmarks.EDIT[key])

    def __set_view_menu(self):
        self.bookmarks.VIEW['status_bar'].setCheckable(True)
        self.bookmarks.VIEW['status_bar'].changed.connect(
            lambda: self.hideshow_status_bar.emit(
                self.bookmarks.VIEW['status_bar'].isChecked()
            )
        )
        for key in self.bookmarks.VIEW:
            self.menu_view.addAction(self.bookmarks.VIEW[key])

    def __set_preferences_menu(self):
        for key in self.bookmarks.PREFERENCES:
            self.menu_preferences.addAction(self.bookmarks.PREFERENCES[key])

    def __set_help_menu(self):
        self.bookmarks.HELP['about'].triggered.connect(
            lambda: self.about.emit()
        )
        for key in self.bookmarks.HELP:
            self.menu_help.addAction(self.bookmarks.HELP[key])

    def disable_editing(self):
        if not self.__is_editing_enable:
            return
        self.__is_editing_enable = False
        for i in self.__file:
            self.bookmarks.FILE[i].setDisabled(True)
        for i in self.__edit:
            self.bookmarks.EDIT[i].setDisabled(True)

    def enable_editing(self):
        if self.__is_editing_enable:
            return
        self.__is_editing_enable = True
        for i in self.__file:
            self.bookmarks.FILE[i].setEnabled(True)
        for i in self.__edit:
            self.bookmarks.EDIT[i].setEnabled(True)
