from .text_area import TextArea
from PyQt5.QtWidgets import QTabWidget
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QIcon


class FilesBar(QTabWidget):
    s_new_tab = pyqtSignal()
    s_nothing_open = pyqtSignal()
    s_cursor_position_changed = pyqtSignal(int, int)

    _ICON_DOT = QIcon("assets/dot-dark.png")

    def __init__(self):
        super().__init__()
        self.setMovable(True)
        self.setTabsClosable(True)
        self.tabCloseRequested.connect(self.close_tab)
        self.tabs = []

    def __cursor_position_changed(self, line, index):
        self.s_cursor_position_changed.emit(line, index)

    def __selection_changed(self, *a, **k):
        # TODO implemet this
        # show "[int] selected" on status bar
        pass

    def show_modified_dot(self):
        new_text = self.currentWidget().get_name()
        if self.currentWidget().isModified():
            # self.setTabIcon(self.currentIndex(), self._ICON_DOT) # it does not working
            new_text += ' *'

        self.setTabText(self.currentIndex(), new_text)

    def open_new_tab(self, name: str = "Untilted", data: str = "", path=None):
        if not self.is_open_something():
            self.s_new_tab.emit()
        ta_widget = TextArea(name, data, path)
        ta_widget.cursorPositionChanged.connect(self.__cursor_position_changed)
        ta_widget.selectionChanged.connect(self.__selection_changed)
        self.addTab(ta_widget, name)
        self.setCurrentIndex(self.count() - 1)
        self.currentWidget().modificationChanged.connect(self.show_modified_dot)

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
            self.s_nothing_open.emit()

    # TODO to every get add index param and if param is None then use current widget
    def get_current_name(self):
        if not self.is_open_something():
            return False
        return self.currentWidget().get_name()

    def get_current_text(self) -> str:
        if not self.is_open_something():
            return False
        return self.currentWidget().text().replace("\r", '')

    def get_current_path(self) -> str:
        if not self.is_open_something() or not self.is_current_path():
            return None
        return self.currentWidget().get_path()

    def is_open_something(self) -> bool:
        return self.count() != 0

    def is_current_path(self) -> bool:
        '''Will return True if current file have a path'''
        return self.currentWidget().get_path() is not None

    def is_modified(self, *, index: int = None) -> bool:
        '''This function will return True if widgets[index] is modified.

        If you use this function without index parametr it will return True
        if any of widgets are modified.'''
        def is_modified_by_i(index):
            widget = self.widget(index)
            return widget.isModified()

        valid = False
        if index is None:
            for index in range(self.count()):
                if is_modified_by_i(index):
                    valid = True
                    break
        else:
            assert index >= 0 and index < self.count()
            if is_modified_by_i(index):
                valid = True

        return valid

    def update_name(self, name: str):
        '''Update current widget file name'''
        if not self.is_open_something():
            return False
        self.currentWidget().change_name(name)
        self.setTabText(self.currentIndex(), name)

    def update_path(self, path: str):
        '''Update current widget file path'''
        if not self.is_open_something():
            return False
        self.currentWidget().change_path(path)

    # def replace_in_text(self, old: str, new: str):
    #     ''' Replace "old" with "new" in current file.

    #     This function should not be using,
    #     because it will not save in copy/paste history '''
    #     currentWidget = self.currentWidget()
    #     new_text = currentWidget.text().replace(old, new)
    #     currentWidget.setText(new_text)

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

    def count_text(self, string: str, *, case: bool = True) -> int:
        return self.currentWidget().count(string, case=case)
