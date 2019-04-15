from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get("http://www.baidu.com/")
driver.find_element_by_id("kw").send_keys("深圳阳光整形美容医院")
driver.find_element_by_id("su").click()
time.sleep(3)

# driver.quit()
