#coding=utf-8
namelist  = ["zhudan","huyankai"]
chaxun = input("请输入您要查询的名字：")
findFlag = 0
for name in namelist:
	if name==chaxun:
		findFlag = 1
if findFlag ==1:
	print("找到了")
else:
	print("没找到")
