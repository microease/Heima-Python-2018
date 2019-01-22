#coding=utf-8
names = []
while True:
	print(names)
	print("-"*50)
	print("名字管理系统")
	print("1:添加一个新的名字")
	print("2:删除一个名字")
	print("3:修改一个名字")
	print("4:查询一个名字")
	print("5:退出系统")
	print("-"*50)
	num = int(input("请输入功能序号："))
	if num == 1:
		new_name = input("请输入新的名字：")
		names.append(new_name)
	elif num == 2:
		del_name = input("请输入您要删除的名字：")
		names.remove(del_name)
	elif num == 3:
		modify_name = input("请输入您要修改的名字:")
		modify_nameId = names.index(modify_name)
		modify_name2 = input("请输入您想要修改的名字：")
		names[modify_nameId] = modify_name2
	elif num == 4:
		find_name = input("请输入您要查询的名字：")
		if find_name in names:
			print("您输入的名字在列表中")
		else:
			print("查无此人！")
	elif num == 5:
		break
	else:
		print("您的输入有误，请重新输入。")