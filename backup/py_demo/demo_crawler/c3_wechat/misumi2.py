'''
2023.1.3
给老张写的misumi爬虫
思路：
    1. 直接拼接链接
    2. 加入并行功能
    3. 2022版misumi手册,疑似有反爬机制
    
    斗不过这个反爬,放弃了
'''

import os
import time
import requests  # pip install requests
import threading
import random
# 伪装UserAgent
from fake_useragent import UserAgent  # pip install fake-useragent


# pdf保存位置
save_path = r"D:\s-workspace\crawler_save"
# 并行数
th_total = 20
# 起始页码
start_page = 1
# 总页数
total_page = 5

# 系统参数
th_ready_flag = 0
all_done_flag = False
time_start = time.time()

ua = UserAgent()
headers = {
    # ua.random 表示的时 随机生成一个User-Agent，这样的话我们就能有很多个 User-Agent 来使用，
    # 就不用再担心 被封ip了。
    "User-Agent": ua.random,
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "DNT": "1",
    "Connection": "cloes"
}

# 子线程函数：保存pdf


def get_img(count):
    global time_start
    time_cost = int(time.time() - time_start)
    time_left = int(time_cost / (count + 1) * (total_page - count - 1))
    print("current crawl: %d/%d , remaining: %s s" % (count, total_page, time_left))
    num = str(count).zfill(4)
    global headers
    file_re = requests.get("https://www.misumi.com.cn/linked/archive/ebook/fabiaozhunpin202210/pdf/qian_%s.pdf" % num, headers=headers)
    file_name = str(count) + ".pdf"
    full_path = os.path.join(save_path, file_name)
    with open(full_path, "wb") as f:
        f.write(file_re.content)
        global th_ready_flag
        global all_done_flag
        th_ready_flag += 1
        if count == total_page + start_page - 1:
            all_done_flag = True


# 开始处理
for count in range(start_page - 1, start_page - 1 + total_page):
    count += 1
    th_img = threading.Thread(target=get_img, args=[count], daemon=True)
    th_img.start()
    if count % th_total == 0:
        th_ready_flag = 0
        while th_ready_flag < th_total:
            time.sleep(1)

# 等待全部完成
while not all_done_flag:
    time.sleep(1)
