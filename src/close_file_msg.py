from PyQt5.QtWidgets import QMessageBox


def ask_before_exit(parent, unsaved_file: bool = False):
    print(unsaved_file)
    if unsaved_file:
        return _ask_user_about_unsave_file()
    else:
        return _ask_exit(parent)


def _ask_user_about_unsave_file():
    retval = QMessageBox.Yes

    ask = QMessageBox()
    ask.setIcon(QMessageBox.Question)
    ask.setWindowTitle("Exit")
    ask.setText("You have unsaved file!")
    ask.setInformativeText("Do you really want to exit?")
    ask.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
    ask.setDefaultButton(QMessageBox.No)
    retval = ask.exec_()

    return _change_answer_to_bool(retval)


def _ask_exit(parent):
    retval = QMessageBox.question(
        parent, 'Message',
        "Are you sure you want to quit?", QMessageBox.Yes |
        QMessageBox.No, QMessageBox.No)
    return _change_answer_to_bool(retval)


def _change_answer_to_bool(answer):
    # QMessageBox.No - {answer}
    # QMessageBox.No - QMessageBox.No = 0 == False
    # QMessageBox.No - QMessageBox.Yes = 49152 == True
    return bool(QMessageBox.No - answer)
