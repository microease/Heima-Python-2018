#coding=utf-8
import os
from multiprocessing import Pool,Manager

def copyFiles(name,oldDirName,newDirName,queue):
	fr = open(oldDirName+"/"+name)
	fw = open(newDirName+"/"+name,"w")
	content = fr.read()
	fw.write(content)
	fr.close()
	fw.close()
	queue.put(name)
def main():
	#创建新的文件夹，以原来的文件夹-复件命名
	oldDirName = input("请输入您要复制的文件夹名字：")
	newDirName = oldDirName +"-复件"
	#print(newDirName)
	os.mkdir(newDirName)

	#获取原来文件夹中的所有文件名字
	fileNames = os.listdir(oldDirName)
	#print(fileNames)

	#使用多进程的方式复制所有文件到新的文件夹
	pool = Pool(5)
	queue = Manager().Queue()
	for name in fileNames:
		pool.apply_async(copyFiles,args=(name,oldDirName,newDirName,queue))
	num = 0
	allNum = len(fileNames)
	while num < allNum:
		queue.get()
		num += 1
		copyRate = num/allNum
		print("\rcopy的进度为：%.2f%%"%(copyRate*100),end="")
if __name__ == "__main__":
	main()