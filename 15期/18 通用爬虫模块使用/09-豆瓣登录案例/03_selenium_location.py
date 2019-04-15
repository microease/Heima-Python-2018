# coding:utf8
# Author :       huxiaoyi
# Date：         2019-04-15
# Time：         21:03
from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://accounts.douban.com/passport/login")

# driver.find_element_by_id()