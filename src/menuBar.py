from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QMenuBar, QAction


class MenuBar(QMenuBar):

    # file tab
    new_file = pyqtSignal()
    save_file = pyqtSignal()
    save_file_as = pyqtSignal()
    open_file = pyqtSignal()
    close_window = pyqtSignal()

    # help tab

    def __init__(self):
        super().__init__()
        self.menu_file = self.addMenu("&File")
        self.menu_edit = self.addMenu("&Edit")
        self.menu_view = self.addMenu("&View")
        self.menu_settings = self.addMenu("&Settings")
        self.menu_help = self.addMenu("&Help")

        self._set_file_menu()
        self._set_edit_menu()
        self._set_view_menu()
        self._set_settings_menu()
        self._set_help_menu()

    def _set_file_menu(self):
        actions = {
            'new': QAction("&New File", self),
            'save': QAction("&Save", self),
            'save_as': QAction("Save &As...", self),
            'open': QAction("&Open File...", self),
            'exit': QAction("&Exit", self),
        }
        actions['new'].setShortcut("Ctrl+N")
        actions['new'].triggered.connect(lambda: self.new_file.emit())

        actions['save'].setShortcut("Ctrl+S")
        actions['save'].triggered.connect(lambda: self.save_file.emit())

        actions['save_as'].setShortcut("Ctrl+Shift+S")
        actions['save_as'].triggered.connect(lambda: self.save_file_as.emit())

        actions['open'].setShortcut("Ctrl+O")
        actions['open'].triggered.connect(lambda: self.open_file.emit())

        actions['exit'].triggered.connect(lambda: self.close_window.emit())

        for key in actions:
            self.menu_file.addAction(actions[key])

    def _set_edit_menu(self):
        # TODO
        actions = {
            'soon': QAction("&Soon", self),
        }
        for key in actions:
            self.menu_edit.addAction(actions[key])

    def _set_view_menu(self):
        # TODO
        actions = {
            'soon': QAction("&Soon", self),
        }
        for key in actions:
            self.menu_view.addAction(actions[key])

    def _set_settings_menu(self):
        # TODO
        actions = {
            'soon': QAction("&Soon", self),
        }
        for key in actions:
            self.menu_settings.addAction(actions[key])

    def _set_help_menu(self):
        actions = {
            'about': QAction("&About", self),
        }
        for key in actions:
            self.menu_help.addAction(actions[key])
