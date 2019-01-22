#coding=utf-8
#auther:microease
studentInfos = [{'name': 'huyankai', 'sex': '男', 'phoneNumber': '15172332476'}]
#有重复代码，需要完善

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
		newName = input("请输入新学生的名字：")
		newSex = input("请输入新学生的性别：")
		newPhoneNumber = input("请输入新学生的电话：")
		newStudentInfos ={}
		newStudentInfos['name'] =newName
		newStudentInfos['sex'] =newSex
		newStudentInfos['phoneNumber'] =newPhoneNumber
		studentInfos.append(newStudentInfos)
		print(studentInfos)
	elif key=="2":
		shanchu = input("请输入您要删除的名字：")
		#需要增加个新功能，判断用户输入的在不在列表里面，不在 报错
		name.remove('%s'%shanchu)
		print(name)
	elif key=="3":
		print(studentInfos)
		studentID = int(input("请输入您要修改的学生序号："))
		#此处加int是因为下面发生计算，所以类型不能为字符，必须为数字
		newName = input("请输入新学生的名字：")
		newSex = input("请输入新学生的性别：")
		newPhoneNumber = input("请输入新学生的电话：")
		studentInfos[studentID-1]['name'] = newName
		studentInfos[studentID-1]['sex'] = newSex
		studentInfos[studentID-1]['PhoneNumber'] = newPhoneNumber
		#此处id减去1是因为下标从0开始，而序号从1开始
		print(studentInfos)

	elif key=="4":
		chaxun = input("请输入您想查询的名字：")
		chaxunjieguo = name.count('%s'%chaxun)
		print(chaxunjieguo)
		#此处待完善
	elif key=="5":
		print("*"*30)
		print("学生的信息如下：")
		print("序号 姓名 性别 电话")
		i = 1
		for tempInfo in studentInfos:
			print("%d  %s  %s  %s"%(i,tempInfo['name'],tempInfo['sex'],tempInfo['phoneNumber']))
		print("*"*30)
		i+=1


	elif key=="0":
		break
	else:
		print("非法输入，请重新输入！")