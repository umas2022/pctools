'''
2023.1.3
给老张写的misumi爬虫
思路：
    1. 直接拼接链接
    2. 加入并行功能
'''

import os
import time
import requests  # pip install requests
import threading


# pdf保存位置
save_path = r"D:\s-workspace\crawler_save"
# 并行数
th_total = 20
# 起始页码
start_page = 1
# 总页数
total_page = 38

# 系统参数
th_ready_flag = 0
all_done_flag = False
time_start = time.time()

# 子线程函数：保存pdf


def get_img(count):
    global time_start
    time_cost = int(time.time() - time_start)
    time_left = int(time_cost / (count + 1) * (total_page - count - 1))
    print("current crawl: %d , remaining: %s s" % (count, time_left))
    num = str(count).zfill(4)
    img_re = requests.get("https://cn.c.misumi.com.cn/book/sh2_2019_msm_press_01/pdf/%s.pdf" % num)
    # img_re = requests.get("https://www.misumi.com.cn/linked/archive/ebook/fabiaozhunpin202210/pdf/qian_%s.pdf" % num)
    file_name = str(count) + ".pdf"
    full_path = os.path.join(save_path, file_name)
    with open(full_path, "wb") as f:
        f.write(img_re.content)
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
