import sys
import os
from PyQt6.QtWidgets import   QWidget,  QHBoxLayout, QTableWidget,QTableWidgetItem
from PyQt6.QtGui import QPalette, QColor,QIcon
from PyQt6.QtCore import QSize, Qt


class Cfoot(QWidget):

    def __init__(self):
        super(Cfoot, self).__init__()
        self.layout = QHBoxLayout()

        table_widget = QTableWidget(3,4)
        self.layout.addWidget(table_widget)

        table_item = QTableWidgetItem()
        table_item.setText("列1")
        table_widget.setHorizontalHeaderItem(0,table_item)
        table_widget.setColumnWidth(0,120)


        self.setLayout(self.layout)
