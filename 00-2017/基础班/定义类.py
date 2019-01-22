class Cat:

	def eat(self):
		print("吃")
	def drink(self):
		print("喝")
	def sleep(self):
		print("睡觉")

xiaohuamao = Cat()
xiaohuamao.eat()
xiaohuamao.drink()
xiaohuamao.sleep()

xiaohuamao.color = "花色"
xiaohuamao.weight = "5kg"
a = xiaohuamao.color
print(a)