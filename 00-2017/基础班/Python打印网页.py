#coding=utf8

import pip

import requests
import json
from bs4 import BeautifulSoup
response = requests.get('http://imgout.ph.126.net/5589800')
print(response) # 状态码