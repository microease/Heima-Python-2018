#coding=utf-8
class People:
	def __init__(self,name):
		self.name = name
		self.hp = 100
		self.gun = None
	def __str__(self):
		return self.name + "剩余血量为：" + str(self.hp)
	def upperBullet(self,clip,bullet):
		clip.upper(bullet)
	def upperClip(self,gun,clip):
		gun.withClip(clip)
	def getgun(self,gun):
		self.gun = gun
	def shot(self,enemy):
		self.gun.shooting(enemy)
	def lossedhp(self,lethality):
		self.hp -= lethality
class Gun:
	def __init__(self):
		self.clip = None
	def __str__(self):
		if self.clip:
			return "当前没弹夹"
		else:
			return "当前有弹夹"
	def withClip(self,clip):
		if not self.clip:
			self.clip = clip
	def shooting(self,enemy):
		bullet = self.clip.lossbullet()
		if bullet:
			bullet.lossHp(enemy)
		else:
			("没子弹了")
class Clip:
	def __init__(self,amount):
		self.amount = amount
		self.clipList = []
	def __str__(self):
		return "弹夹当前的子弹数量为：" + str(len(self.clipList)) + "/" + str(self.amount)
	def upper(self,bullet):
		if len(self.clipList) < self.amount:
			self.clipList.append(bullet)
	def lossbullet(self):
		if len(self.clipList) > 0:
			bullet = self.clipList[-1]
			self.clipList.pop()
			return bullet
		else:
			return None
class Bullet:
	def __init__(self,lethality):
		self.lethality = lethality
	def lossHp(self,enemy):
		enemy.lossedhp(self.lethality)
laowang = People("老王")
print(laowang)
clip = Clip(20)
i = 0
while i < 10:
	bullet = Bullet(5)
	laowang.upperBullet(clip,bullet)
	i+=1
print(clip)
gun = Gun()
laowang.upperClip(gun,clip)
print(gun)
enemy = People("敌人")
laowang.getgun(gun)
laowang.shot(enemy)
print(enemy)
laowang.shot(enemy)
print(enemy)
laowang.shot(enemy)
print(enemy)
laowang.shot(enemy)
print(enemy)
laowang.shot(enemy)
print(enemy)
laowang.shot(enemy)
print(enemy)
laowang.shot(enemy)
print(enemy)
laowang.shot(enemy)
print(enemy)
laowang.shot(enemy)
print(enemy)
