import sys
import os
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit
from PyQt6.QtGui import QPalette, QColor, QIcon
from PyQt6.QtCore import QSize, Qt
from resource.components import get_list, main_func
from resource.utils.upath import resource_path
from resource.components import log_box
from resource.utils.contact import Communicate


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        # 窗口名/大小/图标/布局
        self.setWindowTitle("电脑配件QT版")
        # self.setFixedSize(QSize(800, 600))
        self.setWindowIcon(QIcon(resource_path("img/mati_ei_256.ico")))
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(20)

        # 三个组件
        self.get_list = get_list.GetList()
        self.log_box = log_box.LogBox()
        self.main_func = main_func.MainFunc()
        layout.addWidget(self.get_list)
        layout.addWidget(self.main_func)
        layout.addWidget(self.log_box)
        self.get_list.tomain.dataChanged.connect(self.main_func.tolist.dataChanged)


        # 主体布局
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
