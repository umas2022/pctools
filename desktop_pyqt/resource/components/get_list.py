from PyQt6.QtWidgets import QComboBox, QGroupBox, QWidget, QHBoxLayout, QLabel, QLineEdit, QPushButton
from PyQt6.QtGui import QPalette, QColor, QIcon
from PyQt6.QtCore import QSize, Qt
from resource.utils.upath import resource_path
import json


class GetList(QWidget):

    def __init__(self):
        super(GetList, self).__init__()

        self.index = self.load_index()
        index_group = [self.index[item]["label"] for item in self.index]
        index_function=[self.index["preset"]["data"][item] for item in self.index["preset"]["data"]]

        # 布局
        self.layout = QHBoxLayout()
        groupbox = QGroupBox("选择功能")
        self.layout.addWidget(groupbox)
        hbox = QHBoxLayout()
        groupbox.setLayout(hbox)

        # 下拉菜单1: 组选项
        self.combo_box1 = QComboBox()
        self.combo_box1.setFixedWidth(150)
        self.combo_box1.addItems(index_group)
        hbox.addWidget(self.combo_box1)
        self.combo_box1.currentIndexChanged.connect(self.on_combobox_changed)

        # 下拉菜单2: 具体功能
        self.combo_box2 = QComboBox()
        self.combo_box2.setFixedWidth(150)
        self.combo_box2.addItems(index_function)
        hbox.addWidget(self.combo_box2)

        btn_start = QPushButton("go")
        hbox.addWidget(btn_start)

        hbox.addStretch()

        self.setLayout(self.layout)

    def load_index(self):
        '''加载index.json'''
        index_path = resource_path("py_script/index.json")
        with open(index_path, "r", encoding="utf-8")as list_file:
            list_json = json.load(list_file)
            return list_json["data"]
        
    def on_combobox_changed(self,num):
        '''组选项被更改'''
        index_group = [item for item in self.index]
        group_selected = index_group[num]
        index_function=[self.index[group_selected]["data"][item] for item in self.index[group_selected]["data"]]
        self.combo_box2.clear()
        self.combo_box2.addItems(index_function)






