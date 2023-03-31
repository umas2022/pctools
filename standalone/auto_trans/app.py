import sys
import os
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QComboBox, QGroupBox, QPushButton, QTextEdit
from PyQt6.QtGui import QPalette, QColor, QIcon
from PyQt6.QtCore import QSize, Qt

from component.auto_trans import AutoTrans


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.config = {
            # 截图临时文件存放位置
            # "save_path": r"D:\s-code\test\save",
            "save_path": r".",
            # ocr源语言: 竖排日文
            "target": "jpn_vert",
            # 翻译源语言: 日文
            "source": "ja",
            # 翻译目标语言: 简体中文
            "translate": "zh-CN",
            # 文本框字号
            "fontsize":14,
        }

        self.text = {
            # 原文
            "raw": "",
            # 注音
            "romaji": "",
            # 翻译
            "translated": ""
        }

        # 窗口名/大小/图标/布局
        self.setWindowTitle("独立电脑配件-自助翻译")
        layout_main = QVBoxLayout()
        layout_main.setContentsMargins(0, 0, 0, 0)
        layout_main.setSpacing(20)

        # 第一行两个按钮
        layout_line = QHBoxLayout()
        groupbox = QGroupBox("控制")
        layout_main.addWidget(groupbox)
        groupbox.setLayout(layout_line)

        cbox = QComboBox()
        cbox.addItems(["竖排日文","横排日文"])
        cbox.currentIndexChanged.connect(lambda index: self.on_combobox_changed(index))
        layout_line.addWidget(cbox)

        # 按钮: 截图
        btn_start = QPushButton("截图")
        btn_start.clicked.connect(self.on_click_start)
        layout_line.addWidget(btn_start)

        # 按钮: 重新翻译
        btn_new = QPushButton("重新翻译")
        btn_new.clicked.connect(self.on_click_new)
        layout_line.addWidget(btn_new)

        # 文本区: 原文
        layout_line = QHBoxLayout()
        groupbox = QGroupBox("原文")
        layout_main.addWidget(groupbox)
        groupbox.setLayout(layout_line)

        self.raw_box = QTextEdit()
        self.raw_box.setMaximumHeight(100)
        self.raw_box.setMinimumWidth(400)
        self.raw_box.setFontPointSize(self.config["fontsize"])
        self.raw_box.setPlaceholderText("这里显示原文")
        self.raw_box.textChanged.connect(self.on_text_change)
        layout_line.addWidget(self.raw_box)

        # 文本区: 注音
        layout_line = QHBoxLayout()
        groupbox = QGroupBox("注音")
        layout_main.addWidget(groupbox)
        groupbox.setLayout(layout_line)

        self.roma_box = QTextEdit()
        self.roma_box.setMaximumHeight(100)
        self.roma_box.setMinimumWidth(400)
        self.roma_box.setFontPointSize(self.config["fontsize"])
        self.roma_box.setPlaceholderText("这里显示注音")
        layout_line.addWidget(self.roma_box)

        # 文本区: 翻译
        layout_line = QHBoxLayout()
        groupbox = QGroupBox("译文")
        layout_main.addWidget(groupbox)
        groupbox.setLayout(layout_line)

        self.trans_box = QTextEdit()
        self.trans_box.setMaximumHeight(100)
        self.trans_box.setMinimumWidth(400)
        self.trans_box.setFontPointSize(self.config["fontsize"])
        self.trans_box.setPlaceholderText("这里显示译文")
        layout_line.addWidget(self.trans_box)

        # 主体布局
        widget = QWidget()
        widget.setLayout(layout_main)
        self.setCentralWidget(widget)

    def on_combobox_changed(self,index):
        '''下拉框: 选择语言'''
        if index == 0:
            self.config["target"] = "jpn_vert"
        elif index ==1:
            self.config["target"] = "jpn"

    def on_click_start(self):
        '''按钮: 启动截图'''
        ats = AutoTrans(self.config)
        ats.startShot()
        self.text["raw"] = ats.get_text(self.config["save_path"], self.config["target"])
        self.raw_box.setText(self.text["raw"])
        self.text["romaji"] = ats.get_romaji(self.text["raw"])
        self.roma_box.setText(self.text["romaji"])
        self.text["translated"] = ats.get_translate(self.text["raw"],self.config["source"],self.config["translate"])
        self.trans_box.setText(self.text["translated"])
        # 删除图片
        os.remove(os.path.join(self.config["save_path"],"shot.jpg"))

    def on_click_new(self):
        '''按钮: 重新翻译'''
        ats = AutoTrans(self.config)
        self.text["romaji"] = ats.get_romaji(self.text["raw"])
        self.roma_box.setText(self.text["romaji"])
        self.text["translated"] = ats.get_translate(self.text["raw"],self.config["source"],self.config["translate"])
        self.trans_box.setText(self.text["translated"])

    def on_text_change(self):
        '''文本框: 原文'''
        self.text["raw"] = self.raw_box.toPlainText()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
