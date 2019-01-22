#coding= utf-8
#0. 提示并获取要复制的文件名
name = input("请输入您要复制的文件名：")
#1.打开要复制的文件
f_read = open(name,"r")
#2. 创建一个新的文件，用来存储源文件的数据内容
findPosition = name.rfind(".")
newName = name[:findPosition] + "[复件]" + name[findPosition:]
f_write = open(newName,"w")
content = f_read.read()
print (content)
f_write.write(content)
f_read.close()
f_write.close()

#3. 复制
#第1种
#content = f_read.read()
#f_write.write(content)
#第2种
#for lineContent in f_read.readlines():
#    f_write.write(lineContent)
#第3种


#4. 关闭文件
