#coding=utf-8
class People():
	def __init__(self,name,age):
		self.__name = name
		self.__age = age
	def setNewAge(self,newAge):
		if newAge>0 and newAge <=100:
			self.__age = newAge
	def getAge(self):
		return self.__age
	def __del__(self):
		print("---------------删除")
laowang = People("老王",22)
laowang.setNewAge(21)
age = laowang.getAge()
print(age)
laozhang = laowang
print(laowang)
del laowang
print(laozhang)