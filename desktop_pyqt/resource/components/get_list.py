from PyQt6.QtWidgets import QComboBox, QGroupBox, QWidget, QHBoxLayout, QLabel, QLineEdit, QPushButton
from resource.utils.upath import resource_path
from resource.utils.contact import Communicate
import json


class GetList(QWidget):

    def __init__(self):
        super(GetList, self).__init__()

        self.tomain = Communicate()

        # 加载json数据
        self.index = self.load_index()
        index_group = [self.index[item]["label"] for item in self.index]
        index_function = [self.index["preset"]["data"][item] for item in self.index["preset"]["data"]]
        self.index_function_name = [item for item in self.index["preset"]["data"]]
        self.selected = self.index_function_name[0]

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
        self.combo_box1.currentIndexChanged.connect(self.on_group_changed)

        # 下拉菜单2: 具体功能
        self.combo_box2 = QComboBox()
        self.combo_box2.setFixedWidth(150)
        self.combo_box2.addItems(index_function)
        hbox.addWidget(self.combo_box2)
        self.combo_box2.currentIndexChanged.connect(self.on_function_changed)

        # 按钮go
        btn_start = QPushButton("go")
        btn_start.clicked.connect(self.start)
        hbox.addWidget(btn_start)

        # 弹簧
        hbox.addStretch()

        self.setLayout(self.layout)

    def load_index(self):
        '''加载index.json'''
        index_path = resource_path("py_script/index.json")
        with open(index_path, "r", encoding="utf-8")as list_file:
            list_json = json.load(list_file)
            return list_json["data"]

    def on_group_changed(self, num):
        '''组选项被更改'''
        # 更新功能下拉框菜单
        index_group = [item for item in self.index]
        group_selected = index_group[num]
        index_function = [self.index[group_selected]["data"][item] for item in self.index[group_selected]["data"]]
        self.combo_box2.clear()
        self.combo_box2.addItems(index_function)
        # 更新默认选中项
        self.index_function_name = [item for item in self.index[group_selected]["data"]]
        self.selected = self.index_function_name[0]

    def on_function_changed(self, num):
        '''功能选项被更改'''
        self.selected = self.index_function_name[num]

    def start(self):
        '''开始按钮'''
        self.tomain.dataChanged.emit(self.selected)

