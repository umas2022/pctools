# 自助翻译.exe

- 环境初始化
```
pip install -r requirement.txt
```
- 官网安装tesseract,记下安装位置  
    https://tesseract-ocr.github.io/tessdoc/Installation.html
    - 记得勾选 Additional language data

- 手动配置pytesseract路径  
    - 首先找到pytesseract的安装位置 pip show pytesseract
    - 例如我是d:\s-code\self\pctools\venv\lib\site-packages\
    - 打开pytesseract.py,找到
    ```tesseract_cmd = 'tesseract'```
    改为你的tesseract安装位置,比如我是```tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'```

- 打包
    - 运行打包脚本  
    ```python build_qt.py```
    - pyinstaller命令无法自动包含pykakasi的db文件,所以
    - 记得把打包脚本里pykakasi\\data的路径改成你自己的



