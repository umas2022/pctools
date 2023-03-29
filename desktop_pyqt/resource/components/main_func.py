from PyQt6.QtWidgets import   QGroupBox,QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QCheckBox, QComboBox
from PyQt6.QtCore import  Qt


class MainFunc(QWidget):

    def __init__(self):
        super(MainFunc, self).__init__()

        self.layout_line = QVBoxLayout()
        groupbox = QGroupBox("输入参数")
        self.layout_line.addWidget(groupbox)
        vbox = QVBoxLayout()
        groupbox.setLayout(vbox)

        # 第一行=========================================
        self.layout_item1 = QHBoxLayout()
        vbox.addLayout(self.layout_item1)

        # 标签
        self.label1 = QLabel("输入框", self)
        self.label1.setFixedWidth(100)
        self.layout_item1.addWidget(self.label1)

        # 输入框
        self.txt_line = QLineEdit()
        self.txt_line.setPlaceholderText("input ...")
        self.layout_item1.addWidget(self.txt_line)

        self.layout_item1.addStretch()

        # 第二行========================================
        self.layout_item2 = QHBoxLayout()
        vbox.addLayout(self.layout_item2)

        # 标签
        self.label2 = QLabel("复选框", self)
        self.label2.setFixedWidth(100)
        self.layout_item2.addWidget(self.label2)

        # 复选框
        self.check_box = QCheckBox()
        self.check_box.setCheckState(Qt.CheckState.Checked)
        self.layout_item2.addWidget(self.check_box)

        self.layout_item2.addStretch()

        # 第三行========================================
        self.layout_item3 = QHBoxLayout()
        vbox.addLayout(self.layout_item3)

        # 标签
        self.label3 = QLabel("按钮", self)
        self.label3.setFixedWidth(100)
        self.layout_item3.addWidget(self.label3)

        # 按钮
        self.btn_add = QPushButton("add")
        self.btn_add.clicked.connect(self.add)
        self.layout_item3.addWidget(self.btn_add)

        self.label3_num = QLabel("0", self)
        self.layout_item3.addWidget(self.label3_num)

        self.layout_item3.addStretch()

        # 第四行========================================
        self.layout_item4 = QHBoxLayout()
        vbox.addLayout(self.layout_item4)

        # 标签
        self.label4 = QLabel("下拉框", self)
        self.label4.setFixedWidth(100)
        self.layout_item4.addWidget(self.label4)

        # 下拉框
        self.combo_box = QComboBox()
        self.combo_box.addItems(["One", "Two", "Three"])
        self.layout_item4.addWidget(self.combo_box)

        self.layout_item4.addStretch()

        # 主窗体
        self.setLayout(self.layout_line)

    def add(self):
        # 获取当前标签中的数字，并加1
        num = int(self.label3_num.text()) + 1
        # 将新数字显示在标签中
        self.label3_num.setText(str(num))
