'''
2023.3.16
宝可梦wiki爬虫,保存朱紫图鉴400只宝可梦序号+名称+属性到本地json文件
原理:网页里table写的很整齐,直接find就行,也没有反爬,页面源码存在page.html里了
'''

import requests
from bs4 import BeautifulSoup
import json

url = r'https://wiki.52poke.com/wiki/%E5%AE%9D%E5%8F%AF%E6%A2%A6%E5%88%97%E8%A1%A8%EF%BC%88%E6%8C%89%E5%B8%95%E5%BA%95%E4%BA%9A%E5%9B%BE%E9%89%B4%E7%BC%96%E5%8F%B7%EF%BC%89'

response = requests.get(url)
print("\nget response\n")
soup = BeautifulSoup(response.content, "html.parser")
# 8个table,每个table含50个宝可梦,共400
tables = soup.find_all("table", class_="roundy eplist bgl-帕底亚 bd-帕底亚")
data = []
for table in tables:
    # 遍历行
    trs = table.find_all("tr")
    # 遍历行中单元格
    for tr in trs:
        tds = tr.find_all("td")
        # 跳过表头
        if tds == []:
            continue
        # 第一格:帕迪亚编号
        pd_id = tds[0].text
        # 第二格:全国编号
        gb_id = tds[1].text
        # 第三格图片
        # 第四格名称
        name = tds[3].find("a").text
        # 第五格属性1
        typelist = [tds[4].find("a").text]
        # 第六格属性2,class为hide时没有属性2
        if not "hide" in tds[5].get("class"):
            typelist.append(tds[5].find("a").text)

        print(pd_id)
        data.append({'pd_id': pd_id, 'gb_id': gb_id, 'name': name, 'typelist': typelist})


with open("list.json", "w",encoding="utf-8") as f:
    f.write(json.dumps(data, ensure_ascii=False) + "\n")
