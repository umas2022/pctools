import sys
import os
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget,QPushButton, QVBoxLayout, QHBoxLayout, QLabel,QLineEdit
from PyQt6.QtGui import QPalette, QColor,QIcon
from PyQt6.QtCore import QSize, Qt


class Cbody(QWidget):

    def __init__(self):
        super(Cbody, self).__init__()
        self.layout = QHBoxLayout()

        txt_line = QLineEdit()
        txt_line.setPlaceholderText("input ...")
        self.layout.addWidget(txt_line)
        btn_add = QPushButton("add")
        self.layout.addWidget(btn_add)

        self.setLayout(self.layout)
