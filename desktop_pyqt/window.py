import sys
import os
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel,QLineEdit
from PyQt6.QtGui import QPalette, QColor,QIcon
from PyQt6.QtCore import QSize, Qt


from resource.utils.upath import resource_path
from resource.components import cheader,cbody,cfoot


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("My App")
        self.setFixedSize(QSize(800, 600))
        self.setWindowIcon(QIcon(resource_path("img/mati_ei_256.ico")))

        # current_dir = resource_path("")
        # label = QLabel(current_dir)
        # self.setCentralWidget(label)

        layout1 = QVBoxLayout()

        layout1.setContentsMargins(0,0,0,0)
        layout1.setSpacing(20)

        layout1.addWidget(cheader.Cheader())
        layout1.addWidget(cbody.Cbody())
        layout1.addWidget(cfoot.Cfoot())

        # 弹簧,把空元素顶上去
        layout1.addStretch()

        widget = QWidget()
        widget.setLayout(layout1)
        self.setCentralWidget(widget)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
