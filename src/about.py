from PyQt5.QtWidgets import QMessageBox


_version = "0.0.0"
_author = "Marcin Ożóg"
_about_text = """
Version: {}
Author: {}
""".format(
    _version,
    _author
)


def show():
    _about = QMessageBox()
    _about.setWindowTitle("About")
    _about.setIcon(QMessageBox.Information)

    _about.setText("PyQt Text Editor")
    _about.setInformativeText(_about_text)
    _about.setStandardButtons(QMessageBox.Ok)
    return _about.exec_()
