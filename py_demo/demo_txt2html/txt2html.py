'''
2023.3.7
txt转html
老张把chatgpt的记录保存成txt了,想用html格式挂在github.io上
'''

import os


def get_file(path_in):
    '''文件遍历'''
    for root, dirs, files in os.walk(path_in):
        for fileName in files:
            full_path = os.path.normpath(os.path.join(root, fileName))
            if os.path.splitext(full_path)[-1] == ".txt":
                yield (full_path, os.path.splitext(full_path)[0])


for full_path, file_name in get_file("./"):
    html_file = file_name + ".html"
    with open(html_file, "w") as html_obj:
        # 写头
        html_obj.write('''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Document</title>
        </head>
        <body>\n''')

        # 写内容
        with open(full_path, 'r') as txt_obj:
            line = txt_obj.readline()
            while line:
                html_obj.write("<p>" + line.strip() + "</p>\n")
                line = txt_obj.readline()

        # 写尾
        html_obj.write('''
        </body>
        <style>
            p {
                font-family: 'Times New Roman', Times, serif;
                font-size: 50pt;
            }
        </style>
        </html>''')
