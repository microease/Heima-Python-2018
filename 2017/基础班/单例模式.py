#coding=utf-8

class Singleton(object):
	__instance = None
	__first_init = False

	def __new__(cls,age,name):
		if not cls.__instance:
			cls.__instance = object.__new__(cls)
		return cls.__instance
	def __init(self,age,name):
		if not self.__first_init:
			self.age = age
			self.name = name
			Singleton.__first_init = True
		print(self)



a =Singleton(22,"胡炎凯")
b =Singleton(22,"胡炎凯")

print(a)
print(b)