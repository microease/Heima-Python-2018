#coding=utf-8
class Cake(object):
	def __init__(self,taste="默认"):
		self.taste = taste
class AppleCake(object):
	def __init__(self,taste="苹果味"):
		self.taste = taste
class BananaCake(object):
	def __init__(self,taste="香蕉味"):
		self.taste = taste
class CakeKitchen(object):
	def createCake(self, taste):
		if taste == "苹果":
			cake= AppleCake()
		elif taste == "香蕉":
			cake = BananaCake()
		elif taste == "默认":
			cake  = Cake()
		return cake
class CakeStore(object):
	def __init__(self):
		self.kitchen = CakeKitchen()
	def taste(self,taste):
		cake = self.kitchen.createCake(taste)
		print("-----味道：%s-----"%cake.taste)

a = CakeStore()
a.taste("苹果")
a.taste("香蕉")
a.taste("默认")