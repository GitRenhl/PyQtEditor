from PyQt5.QtWidgets import QWidget, \
    QHBoxLayout,\
    QVBoxLayout,\
    QDialog,\
    QLineEdit,\
    QLabel, \
    QCheckBox, \
    QPushButton
from PyQt5.QtCore import Qt


class FindAndReplace(QDialog):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.master = parent
        self.find = QLineEdit()
        self.replace = QLineEdit()

        self.whole_words = QCheckBox()
        self.case_sensitive = QCheckBox()
        self.wraps = QCheckBox()

        self.status_bar = QLabel()

        self.setup_ui()

        self.show()

    def setup_ui(self):
        self.setWindowTitle("Replace text")
        self.setFixedSize(350, 180)
        # self.setWindowModality(Qt.ApplicationModal)
        self.setModal(False)
        self.find.setFixedWidth(160)
        self.replace.setFixedWidth(160)

        main_lay = QVBoxLayout()
        lay_inputs_and_buttons = QHBoxLayout()
        lay_inputs = QVBoxLayout()

        lay_input_text = QVBoxLayout()
        lay_input_text_1 = QHBoxLayout()
        lay_input_text_2 = QHBoxLayout()

        lay_checkboxes = QVBoxLayout()

        lay_buttons = QVBoxLayout()

        ley_msg = QVBoxLayout()

        # TEXT #
        label_find = QLabel()
        label_find.setText("Find:")
        label_find.setAlignment(Qt.AlignRight)
        lay_input_text_1.addWidget(label_find)
        lay_input_text_1.addWidget(self.find)

        label_replace = QLabel()
        label_replace.setText("Replace:")
        label_replace.setAlignment(Qt.AlignRight)
        lay_input_text_2.addWidget(label_replace)
        lay_input_text_2.addWidget(self.replace)

        lay_input_text.addLayout(lay_input_text_1)
        lay_input_text.addLayout(lay_input_text_2)

        # CHECKBOXES #
        # TODO read from cache
        self.whole_words.setChecked(False)
        self.whole_words.setText("Match case")
        self.case_sensitive.setChecked(False)
        self.case_sensitive.setText("Match whole words only")
        self.wraps.setChecked(True)
        self.wraps.setText("Wraps around")

        lay_checkboxes.addWidget(self.whole_words)
        lay_checkboxes.addWidget(self.case_sensitive)
        lay_checkboxes.addWidget(self.wraps)

        # LAY INPUTS #
        lay_inputs.addLayout(lay_input_text)
        lay_inputs.addLayout(lay_checkboxes)

        # LAY BUTTONS #
        buttons = {
            'find': QPushButton("Find Next"),
            'replace': QPushButton("Replace"),
            'replace_all': QPushButton("Replace all"),
            'count': QPushButton("Count"),
            'exit': QPushButton("Exit"),
        }

        buttons['find'].clicked.connect(self.__btn_find)
        buttons['replace'].clicked.connect(self.__btn_replace_click)
        buttons['replace_all'].clicked.connect(self.__btn_replace_all_click)
        buttons['count'].clicked.connect(self.__btn_count)
        buttons['exit'].clicked.connect(self.close)

        for b in buttons.values():
            lay_buttons.addWidget(b)

        # LAY INPUTS AND BUTTONS #
        lay_inputs_and_buttons.addLayout(lay_inputs)
        lay_inputs_and_buttons.addLayout(lay_buttons)

        # MESSAGE LEY
        ley_msg.addWidget(self.status_bar)

        # MAIN LAY #
        main_lay.addLayout(lay_inputs_and_buttons)
        main_lay.addLayout(ley_msg)

        self.setLayout(main_lay)

    def __btn_replace_click(self):
        self.master.files_tabs.currentWidget().replace(self.replace.text())

    def __btn_replace_all_click(self):
        self.status_bar.setText('')
        curWidg = self.master.files_tabs.currentWidget
        replaced = 0
        founded = True
        while True:
            founded = curWidg().findFirst(self.find.text(),
                                          True,
                                          self.case_sensitive.isChecked(),
                                          self.whole_words.isChecked(),
                                          self.wraps.isChecked())
            if founded:
                curWidg().replace(self.replace.text())
                replaced += 1
            else:
                self.status_bar.setStyleSheet("QLabel {color: red;}")
                self.status_bar.setText(
                    f"{replaced} occurrences were replaced")
                break

    def __btn_find(self):
        curWidg = self.master.files_tabs.currentWidget
        founded = curWidg().findFirst(self.find.text(),
                                      True,
                                      self.case_sensitive.isChecked(),
                                      self.whole_words.isChecked(),
                                      self.wraps.isChecked())
        if not founded:
            self.status_bar.setStyleSheet("QLabel {color: red;}")
            self.status_bar.setText(
                "Can't find the text \"{}\"".format(
                    self.find.text()
                )
            )

    def __btn_count(self):
        counter = self.master.files_tabs.count_text(self.find.text())
        self.status_bar.setStyleSheet("QLabel {color: blue;}")
        self.status_bar.setText(f"Count: {counter} matches.")
