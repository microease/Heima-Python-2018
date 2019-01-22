#coding=utf-8
import os

folderName = input("请输入要批量删除重命名的文件夹：")
nameRename = input("请输入要批量删除的字符：")
dirList = os.listdir("./"+folderName+"/")

print(dirList)

for name in dirList:
	print (name)
	newName = name.replace(nameRename,'',2)
	os.rename("./"+folderName+"/"+name,"./"+folderName+"/"+newName)


print(dirList)
