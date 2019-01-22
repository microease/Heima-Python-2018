#coding= utf-8
class SweetPotato:
	def __init__(self):
		self.cookedLevel = 0
		self.cookedString = "生的"
		self.condiments = []
	def cook(self,time):
		self.cookedLevel += time
		if self.cookedLevel > 8:
			self.cookedString = "烤焦了"
		elif self.cookedLevel > 5:
			self.cookedString = "烤熟了"
		elif self.cookedLevel > 3:
			self.cookedString = "半生不熟"
		else:
			self.cookedString = "生的"
	def addCondiments(self,addWhat):
		self.condiments.append(addWhat)

#重点：一定要先判断大于8，再判断是否大于5，再判断大于3，如果不这样的话，反过来，程序会满足多个if
	def __str__(self):
		msg = "地瓜的生熟程度为：" + self.cookedString
		msg += ",等级为" + str(self.cookedLevel)
		if len(self.condiments)>0:
			msg += ",加了这些佐料："
			for condiment in self.condiments:
				msg += condiment + "," 
			#msg = msg[:-1]
			msg = msg.strip(",")
		else:
			msg+= "，请添加调料"
		return msg
xiaodigua = SweetPotato()
xiaodigua.cook(1)
print(xiaodigua)
xiaodigua.cook(1)
print(xiaodigua)
xiaodigua.cook(1)
print(xiaodigua)
xiaodigua.cook(1)
print(xiaodigua)
xiaodigua.cook(1)
print(xiaodigua)
xiaodigua.cook(1)

xiaodigua.addCondiments("番茄酱")
print(xiaodigua)
xiaodigua.addCondiments("芥末酱")
print(xiaodigua)
xiaodigua.addCondiments("咖喱")
print(xiaodigua)
xiaodigua.addCondiments("孜然")

print(xiaodigua)