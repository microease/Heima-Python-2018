#coding=utf-8
name = ["huyankai","zhudan"]
while True:
	print("*"*30)
	print("欢迎使用系统")
	print("1：添加新名字")
	print("2：删除一个名字")
	print("3：修改一个名字")
	print("4：查询一个名字")
	print("5：遍历所有的名字")
	print("0：退出系统")
	print("*"*30)

	key = input("请输入您想要的选项：")


	if key=="1":
		insertName = input("请输入您要添加的名字：")
		name.append(insertName)
		print(name)
	elif key=="2":
		shanchu = input("请输入您要删除的名字：")
		#需要增加个新功能，判断用户输入的在不在列表里面，不在 报错
		name.remove('%s'%shanchu)
		print(name)
	elif key=="3":
		print(name)
		xiugai = input("请输入您要修改下标和名字，用逗号隔开，查询下标请按4：")
		name[] = ''
#有问题，此处待修改
		print(name)

	elif key=="4":
		chaxun = input("请输入您想查询的名字：")
		chaxunjieguo = name.count('%s'%chaxun)
		print(chaxunjieguo)
		print(name)
#有问题，此处待修改
	elif key=="5":
		print(name)

	elif key=="0":
		break
	else:
		print("非法输入，请重新输入！")