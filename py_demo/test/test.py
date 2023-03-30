import sys
from PyQt6.QtWidgets import QApplication, QWidget, QGroupBox, QVBoxLayout, QPushButton, QStackedLayout

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()

        # 创建第一个 QGroupBox
        self.groupBox1 = QGroupBox("Group Box 1")
        layout1 = QVBoxLayout()
        layout1.addWidget(QPushButton("Button 1"))
        self.groupBox1.setLayout(layout1)

        

        # 创建 QStackedLayout
        self.stackedLayout = QStackedLayout()
        self.stackedLayout.addWidget(self.groupBox1)

        # 创建 QPushButton
        self.button = QPushButton("Replace Group Box")
        self.button.clicked.connect(self.replace_groupbox)

        # 将 QStackedLayout 和 QPushButton 添加到 QVBoxLayout 中
        layout = QVBoxLayout()
        layout.addLayout(self.stackedLayout)
        layout.addWidget(self.button)
        self.setLayout(layout)

    def replace_groupbox(self):
        # 创建第二个 QGroupBox
        self.groupBox2 = QGroupBox("Group Box 2")
        layout2 = QVBoxLayout()
        layout2.addWidget(QPushButton("Button 2"))
        self.groupBox2.setLayout(layout2)
        self.stackedLayout.addWidget(self.groupBox2)


        if self.groupBox1.isVisible():
            self.stackedLayout.setCurrentWidget(self.groupBox2)
        else:
            self.stackedLayout.setCurrentWidget(self.groupBox1)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = MyWidget()
    widget.show()
    sys.exit(app.exec())
