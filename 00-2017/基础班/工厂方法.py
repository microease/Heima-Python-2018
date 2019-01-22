#coding=utf-8

class CarStore(object):
	#工厂方法：在父类中定义这个方法，不实现，具体的功能在子类当中实现
	def createCar(self,typeName):
		pass
	def order(self,typeName):
		self.car = self.createCar(typeName)
		self.car.move()
		self.car.stop()
class Audi(CarStore):
	def createCar(self,typeName):
		self.createCar