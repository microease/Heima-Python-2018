#coding=utf-8
pstr = "hello world!"
def Strreplace(pstr,oldString,newString):
	result = pstr.split(oldString)
	return newString.join(result)
a = Strreplace(pstr,"world","huyankai")