'''
2022.3.1
yagmail发送邮件

用例：
send_mail("hello world")
'''

import yagmail

def send_mail(content):

    # yag = yagmail.SMTP(user='599509869@qq.com', password='gimepgtagoymbcff', host="smtp.qq.com", port="25")
    yag = yagmail.SMTP(user='599509869@qq.com', password='kozqfnlswdhnbddi', host="smtp.qq.com")
    yag.send('1970313791@qq.com', 'python report', content)

    # to = '1970313791@qq.com'
    # to2 = '599509869@qq.com'
    # subject = 'This is obviously the subject'
    # body = 'This is obviously the body'
    # html = '<a href="https://pypi.python.org/pypi/sky/">Click me!</a>'
    # img = '/local/file/bunny.png'
    # yag.send(to = [to,to2], subject = subject, contents = [body, html, img])


