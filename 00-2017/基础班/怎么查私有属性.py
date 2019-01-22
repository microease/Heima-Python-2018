#coding=utf-8
class People():
	def __init__(self,name,age):
		self.__name = name
		self.__age = age
	def getAge(self):
		return self.__age
laowang = People("老王",22)
dirpeople = dir(People)
age = laowang.getAge()

print(dirpeople)
print(getAge)