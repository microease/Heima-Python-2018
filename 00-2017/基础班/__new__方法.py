#coding=utf-8
class Test(object):
	def __init__(self):
		self.num =100
		print("测试")
		print(self)
	def __str__(self):
		return "xxxxxx"
	def __new__(cls):
		print("--new--")
		print(cls)
		return super().__new__(cls)
a = Test()

print(a.num)

print(a)