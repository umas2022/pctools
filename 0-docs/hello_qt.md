# python+QT入门记录


## 基本操作
- 打包exe
```
pip install pyinstaller
pyinstaller.exe -F -w .\window.py

-F	打包一个exe文件
-D	打包多个文件，在dist中生成很多依赖文件
-d	产生debug版本的可执行文件
-w	程序启动不打开命令行
-n、–name	指定名称打包程序名称(默认值为脚本的基本名称)
-i	指定.exe程序的图标
--add-data="源地址;目标地址"。 windows以;分割，linux以:分割
```
- 为了避免静态资源路径加载错误,可以使用一个绝对路径函数
```python
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = os.path.dirname(os.path.realpath(__file__))
    return os.path.join(base_path, relative_path)
```

## 基本框架

- 参考  
https://www.pythonguis.com/tutorials/pyqt6-creating-your-first-window/


- 简单窗口  

```python
import sys

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton


# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("电脑配件qt版")
        button = QPushButton("Press Me!")

        self.setFixedSize(QSize(800, 600))
        self.setCentralWidget(button)

# You need one (and only one) QApplication instance per application.
# Pass in sys.argv to allow command line arguments for your app.
# If you know you won't use command line arguments QApplication([]) works too.
app = QApplication(sys.argv)

window = MainWindow()
window.show()  # IMPORTANT!!!!! Windows are hidden by default.

# Start the event loop.
app.exec()
# Your application won't reach here until you exit and the event
# loop has stopped.
```

## 常用函数和功能

- 窗口名
```python
self.setWindowTitle("My App")
```
- 窗口图标
```python
self.setWindowIcon(QtGui.QIcon("./data/img/mati_ei_256.ico"))
```

- 窗口大小 
```python
self.setFixedSize(QSize(800, 600))
```

- 文本
```python
self.label = QLabel()
self.label.setText()
```


- 按钮
```python
self.button = QPushButton("Press Me!")
self.button.clicked.connect(self.the_button_was_clicked)
```

- 输入框
```python
self.input = QLineEdit()
self.input.textChanged.connect(self.label.setText)
```

- 其他的一些小组件
```python
QCheckbox	    一个复选框
QComboBox	    下拉列表框
QDateEdit	    用于编辑日期和日期时间
QDateTimeEdit	用于编辑日期和日期时间
QDial	        可旋转表盘
QDoubleSpinbox	浮点数的数字微调器
QFontComboBox	字体列表
QLCDNumber	    一个相当丑陋的LCD显示屏
QLabel	        只是一个标签，而不是交互式的
QLineEdit	    输入一行文本
QProgressBar	进度条
QPushButton	    一个按钮
QRadioButton	切换集，只有一个活动项
QSlider	        滑块
QSpinBox	    整数微调器
QTimeEdit	    对于编辑时间
```


- 事件
```python
mouseMoveEvent	鼠标移动
mousePressEvent	按下鼠标按钮
mouseReleaseEvent	释放鼠标按钮
mouseDoubleClickEvent	检测到双击

def mouseMoveEvent(self, e):
    self.label.setText("mouseMoveEvent")
```

## 布局

- 基本布局4种
```python
QHBoxLayout	线性水平布局
QVBoxLayout	线性垂直布局
QGridLayout	在可转位网格 XxY 中
QStackedLayout	堆叠 （z） 彼此前面
```


- 线性水平和垂直布局例子  
```python
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget,QVBoxLayout,QHBoxLayout
from PyQt6.QtGui import QPalette, QColor


class Color(QWidget):

    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(palette)

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("My App")

        layout1 = QHBoxLayout()
        layout2 = QVBoxLayout()
        layout3 = QVBoxLayout()

        layout1.setContentsMargins(0,0,0,0)
        layout1.setSpacing(20)

        layout2.addWidget(Color('red'))
        layout2.addWidget(Color('yellow'))
        layout2.addWidget(Color('purple'))

        layout1.addLayout( layout2 )

        layout1.addWidget(Color('green'))

        layout3.addWidget(Color('red'))
        layout3.addWidget(Color('purple'))

        layout1.addLayout( layout3 )

        widget = QWidget()
        widget.setLayout(layout1)
        self.setCentralWidget(widget)



app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
```

```python

```

