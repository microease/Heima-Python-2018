class Cat(object):
	num = 0
	def __init__(self):
		self.age = 1
	def run(self):
		print("猫在跑")

mao = Cat()
print (Cat.num+=1)
mao2 = Cat()
print(mao2.num)