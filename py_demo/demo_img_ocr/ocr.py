# 导入pytesseract库
import pytesseract # pip install pytesseract
# 导入PIL库
from PIL import Image

# 打开图片文件
img = Image.open('./data/test_jp2.jpg') # 这个图片识别效果不好
# 使用pytesseract识别图片中的文字，并返回一个字符串
# text = pytesseract.image_to_string(img, lang='chi_sim') # 简体中文(包含英文也支持)
text = pytesseract.image_to_string(img, lang='jpn_vert')  # 日文竖排,右到左(漫画排版)

# 将字符串按换行符分割，并转换为一个列表
print(text.split('\n'))

# 删除空格并拼接成一行
print(text.replace(" ","").replace("\n",""))
