from .text_area import TextArea
from PyQt5.QtWidgets import QTabWidget
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QIcon


class FilesBar(QTabWidget):
    new_tab = pyqtSignal()
    nothing_open = pyqtSignal()

    _ICON_DOT = QIcon("assets/dot-dark.png")

    def __init__(self):
        super().__init__()
        self.setMovable(True)
        self.setTabsClosable(True)
        self.tabCloseRequested.connect(self.close_tab)
        self.tabs = []

    def show_modified_dot(self):
        pass
        # if self.currentWidget().isModified():
        #     self.setTabIcon(self.currentIndex(), self._ICON_DOT)
        # else:
        #     self.setTabIcon(self.currentIndex(), None)

    def open_tab(self, name: str="Untilted", data: str="", path=None):
        if not self.is_open_something():
            self.new_tab.emit()
        text_widget = TextArea(name, data, path)
        self.addTab(text_widget, name)
        self.setCurrentIndex(self.count() - 1)
        self.currentWidget().textChanged.connect(self.show_modified_dot)

    def close_tab(self, index: int = None):
        from .close_file_msg import ask_before_exit
        if not self.is_open_something():
            return
        if index is None:
            index = self.currentIndex()

        is_modified = self.is_modified(index=index)
        if is_modified and not ask_before_exit(self, is_modified):
            return

        self.removeTab(index)
        if self.count() == 0:
            self.nothing_open.emit()

    def get_current_name(self):
        if not self.is_open_something():
            return False
        return self.currentWidget().get_name()

    def get_current_text(self) -> str:
        if not self.is_open_something():
            return False
        return self.currentWidget().text().replace("\r", '')

    def get_current_path(self) -> str:
        if not self.is_open_something() and self.is_current_path():
            return False
        return self.currentWidget().get_path()

    def is_open_something(self) -> bool:
        return self.count() != 0

    def is_current_path(self) -> bool:
        return self.currentWidget().get_path() is None

    def is_modified(self, *, index: int = None) -> bool:
        valid = False

        def is_modified(index):
            return self.widget(index).isModified()

        if index is None:
            for i in range(self.count()):
                if is_modified(i):
                    valid = True
                    break
        else:
            assert index >= 0 and index < self.count()
            if is_modified(index):
                valid = True

        return valid

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

    def count_text(
            self,
            string: str,
            *,
            case: bool=True) -> int:
        return self.currentWidget().count(string, case=case)
