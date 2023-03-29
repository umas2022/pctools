import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QGroupBox, QHBoxLayout, QPushButton

class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # 创建一个垂直布局
        vbox = QVBoxLayout()

        # 创建一个QGroupBox并将其添加到vbox中
        groupbox = QGroupBox("Group Box")
        vbox.addWidget(groupbox)

        # 在QGroupBox中创建一个水平布局
        hbox = QHBoxLayout()
        groupbox.setLayout(hbox)

        # 创建两个按钮并将其添加到水平布局中
        btn1 = QPushButton("Button 1")
        hbox.addWidget(btn1)
        btn2 = QPushButton("Button 2")
        hbox.addWidget(btn2)

        # 设置窗口的布局
        self.setLayout(vbox)

        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('QGroupBox Example')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())
