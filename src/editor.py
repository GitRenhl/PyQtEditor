from os.path import split as split_pathname
from os.path import exists as is_file_exists
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QMessageBox, QLabel
from .menu.menu_bar import MenuBar
from .files_bar import FilesBar
from .new_file import NewFile
from .find_and_replace import FindAndReplace


class Editor(QMainWindow):
    _STR_LN_COL_TEHEME = "Ln: {ln}, Col: {col}"

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Text Editor")
        self.resize(1000, 600)

        self._menu_bar = MenuBar()
        self.files_tabs = FilesBar()

        self.status_bar = self.statusBar()
        self._is_status_bar_shown = True
        self._sb_cursor_counter = QLabel()

        self.__init_ui()
        self.__connectSignals()

    def __init_ui(self):
        self._menu_bar.disable_editing()
        self.setMenuBar(self._menu_bar)
        self._menu_bar.bookmarks.VIEW['status_bar'].setChecked(
            self._is_status_bar_shown)
        self.setCentralWidget(self.files_tabs)
        self.__init_status_bar()

    def __init_status_bar(self):
        self.status_bar.addPermanentWidget(self._sb_cursor_counter)
        self._sb_cursor_counter.setText(
            self._STR_LN_COL_TEHEME.format(ln=0, col=0)
        )

    def readSettings(self):
        pass

    def __connectSignals(self):
        self._menu_bar.new_file.connect(self.new_file)
        self._menu_bar.save_file.connect(self.save_file)
        self._menu_bar.save_file_as.connect(self.save_file_as)
        self._menu_bar.open_file.connect(self.open_file)
        self._menu_bar.close_tab.connect(self.files_tabs.close_tab)
        self._menu_bar.close_program.connect(self.close)

        self._menu_bar.undo.connect(self.files_tabs.undo)
        self._menu_bar.redo.connect(self.files_tabs.redo)
        self._menu_bar.cut.connect(self.files_tabs.cut)
        self._menu_bar.copy.connect(self.files_tabs.copy)
        self._menu_bar.paste.connect(self.files_tabs.paste)
        self._menu_bar.replace_in_file.connect(self.replace_in_file)

        self._menu_bar.hideshow_status_bar.connect(self.hideshow_status_bar)

        self._menu_bar.about.connect(self.show_about)

        self.files_tabs.s_new_tab.connect(self._menu_bar.enable_editing)
        self.files_tabs.s_nothing_open.connect(self._menu_bar.disable_editing)
        self.files_tabs.currentChanged.connect(self._current_file_change)
        self.files_tabs.s_cursor_position_changed.connect(
            self._update_coursor_line_counter)

    def _current_file_change(self, index):
        ''' This function should be called by a signal when user change 
        current file'''
        if index == -1:
            # -1 because _update_coursor_line_counter add 1 to ln and col and
            # I want ln, col to be 0, 0 when no file is currently open
            ln, col = -1, -1
        else:
            ln, col = self.files_tabs.currentWidget().getCursorPosition()
        self._update_coursor_line_counter(ln, col)

    def _update_coursor_line_counter(self, line, index):
        ''' This function should be called by a signal when user change 
        cursor position in file'''
        # +1 because no-one normal starts counting from 0
        text = self._STR_LN_COL_TEHEME.format(ln=line + 1,
                                              col=index + 1)
        self._sb_cursor_counter.setText(text)

    def replace_in_file(self):
        '''Open find and replace window'''
        FindAndReplace(self)

    def new_file(self):
        '''Open new file window and after that create new tab in files tabs'''
        dialog = NewFile(self)
        dialog.exec_()
        if dialog.is_create_clicked():
            self.files_tabs.open_new_tab(dialog.name.text())

    @staticmethod
    def __save(path: str, text: str) -> bool:
        try:
            with open(path, 'w') as f:
                f.write(text)
        except Exception as e:
            print(e)
            return False
        return True

    def save_file(self):
        if not self.files_tabs.is_open_something() or not self.files_tabs.currentWidget().isModified():
            return

        PATH = self.files_tabs.get_current_path()
        if PATH is None:
            return self.save_file_as()

        FILE_NAME = self.files_tabs.get_current_name()
        self.status_bar.showMessage(f"Saving file {FILE_NAME}...")
        FULL_PATH = PATH + "/" + FILE_NAME

        if not is_file_exists(FULL_PATH):
            self.status_bar.clearMessage()
            return self.save_file_as()

        DATA = self.files_tabs.get_current_text()
        is_saved = self.__save(FULL_PATH, DATA)

        if not is_saved:
            self.status_bar.showMessage("Error while saving "
                                        f"\"{FILE_NAME}\"")
        else:
            self.status_bar.showMessage(f"File \"{FILE_NAME}\" "
                                        "saved successfully")
            self.files_tabs.currentWidget().setModified(False)

    def save_file_as(self):
        if not self.files_tabs.is_open_something() or not self.files_tabs.currentWidget().isModified():
            return

        self.status_bar.showMessage(f"Saving file as...")
        file_name = QFileDialog.getSaveFileName(self,
                                                "Save as...",
                                                self.files_tabs.get_current_name(),
                                                "All Files (*.*)"
                                                )[0]
        if file_name == '':
            self.status_bar.clearMessage()
            return

        data = self.files_tabs.get_current_text()
        is_saved = self.__save(file_name, data)
        if not is_saved:
            self.status_bar.showMessage("Error while saving "
                                        f"\"{FILE_NAME}\"")
        else:
            new_path, new_name = split_pathname(file_name)
            self.files_tabs.update_name(new_name)
            self.files_tabs.update_path(new_path)
            self.status_bar.showMessage(f"File \"{new_name}\" "
                                        "saved successfully")
            self.files_tabs.currentWidget().setModified(False)

    @staticmethod
    def __open(path: str) -> str:
        try:
            with open(path, 'r') as f:
                text = f.read()
        except Exception as e:
            print(e)
            return
        return text

    def open_file(self):
        file_path = QFileDialog.getOpenFileName(self, "Open file")[0]
        if file_path == "":
            return

        path, name = split_pathname(file_path)
        text = self.__open(file_path)
        if text is None:
            self.status_bar.showMessage("Error while opening "
                                        f"\"{name}\" file",
                                        10000)
            return
        self.files_tabs.open_new_tab(name, text, path)

    def hideshow_status_bar(self, is_show):
        if is_show:
            self.status_bar.show()
            self.files_tabs.currentChanged.connect(
                self._current_file_change)
            self.files_tabs.s_cursor_position_changed.connect(
                self._update_coursor_line_counter)
        else:
            self.status_bar.hide()
            self.files_tabs.currentChanged.disconnect(
                self._current_file_change)
            self.files_tabs.s_cursor_position_changed.disconnect(
                self._update_coursor_line_counter)
        _is_status_bar_shown = is_show

    def show_about(self):
        '''Open about window'''
        from src import about
        about.show(self)

    def closeEvent(self, event):
        '''Call this function after close event.
        The query will appear before exiting the program'''
        from src.close_file_msg import ask_before_exit
        is_something_modified = self.files_tabs.is_modified()
        reply = ask_before_exit(self, is_something_modified)
        if reply:
            event.accept()
        else:
            event.ignore()
