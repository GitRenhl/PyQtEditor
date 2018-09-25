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

    def get_text_from_current_tab(self):
        if self.is_open_something():
            return self.currentWidget().toPlainText()
        return False

    def is_open_something(self):
        return self.currentIndex() >= 0

    def is_current_path(self):
        return self.currentWidget().file_path is None
