from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# 移动百度版
driver = webdriver.Chrome()
driver.get("http://m.baidu.com/")
driver.maximize_window()
# 搜索词并返回搜索结果列表
driver.find_element_by_id("index-kw").send_keys("深圳阳光医院内眦开大")
driver.find_element_by_id("index-kw").send_keys(Keys.RETURN)
# xpath找到所有链接
res = driver.find_elements_by_xpath("//header/div/a")
for i in res:
    t = i.find_element_by_xpath("h3/span")
    print(t.text, type(t.text))
    if u'深圳阳光整形美容医院' in t.text:  # 判断标题中是否有深圳阳光整形美容医院，如果有则点击
        print("找到目标！")
        t.click()

time.sleep(3)

# driver.quit()
