from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

options = webdriver.ChromeOptions()
options.add_argument('lang=zh_CN.UTF-8')
options.add_argument('user-agent="Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1"')


# 移动百度版

driver = webdriver.Chrome(chrome_options=options)


driver.get("http://m.baidu.com/")
# driver.maximize_window()
# 搜索词并返回搜索结果列表
driver.find_element_by_id("index-kw").send_keys("深圳阳光医院")
driver.find_element_by_id("index-kw").send_keys(Keys.RETURN)
# xpath找到所有链接
# res = driver.find_elements_by_xpath("//header/div/a")

# 第一版：手机自然搜索
# for i in res:
#     t = i.find_element_by_xpath("/span")
#     print(t.text, type(t.text))
#     if u'深圳阳光整形美容医院' in t.text:  # 判断标题中是否有深圳阳光整形美容医院，如果有则点击
#         print("找到目标！")
#         t.click()
# 第二版：竞价：
# xpath找到所有的广告
res = driver.find_elements_by_xpath("//div[@class=\"ec_urlline\"]/a[@class=\"ec-showurl-line \"]")

for i in res:
    i.send_keys(Keys.ENTER)

time.sleep(15)

# driver.quit()
