from .text_area import TextArea
from PyQt5.QtWidgets import QTabWidget


class FilesBar(QTabWidget):

    def __init__(self):
        super().__init__()
        self.setMovable(True)
        self.setTabsClosable(True)
        self.tabCloseRequested.connect(self.close_tab)
        self.tabs = []

    def open_tab(self, name: str="Untilted", data: str="", path=None):
        text_widget = TextArea(name, data, path)
        self.addTab(text_widget, name)
        self.tabs.append(name)
        self.setCurrentIndex(len(self.tabs) - 1)

    def close_tab(self, index: int):
        print("Closed:", index)
        self.removeTab(index)
        self.tabs.pop(index)

    def get_current_name(self):
        if not self.is_open_something():
            return False
        return self.currentWidget().get_name()

    def get_current_text(self):
        if not self.is_open_something():
            return False
        return self.currentWidget().text().replace("\r", '')

    def get_current_path(self):
        if not self.is_open_something() and self.is_current_path():
            return False
        return self.currentWidget().get_path()

    def is_open_something(self):
        return self.currentIndex() >= 0

    def is_current_path(self):
        return self.currentWidget().get_path() is None

    def update_name(self, name: str):
        if not self.is_open_something():
            return False
        self.setTabText(self.currentIndex(), name)
        self.currentWidget().change_name(name)

    def update_path(self, path: str):
        if not self.is_open_something():
            return False
        self.currentWidget().change_path(path)

    def undo(self):
        if self.is_open_something():
            self.currentWidget().undo()

    def redo(self):
        if self.is_open_something():
            self.currentWidget().redo()

    def cut(self):
        if self.is_open_something():
            self.currentWidget().cut()

    def copy(self):
        if self.is_open_something():
            self.currentWidget().copy()

    def paste(self):
        if self.is_open_something():
            self.currentWidget().paste()
