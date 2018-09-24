from .menuBar import MenuBar
from .files_bar import FilesBar
from PyQt5.QtWidgets import QMainWindow, QAction, QApplication, QTextEdit, QFileDialog


class Editor(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Text Editor")
        self.resize(800, 600)

        self._menu_bar = MenuBar()
        self.files_tabs = FilesBar()
        # self.status_bar = self.statusBar()
        self.init_ui()

        self.confSignals()

        self.new_file()

    def init_ui(self):
        self.setMenuBar(self._menu_bar)
        self.setCentralWidget(self.files_tabs)

    def readSettings(self):
        pass

    def confSignals(self):
        self._menu_bar.new_file.connect(self.new_file)
        self._menu_bar.save_file.connect(self.save_file)
        self._menu_bar.save_file_as.connect(self.save_file_as)
        self._menu_bar.open_file.connect(self.open_file)
        self._menu_bar.close_window.connect(self.quit)

    def new_file(self):
        print("New file")
        self.files_tabs.open_tab()
        # self.update_status_bar()

    def save_file(self):
        # TODO
        valid = True
        if not self.files_tabs.is_open_something():
            valid = False
        elif self.files_tabs.is_current_path():
            valid = False
            self.save_file_as()

        if valid:
            print(self.files_tabs.currentWidget().toPlainText())

    def save_file_as(self):
        # TODO
        print("Save as...")

    def open_file(self):
        # TODO
        print("open")

    def quit(self):
        QApplication.quit()

    # def update_status_bar(self):
    #     text = self.files_tabs.currentWidget().toPlainText()
    #     self.status_bar.showMessage("Words:{} Length:{}".format(
    #         len(text),
    #         text.count("\n")
    #     ))
