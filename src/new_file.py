from PyQt5.QtWidgets import QWidget, \
    QHBoxLayout,\
    QVBoxLayout,\
    QDialog,\
    QLineEdit,\
    QLabel,\
    QPushButton
from PyQt5.QtCore import Qt


class NewFile(QDialog):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.name = QLineEdit()
        self.name.setText("Untilted")
        self.__btn_create_clicked = False
        self.setup_ui()

        self.show()

    def setup_ui(self):
        self.setWindowTitle("New File")
        self.resize(300, 80)
        self.setWindowModality(Qt.ApplicationModal)

        main_lay = QVBoxLayout()
        lay1 = QHBoxLayout()
        lay2 = QHBoxLayout()

        label = QLabel()
        label.setText("File name:")

        lay1.addWidget(label)
        lay1.addWidget(self.name)

        btn_ok = QPushButton("Create")
        btn_ok.clicked.connect(self.__btn_ok_click)
        btn_cancel = QPushButton("Cancel")
        btn_cancel.clicked.connect(self.close)

        lay2.addWidget(btn_ok)
        lay2.addWidget(btn_cancel)

        main_lay.addLayout(lay1)
        main_lay.addLayout(lay2)

        self.setLayout(main_lay)

    def __btn_ok_click(self):
        print("test")
        self.__btn_create_clicked = True
        if self.name.text() == "":
            self.name.setText("Untilted")

        self.close()

    def is_create_clicked(self):
        return self.__btn_create_clicked
