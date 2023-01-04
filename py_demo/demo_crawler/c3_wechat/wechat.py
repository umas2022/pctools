'''
2023.1.3
给老张写的微信图片爬虫
思路：
    1. 网页源码比较简单,所有图片都在<img>的src里面给出了url
    2. 所以只需要遍历到所有src依次下载就好了
    3. 网页没有任何反爬机制,可以直接使用request
    4. 图片质量比较差,加锐化,降噪
    5. 加入并行
'''

import os
import threading
import time
import requests  # pip install requests
from bs4 import BeautifulSoup  # pip install beautifulsoup4
from PIL import Image, ImageEnhance  # pip install pillow
import cv2  # pip install opencv-python

# 图片保存位置
save_path = r"D:\s-workspace\crawler_save"
# 网页url
page_url = "https://mp.weixin.qq.com/s?__biz=MzU5OTYxODY1Mw==&mid=2247530873&idx=2&sn=5168702363787c5752ba1d7fc7c7fe86&chksm=feb01c4bc9c7955d4ed2cdd9c0348c47fba50dff5dc13ccfa0fd83634bfe7b8c704e6639c006&scene=21#wechat_redirect"
# 并行数
th_total = 10

'''爬图片'''
def get_img(img_url, count):
    img_re = requests.get(img_url)
    jpg_name = str(count) + ".jpg"
    full_path = os.path.join(save_path, jpg_name)
    with open(full_path, "wb") as f:
        f.write(img_re.content)


page_re = requests.get(page_url)
page_soup = BeautifulSoup(page_re.text, "lxml")
img_tag_list = page_soup.find_all("img", {"class": "rich_pages"})
count = 1
for img_tag in img_tag_list:
    print("current crawl: %d" % count)
    img_url = img_tag["data-src"]
    th_img = threading.Thread(target=get_img, args=[img_url, count], daemon=True)
    th_img.start()
    count += 1
    if count % th_total ==0:
        time.sleep(3)


# '''图片处理'''
# 锐化
# sharp_factor = 1
# for root, dirs, files in os.walk(save_path):
#     for fileName in files:
#         print("sharpen: %s" % fileName)
#         full_path = os.path.join(root, fileName)
#         img = Image.open(full_path)
#         img = img.convert('RGB')
#         enhancer = ImageEnhance.Sharpness(img)
#         im_s = enhancer.enhance(sharp_factor)
#         im_s.save(full_path)

# # 降噪
# filter_factor = 20
# for root, dirs, files in os.walk(save_path):
#     for fileName in files:
#         print("denoising: %s" % fileName)
#         full_path = os.path.join(root, fileName)
#         img = cv2.imread(full_path)
#         img_dst = cv2.fastNlMeansDenoising(img,None,filter_factor,filter_factor)
#         cv2.imwrite(full_path,img_dst)
