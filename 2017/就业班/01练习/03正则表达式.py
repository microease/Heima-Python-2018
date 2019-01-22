#coding=utf-8
import re
#result = re.match(正则表达式，要匹配的字符串)
#result.group()用来判断字符串是否符合正则表达式规则
#案例：正则表达式判断手机号
s1= "15172332476"
pattern = r"^1[3578]\d{9}$"
result = re.match(pattern,s1)
result.group()
print("手机号:" + result.group())