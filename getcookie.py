from selenium import webdriver
import time
import json
driver = webdriver.Chrome()
driver.get("https://login.taobao.com/member/login.jhtml?spm=a21bo.2017.201864-2.d1.5af911d9i0gY3y&f=top&redirectURL=http%3A%2F%2Fwww.taobao.com%2F")
time.sleep(20)
with open('cookies.txt', 'w') as f:
    # 将cookies保存为json格式
    f.write(json.dumps(driver.get_cookies()))

driver.close()
