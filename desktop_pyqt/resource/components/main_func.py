from PyQt6.QtWidgets import QGroupBox, QWidget, QStackedLayout, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QCheckBox, QComboBox,QPushButton
from PyQt6.QtCore import Qt
from resource.utils.contact import Communicate
from resource.utils.upath import resource_path
import os
import json
import pkgutil
import time
import importlib
import sys
import subprocess
import threading

class MainFunc(QWidget):

    def __init__(self):
        super(MainFunc, self).__init__()

        # 通信
        self.module_name=""
        self.intf = ""
        self.tolist = Communicate()
        self.tolist.dataChanged.connect(self.refresh)
        self.tolog = Communicate()

        # 布局
        self.layout_main = QVBoxLayout()
        self.groupbox = QGroupBox("输入参数")
        self.layout_main.addWidget(self.groupbox)
        self.vbox = QVBoxLayout()
        self.groupbox.setLayout(self.vbox)

        # 第一行初始化标签
        layout_init = QHBoxLayout()
        self.vbox.addLayout(layout_init)
        label1 = QLabel("请选择功能", self)
        label1.setFixedWidth(100)
        layout_init.addWidget(label1)

        # 创建 QStackedLayout支持groupbox的切换
        self.stackedLayout = QStackedLayout()
        self.stackedLayout.addWidget(self.groupbox)
        self.layout_main.addLayout(self.stackedLayout)
        self.setLayout(self.layout_main)

    def refresh(self, data):
        '''list发来消息,刷新布局'''

        # 读取json数据
        self.module_name = data
        intf_file_path = os.path.join("py_script", self.module_name, "intf.json")
        intf_file_path = resource_path(intf_file_path)
        self.intf = json.load(open(intf_file_path, "r", encoding="utf-8"))
        self.intf = json.dumps(self.intf)
        self.intf = json.loads(self.intf)

        # 设置新groupbox
        newbox = QGroupBox(self.intf["title"])
        vbox = QVBoxLayout()
        newbox.setLayout(vbox)

        for item in self.intf["require"]:

            # 设置QComboBox下拉框
            if item["type"] == "select":
                new_line = QHBoxLayout()
                # 标签
                label = QLabel(item['data']['label'])
                label.setFixedWidth(100)
                new_line.addWidget(label)
                # 下拉框
                cbox = QComboBox()
                cbox.addItems([i['label'] for i in item['data']['option']])
                cbox.currentIndexChanged.connect(lambda index, item=item: self.on_combobox_changed(index, item))
                new_line.addWidget(cbox)
                # 布局
                vbox.addLayout(new_line)

            # 设置QLineEdit输入框
            elif item["type"] == "input":
                new_line = QHBoxLayout()
                # 标签
                label = QLabel(item['data']['label'])
                label.setFixedWidth(100)
                new_line.addWidget(label)
                # 输入框
                txtl = QLineEdit()
                placeholder = item['data']['placeholder'] if "placeholder" in item['data']else "请输入 ..."
                txtl.setPlaceholderText(placeholder)
                text = item['data']['value'] if "value" in item['data']else ""
                txtl.textChanged.connect(lambda text,item = item: self.on_lineedit_changed(text,item))
                txtl.setText(text)
                
                # 布局
                new_line.addWidget(txtl)
                vbox.addLayout(new_line)

            # 设置QCheckBox复选框
            elif item["type"] == "switch":
                new_line = QHBoxLayout()
                # 标签
                label = QLabel(item['data']['label'])
                label.setFixedWidth(100)
                new_line.addWidget(label)
                # 输入框
                checkb = QCheckBox()
                if item['data']['value']:
                    checkb.setCheckState(Qt.CheckState.Checked)
                new_line.addWidget(checkb)
                checkb.stateChanged.connect(lambda state,item=item: self.on_checkbox_changed(state,item))
                # 布局
                vbox.addLayout(new_line)

            else:
                print("unexpected type : %s" % item["type"])

        # 启动按钮
        new_line = QHBoxLayout()
        btn_start = QPushButton("run")
        btn_start.clicked.connect(self.run)
        new_line.addWidget(btn_start)

        # 布局
        vbox.addLayout(new_line)
        self.stackedLayout.addWidget(newbox)
        self.stackedLayout.setCurrentWidget(newbox)

    def change_value(self,key,value):
        '''遍历修改intf中的value'''
        for index,item in enumerate(self.intf["require"]):
            if item["data"]["key"] == key:
                self.intf["require"][index]["data"]["value"] = value

    def on_combobox_changed(self,index,item):
        '''下拉框被改变'''
        key = item["data"]["key"]
        value = item["data"]["option"][index]["value"]
        self.change_value(key,value)

    def on_lineedit_changed(self,text,item):
        '''输入框被改变'''
        key = item["data"]["key"]
        value = text
        self.change_value(key,value)

    def on_checkbox_changed(self,state,item):
        '''复选框被改变'''
        key = item["data"]["key"]
        value = True if state else False
        self.change_value(key,value)


    def run(self):
        '''启动程序'''

        # 装载参数
        json_set = {}
        for item in self.intf["require"]:
            if item["type"] == "button":
                continue
            json_set[item["data"]["key"]] = item["data"]["value"]
        
        # 功能主函数
        get_function = self.module_name
        py_path = resource_path("py_script")
        sys.path.append(py_path)

        # 定义工作主函数
        def main_func() -> None:
            now = time.time()
            for filefiner, name, ispkg in pkgutil.iter_modules([py_path]):
                if name == get_function:
                    importlib.import_module(name)
                    module = sys.modules[name]
                    mc = module.MainClass(json_set=json_set)
                    mc.run()

            time_spent_ms = int(1000 * (time.time() - now))
            time_spent = str(time_spent_ms / 1000) + "s" if time_spent_ms > 1000 else str(time_spent_ms) + "ms"
            print("time-cost: %s" % time_spent)


        # 直接调用
        def run_direct():
            main_func()

        # # 终端调用
        # def run_terminal():
        #     subprocess.run(['python', './app_sp_operator/terminal_searcher.py', json.dumps(json_set)], creationflags=subprocess.CREATE_NEW_CONSOLE)
        #     # subprocess.run(['python', './app_sp_operator/terminal_searcher.py', json.dumps(get_data)])
        # if json_set["terminal"] == True:
        #     go_main = threading.Thread(target=run_terminal)
        #     go_main.start()
        #     return

        go_main = threading.Thread(target=run_direct)
        go_main.start()


