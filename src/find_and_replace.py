from PyQt5.QtWidgets import QWidget, \
    QHBoxLayout,\
    QVBoxLayout,\
    QDialog,\
    QLineEdit,\
    QLabel,\
    QPushButton
from PyQt5.QtCore import Qt


class FindAndReplace(QDialog):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.master = parent
        self.find = QLineEdit()
        self.replace = QLineEdit()

        self.status_bar = QLabel()
        self.status_bar.setText("Simple Text")

        self.setup_ui()

        self.show()

    def setup_ui(self):
        self.setWindowTitle("Replace text")
        self.resize(300, 80)
        self.setWindowModality(Qt.ApplicationModal)

        main_lay = QVBoxLayout()
        lay1 = QVBoxLayout()
        lay1_1 = QHBoxLayout()
        lay1_2 = QHBoxLayout()

        lay2 = QVBoxLayout()

        # LAY 1_1
        label_find = QLabel()
        label_find.setText("Find:")
        lay1_1.addWidget(label_find)
        lay1_1.addWidget(self.find)

        # LAY 1_2
        label_replace = QLabel()
        label_replace.setText("Replace:")
        lay1_2.addWidget(label_replace)
        lay1_2.addWidget(self.replace)

        # LAY 1 #
        lay1.addLayout(lay1_1)
        lay1.addLayout(lay1_2)

        # LAY 2 #
        btn_replace_all = QPushButton("Replace all")
        btn_replace_all.clicked.connect(self.__btn_replace_all_click)
        btn_count = QPushButton("Count")
        btn_count.clicked.connect(self.__btn_count)
        btn_exit = QPushButton("Exit")
        btn_exit.clicked.connect(self.close)
        lay2.addWidget(btn_replace_all)
        lay2.addWidget(btn_count)
        lay2.addWidget(btn_exit)

        # MESSAGE LEY
        ley_msg = QVBoxLayout()
        ley_msg.addWidget(self.status_bar)

        # ACTION LAY
        action_lay = QHBoxLayout()
        action_lay.addLayout(lay1)
        action_lay.addLayout(lay2)

        # MAIN LAY #
        main_lay.addLayout(action_lay)
        main_lay.addLayout(ley_msg)

        self.setLayout(main_lay)

    def __btn_replace_all_click(self):
        old, new = self.find.text(), self.replace.text()
        print("replace", old, new)
        self.master.files_tabs.replace_in_text(
            old, new
        )

    def __btn_count(self):
        counter = self.master.files_tabs.count_text(self.find.text())
        self.status_bar.setStyleSheet("QLabel {color: blue;}")
        self.status_bar.setText(f"Count: {counter} matches.")
