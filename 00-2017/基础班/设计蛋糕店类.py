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

class CakeStore(object):
	def taste(self,taste):
		if taste == "苹果":
			cake= AppleCake()
		if taste == "香蕉":
			cake = BananaCake()
		print("-----味道：%s-----"%cake.taste)

a = CakeStore()
a.taste("苹果")