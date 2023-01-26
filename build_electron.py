'''
2023.1.4
打包electron项目
'''

import os
import codecs
import markdown  # pip install markdown

# 打包时这里不再拷贝python文件夹,在vue.config.js中已经设置了包含python文件夹
# 注意dev时desktop_v2文件夹中不包含python文件夹,只有打包后才有,如果已经存在要手动删掉,否则vue.config.js中的复制不会生效


# 开发日志转化为html
if os.path.isfile("./desktop_v2/public/static/info/develop.html"):
    os.remove("./desktop_v2/public/static/info/develop.html")
input_file = codecs.open("./0-docs/develop.md", mode="r", encoding="utf-8")
text = input_file.read()
html = markdown.markdown(text)
output_file = codecs.open("./desktop_v2/public/static/info/develop.html", mode="w", encoding="utf-8")
output_file.write(html)

os.chdir("./desktop_v2")
os.system("npm run electron:build")


