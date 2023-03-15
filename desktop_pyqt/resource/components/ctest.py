import sys
import os
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel,QLineEdit
from PyQt6.QtGui import QPalette, QColor,QIcon
from PyQt6.QtCore import QSize, Qt


class Color(QWidget):

    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(palette)

class Ctest(QWidget):

    def __init__(self, color):
        super(Ctest, self).__init__()
        self.layout = QVBoxLayout()
        # self.layout.setContentsMargins(0,0,0,0)

        w_label = QLabel(color)
        font = w_label.font()
        font.setPointSize(20)
        w_label.setFont(font)
        w_label.setAlignment(Qt.AlignmentFlag(4))
        self.layout.addWidget(w_label)


        w_input = QLineEdit()
        w_input.setPlaceholderText("Enter your text")
        w_input.setFixedWidth(100)
        w_input.setAlignment(Qt.AlignmentFlag(4))
        self.layout.addWidget(w_input)

        self.setLayout(self.layout)
