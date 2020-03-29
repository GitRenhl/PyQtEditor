from PyQt5.QtWidgets import QMessageBox


def ask_before_exit(parent, unsaved_file: bool = False):
    if unsaved_file:
        return _question(parent, message="You have unsaved file!")
    else:
        return _question(parent)


def _question(parent, *, title="Message", message=""):
    if message:
        message += "<br>" * 2

    retval = QMessageBox.question(
        parent,
        "Message",
        f"{message}Are you sure you want to quit?",
        QMessageBox.Yes | QMessageBox.No,
        QMessageBox.No
    )
    return _change_answer_to_bool(retval)


def _change_answer_to_bool(answer):
    '''If the answer is "No" then return False, else True'''
    # QMessageBox.No - <answer>
    #
    # QMessageBox.No - QMessageBox.No = 0 return False
    # QMessageBox.No - QMessageBox.Yes = 49152 return True
    return QMessageBox.No - answer == 49152
