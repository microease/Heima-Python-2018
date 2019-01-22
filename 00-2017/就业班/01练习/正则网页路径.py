#coding=utf-8
import re
path = "http://www.wzxdm.com/coding/python/zhengzebiaodashi.html"
htmlCode = "<html><body><h1>hello,huyankai</h1></body></html>"
pattern = r"<(?P<html>.+)><(.+)><(.+)>.+</\3></\2></(?P=html)>"
result = re.match(pattern,htmlCode)
result.group()
print(result.group())
