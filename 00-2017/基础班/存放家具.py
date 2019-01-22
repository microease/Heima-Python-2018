#coding=utf-8
class Home:
	def __init__(self,area):
		self.area = area#房间剩余的可用面积
		self.furniture = []
		self.light = "on"
	def __str__(self):
		msg = "家当前可用面积为：" + str(self.area)
		if len(self.furniture)>0:
			msg += "\t"
			msg += "家当前的物品有："
			#msg += ",".join(self.furniture)
			for temp in self.furniture:
			#此处是难点，为什么能写temp.name呢？furniture是一个列表，在此时temp是一个对象，对象.name就可以调用下面输出的name名
				msg += temp.getName() + ","
			'''
			else:
				msg += "没有任何东西。"
			'''
			msg = msg[:-1]
			if self.light == "on":
				msg += "\t" + "当前灯是开着的，房子和所有的物品都是可见的"
			else:
				msg += "\t" + "当前灯是关着的，什么都看不到呢"
		return msg
	def addfurniture(self,item):
		needArea = item.getArea()
		if self.area > needArea:
			self.furniture.append(item)
			self.area -= needArea
	#关灯
	def turnoff(self):
		self.light = "off"
		for temp in self.furniture:
			temp.turnoff()
class Bed:
	def __init__(self,name,area):
		self.name = name
		self.area = area
		self.light = "on"
	def __str__(self):
		msg = self.name + "的面积为：" +str(self.area)
		msg += "当前的可见程度为：" + self.light
		return msg
	def getName(self):
		return self.name
	def getArea(self):
		return self.area
	def turnoff(self):
		self.light = "off"
		return self.light



#创建一个家对象
home = Home(120)
print(home)
bed = Bed("宜家北欧床",4)
home.addfurniture(bed)

print(bed)
print(home)
bed2 = Bed("高低床",4)
home.addfurniture(bed2)
print(bed2)
print(home)
print("===========分割线===========")
home.turnoff()
print(bed)
print(bed2)
