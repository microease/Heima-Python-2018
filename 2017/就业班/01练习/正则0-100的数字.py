#coding=utf-8
import re
#匹配0-100之间的数字，包括0和100
number1 = "0"
number2 = "9"
number3 = "99"
number4 = "100"
number5 = "80"
number6 = "200"
number7 = "-100"
pattern = r"^[1-9]?\d{0,2}$"
result = re.match(pattern,number7)
result.group()
print(result.group())
