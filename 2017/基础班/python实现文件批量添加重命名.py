#coding=utf-8
import os

folderName = input("请输入要批量添加重命名的文件夹")
dirList = os.listdir("./"+folderName+"/")

print(dirList)

for name in dirList:
	print (name)
	os.rename("./"+folderName+"/"+name,"./"+folderName+"/"+"[重命名]-"+name)

print(dirList)
