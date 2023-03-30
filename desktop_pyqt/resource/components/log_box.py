from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QTextEdit, QGroupBox

from resource.utils.contact import Communicate

class LogBox(QWidget):

    def __init__(self):
        super(LogBox, self).__init__()

        self.tomain = Communicate()
        self.tomain.dataChanged.connect(self.msg_main)

        self.layout = QVBoxLayout()
        vbox = QVBoxLayout()

        groupbox = QGroupBox("任务日志")
        self.layout.addWidget(groupbox)
        groupbox.setLayout(vbox)

        # 文本区
        self.log_box = QTextEdit()
        # self.log_box.setFixedSize(200, 300)
        self.log_box.setPlaceholderText("Enter your text")
        self.log_text = "log text\n"
        vbox.addWidget(self.log_box)

        # 按钮
        self.btn_add = QPushButton("add")
        self.btn_add.clicked.connect(self.add)
        vbox.addWidget(self.btn_add)

        self.setLayout(self.layout)

    def add(self):
        for i in range(10):
            self.log_text = self.log_text + str(i) + "\n"
            self.log_box.setPlainText(self.log_text)


    def msg_main(self,data):
        '''main_func发来消息'''
        print(data)
