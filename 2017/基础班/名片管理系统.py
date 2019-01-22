#coding=utf-8
#author=huyankai
card_info = []
while True:
	print("*"*30)
	print("名片管理系统")
	print("1.添加一个名片")
	print("2.删除一个名片")
	print("3.修改一个名片")
	print("4.查询一个名片")
	print("5.打印所有名片")
	print("6:退出系统")
	print("*"*30)
	num = int(input("请输入您想要操作的序号："))
	if num == 1:
		new_name = input("请输入新的名字：")
		new_wechat = input("请输入新的微信：")
		new_phoneNumber = input("请输入新的电话：")
		new_address = input("请输入新的地址：")
		new_info = {}
		new_info['name'] = new_name
		new_info['wechat'] = new_wechat
		new_info['phoneNumber'] = new_phoneNumber
		new_info['address'] = new_address
		card_info.append(new_info)
		print(card_info)
	elif num == 2:
		del_name = input("请输入您要删除的名字：")
		for temp in card_info:
			if del_name == temp["name"]:
				card_info.remove(temp)
		print("您要删除的名片已经删除。")
	elif num == 3:
		change_name = input("请输入您要修改的名片名字：")
		for temp in card_info:
			if change_name == temp["name"]:
				changed_name = input("请问您要把这个名字修改为什么名字：")
				changed_wechat = input("请问您要把这个微信修改为什么微信：")
				changed_phoneNumber = input("请问您要把这个电话修改为什么电话：")
				changed_address = input("请问您要把这个地址修改为什么地址：")
				temp["name"] = changed_name
				temp["wechat"] = changed_wechat
				temp["phoneNumber"] = changed_phoneNumber
				temp["address"] = changed_address
				print("您要修改的名片已经修改，如下：")
				print(temp)
	elif num == 4:
		find_name = input("请输入您要查找的名字:")
		find_flag = 0
		for temp in card_info:
			if find_name == temp["name"]:
				print("您找的名字在字典中,具体信息如下：")
				print("名字\t微信\t电话\t地址")
				print("%s\t%s\t%s\t%s"%(temp['name'],temp['wechat'],temp['phoneNumber'],temp['address']))
				find_flag = 1
				break
		if find_flag == 0:
				print("查无此人")
	elif num == 5:
		print("名字\t微信\t电话\t地址")
		for temp in card_info:
			print("%s\t%s\t%s\t%s"%(temp['name'],temp['wechat'],temp['phoneNumber'],temp['address']))
	elif num == 6:
		break
	else:
		print("输入有误，请重新输入。")