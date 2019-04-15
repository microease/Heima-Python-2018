# coding:utf-8
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("http://www.douban.com/")
driver.find_element_by_class_name("account-tab-account").click()
driver.find_element_by_id("form_email").send_keys("microease@163.com")
driver.find_element_by_id("form_password").send_keys("huyankai1995521.")
time.sleep(3)
driver.find_element_by_class_name("bn_submit").click()
cookies = {i["name"]: i["value"] for i in driver.get_cookie()}
print(cookies)
