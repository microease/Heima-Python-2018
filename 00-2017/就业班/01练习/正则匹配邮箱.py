#coding=utf-8
import re
mail1 = "microease@gmail.com"
mail2 = "173418535@qq.com"
mail3 = "microease@163.com"
mail4 = "sHG896tguhggyu@KHJGHJ.com"
pattern = r"(\w+)@(163|126|gmail|qq|\w+)\.(com|cn|net)$"
result = re.match(pattern,mail1)
result.group()
print(result.group())
print(result.group(1))
