from .text_area import TextArea
from PyQt5.QtWidgets import QTabWidget
from PyQt5.QtCore import pyqtSignal


class FilesBar(QTabWidget):
    new_tab = pyqtSignal()
    nothing_open = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setMovable(True)
        self.setTabsClosable(True)
        self.tabCloseRequested.connect(self.close_tab)
        self.tabs = []

    def open_tab(self, name: str="Untilted", data: str="", path=None):
        if not self.is_open_something():
            self.new_tab.emit()
        text_widget = TextArea(name, data, path)
        self.addTab(text_widget, name)
        self.setCurrentIndex(self.count()-1)

    def close_tab(self, index: int = None):
        if not self.is_open_something():
            return
        if index is None:
            index = self.currentIndex()
        self.removeTab(index)
        if self.count() == 0:
            self.nothing_open.emit()

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
        return self.count() != 0

    def is_current_path(self):
        return self.currentWidget().get_path() is None

    def update_name(self, name: str):
        if not self.is_open_something():
            return False
        self.currentWidget().change_name(name)
        self.setTabText(self.currentIndex(), name)

    def update_path(self, path: str):
        if not self.is_open_something():
            return False
        self.currentWidget().change_path(path)

    def replace_in_text(self, old: str, new: str):
        self.currentWidget().setText(
            self.currentWidget().text().replace(old, new)
        )

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

    def count_text(self, text: str) -> int:
        return self.currentWidget().count(text)
