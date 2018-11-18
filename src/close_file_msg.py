from PyQt5.QtWidgets import QMessageBox


def ask_user_about_unsave_file():
    retval = QMessageBox.Yes

    ask = QMessageBox()
    ask.setIcon(QMessageBox.Question)
    ask.setWindowTitle("Exit")
    ask.setText("You have unsaved file!")
    ask.setInformativeText("Do you really want to exit?")
    ask.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
    ask.setDefaultButton(QMessageBox.No)
    retval = ask.exec_()

    # QMessageBox.No - QMessageBox.No = 0 == False
    # QMessageBox.No - QMessageBox.Yes = 49152 == True
    return bool(QMessageBox.No - retval)
