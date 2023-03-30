import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QTextEdit, QWidget, QVBoxLayout

class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # 创建 QTextEdit
        self.text_edit = QTextEdit()
        self.text_edit.setLineWrapMode(QTextEdit.WidgetWidth)

        # 设置横向滚动条
        self.text_edit.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)

        # 添加 QTextEdit 到主窗口
        self.setCentralWidget(self.text_edit)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MyMainWindow()
    main_window.show()
    sys.exit(app.exec())
