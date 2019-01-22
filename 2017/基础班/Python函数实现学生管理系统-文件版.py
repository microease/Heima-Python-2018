#coding=utf-8
#auther:microease
studentInfos = [{'name': 'huyankai', 'sex': '男', 'phoneNumber': '15172332476'}]
newName = ""
newSex = ""
newPhoneNumber = ""
'''
IndentationError: unindent does not match any outer indentation level
出现这个错误是因为缩进有问题
'''
def printinfo():
	print("*"*30)
	print("欢迎使用系统")
	print("1：添加新名字")
	print("2：删除一个名字（使用本功能前，请使用5选项查询所有的学生序号）")
	print("3：修改一个名字（使用本功能前，请使用5选项查询所有的学生序号）")
	print("4：查询一个名字（使用本功能前，请使用5选项查询所有的学生序号）")
	print("5：遍历所有的名字")
	print("6：保存数据")
	print("0：退出系统")
	print("*"*30)
def getStudentInfo():
	global newName
	global newSex
	global newPhoneNumber
	newName = input("请输入新学生的名字：")
	newSex = input("请输入新学生的性别：")
	newPhoneNumber = input("请输入新学生的电话：")
def addStudentInfo():
	getStudentInfo()
	newStudentInfos ={}
	newStudentInfos['name'] =newName
	newStudentInfos['sex'] =newSex
	newStudentInfos['phoneNumber'] =newPhoneNumber
	studentInfos.append(newStudentInfos)
def modifyStudentInfo():
		studentID = int(input("请输入您要修改的学生序号："))
		#此处加int是因为下面发生计算，所以类型不能为字符，必须为数字
		getStudentInfo()
		studentInfos[studentID-1]['name'] = newName
		studentInfos[studentID-1]['sex'] = newSex
		studentInfos[studentID-1]['PhoneNumber'] = newPhoneNumber
def deleteStudentInfo():
		studentID = int(input("请输入您要修改的学生序号："))
		#此处加int是因为下面发生计算，所以类型不能为字符，必须为数字
		del studentInfos[studentID-1]
def findStudentInfo():
	studentID = int(input("请输入您要修改的学生序号："))
	print("*"*30)
	print("学生的信息如下：")
	print("序号 姓名 性别 电话")
	for tempInfo in studentInfos:
		print("%s  %s  %s"%(tempInfo['name'],tempInfo['sex'],tempInfo['phoneNumber']))
	print("*"*30)
def save2file():
	backupfile = input("请输入您要保存或者打开的文件名：")
	f = open(backupfile,"w")
	
	f.write(str(studentInfos))
	f.close
def recoverData():
	global studentInfos
	backupfile = input("请输入您要保存或者打开的文件名：")
	f = open(backupfile)
	content = f.read()
	studentInfos = eval(content)
	print(studentInfos)
	f.close()
def main():
	recoverData()
	while True:
		printinfo()
		key = input("请输入您想要的选项：")
		if key=="1":
			addStudentInfo()
			print(studentInfos)
			save2file()
		elif key=="2":
			deleteStudentInfo()
			print(studentInfos)
			save2file()
		elif key=="3":
			print(studentInfos)
			modifyStudentInfo()
			print(studentInfos)
			save2file()
		elif key=="4":
			findStudentInfo()
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
		elif key=="6":
			save2file()
		elif key=="0":
			break
		else:
			print("非法输入，请重新输入！")
main()