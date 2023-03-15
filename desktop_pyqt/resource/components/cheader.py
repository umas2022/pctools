import sys
import os
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel,QLineEdit,QPushButton
from PyQt6.QtGui import QPalette, QColor,QIcon
from PyQt6.QtCore import QSize, Qt


class Cheader(QWidget):

    def __init__(self):
        super(Cheader, self).__init__()
        self.layout = QHBoxLayout()

        btn_start = QPushButton("start")
        self.layout.addWidget(btn_start)

        btn_stop = QPushButton("stop")
        self.layout.addWidget(btn_stop)

        self.layout.addStretch()

        self.setLayout(self.layout)
