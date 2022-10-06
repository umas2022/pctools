'''
create: 2022.10.5
bookwalker漫画《夜夜夜》爬虫
思路：1.登录页登录 2.home页点击进入漫画
使用修改window.navigator.webdriver的方式反爬

目前问题是似乎ip被ban了，后面几次需要进行谷歌人机认证，再后来直接白屏
'''

import sys
sys.path.append("..")
from utils_logger.log import logger_re as logger

import requests
from selenium import webdriver  # pip install selenium
from selenium.webdriver.common.by import By
from selenium.webdriver import ChromeOptions


url_top = "https://bookwalker.jp/top/"
url_login = "https://member.bookwalker.jp/app/03/login"
url_home = "https://bookwalker.jp/de57a21d74-d918-47df-b22f-b3a9454e59df/"
url_manga = "https://viewer.bookwalker.jp/03/20/viewer.html?cid=57a21d74-d918-47df-b22f-b3a9454e59df&cty=1"

'''实例化浏览器'''
# 反爬：消除window.navigator.webdriver
option = ChromeOptions()
option.add_experimental_option('excludeSwitches',['enable-automation'])
option.add_argument("--disable-blink-features=AutomationControlled")
# 实例化谷歌
chrome_driver = r"D:\p-tools\chromedriver\chromedriver106.exe"
driver = webdriver.Chrome(executable_path=chrome_driver,options=option)


wait_here = input(" next : login")
print("start ...")


'''手动登录'''
driver.get(url=url_login)
driver.implicitly_wait(30)
driver.find_element(By.CSS_SELECTOR, 'input[name="j_username"').send_keys("1970313791@qq.com")
driver.find_element(By.CSS_SELECTOR, 'input[name="j_password"').send_keys("umas1970")
driver.find_element(By.CSS_SELECTOR, 'button[class="g-recaptcha c-btn--forward"').click()
driver.implicitly_wait(30)

wait_here = input(" next : homepage")
print("start ...")


'''进入home页打开漫画'''
new_tap = "window.open('%s')" % url_home
driver.execute_script(new_tap)
driver.implicitly_wait(30)
driver.find_element(By.CSS_SELECTOR, 'a[class="bw_btn bw_btn-login"').click()


# driver.switch_to.window(driver.window_handles[0])

# driver.get(url=url_top)
# driver.get(url=url_manga)
# driver.refresh()

# chrome.get(url=url1)

wait_here = input()
driver.quit()
