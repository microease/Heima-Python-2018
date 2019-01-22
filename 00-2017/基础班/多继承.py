#coding=utf-8
class Horse(object):
	def run():
		print("马儿跑的速度快")

class Donkey(object):
	def carry():
		print("驴子能拖物品")

class Mule(Horse,Donkey):
	pass

xiaoluozi = Mule()
xiaoluozi.run
xiaoluozi.carry

xiaoluozi