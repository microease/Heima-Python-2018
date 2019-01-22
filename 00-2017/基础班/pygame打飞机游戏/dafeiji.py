#coding=utf-8
import pygame
import random
#导入pygame模块
from pygame.locals import *
#导入检测键盘的子模块
import time
class Base(object):
    def __init__(self,screen,planeName):
        self.planeName = planeName 
        self.screen = screen
    def display(self):
        self.screen.blit(self.imageFile,(self.x,self.y))
class PublicAircraft(Base):
    def __init__(self,screen,planeName):
        super().__init__(screen,planeName)
        self.imageFile = pygame.image.load(self.imagePath).convert()
        self.bulletList = []
    def display(self):
        super().display()
        for bullet in self.bulletList:
            bullet.display()
            bullet.move()
        needDelBullet = []
        for i in self.bulletList:
            if i.judge():
                needDelBullet.append(i)
        for i in needDelBullet:
            self.bulletList.remove(i)
    def shoot(self):
        newBullet = PublicBullet(self.x,self.y,self.screen,self.planeName)
        self.bulletList.append(newBullet)
class PublicBullet(Base):
    def __init__(self,x,y,screen,planeName):
        super().__init__(screen,planeName)
        #定义默认值，接收从飞机类中传过来的参数
        if planeName == "aircraft":
            self.x = x+40
            self.y = y-20
            imagePath = "./feiji/bullet-3.gif"
        elif planeName == "enemy":
            self.x = x+30
            self.y = y+30
            imagePath = "./feiji/bullet-1.gif"
        self.imageFile = pygame.image.load(imagePath).convert()
    def move(self):
        if self.planeName == "aircraft":
            self.y -= 2
        if self.planeName == "enemy":
            self.y += 2
    def judge(self):
        if self.y<0 or self.y>890:
            return True
        else:
            return False
class HeroAircraft(PublicAircraft):
    def __init__(self,screen,planeName):
        self.x = 250
        self.y = 600
        self.imagePath = "./feiji/hero.gif"
        super().__init__(screen,planeName)
    def moveLeft(self):
        self.x -= 20
    def moveRight(self):
        self.x += 20
    def moveUp(self):
        self.y -= 20
    def moveDown(self):
        self.y += 20
class EnemyAircraft(PublicAircraft):
    def __init__(self,screen,planeName):
        self.x = 0
        self.y = 0
        self.imagePath = "./feiji/enemy-1.gif"
        super().__init__(screen,planeName)
        self.direction = "right"
    def move(self):
        if self.direction == "right":
            self.x += 2
        elif self.direction == "left":
            self.x -= 2
        if self.x > 480-50:
            self.direction = "left"
        elif self.x < 0:
            self.direction = "right"
    def shoot(self):
        num = random.randint(1,5)
        if num == 5:
            super().shoot()
            print("敌人射子弹")
if __name__ == '__main__':
#__name__变量，判断该模块是作为脚本被执行，还是被调用，当直接执行的时候，就是main，在被别人调用的时候，就是name
    screen = pygame.display.set_mode((480,980),0,32)
#设置屏幕，0,32是默认值
    bgImageFile = './feiji/background.png'
#导入图片
    background = pygame.image.load(bgImageFile).convert()
#背景用background保存
    aircraft = HeroAircraft(screen,"aircraft")
    enemy = EnemyAircraft(screen,"enemy")
    #aircraftImageFile =  './feiji/hero.gif'
    #导入飞机图片
    #aircraft = pygame.image.load(aircraftImageFile).convert()
    #飞机图用aircraft保存

while True:
    screen.blit(background,(0,0))
    #设置背景在屏幕的坐标，0.0是左上角的坐标。
    #screen.blit(aircraft,(x,y))
    #设置飞机在屏幕的坐标
    aircraft.display()
    enemy.move()
    enemy.shoot()
    enemy.display()

    for event in pygame.event.get():
        #在发生的事件当中循环，意思可以等同于获取所有的键盘操作
        if event.type == QUIT:
            #判断是否是按下了关闭键
            print("exit")
            exit()
            #退出程序
        elif event.type ==KEYDOWN:
            #判断是否按下了按键
            if event.key == K_a or event.key == K_LEFT:
            #判断是否按下了a键或者左键
                print('左')
                aircraft.moveLeft()
            elif event.key == K_d or event.key == K_RIGHT:
            #判断是否按下了d键或者右键
                print('右')
                aircraft.moveRight()
            elif event.key == K_w or event.key == K_UP:
            #判断是否按下了w键或者上键
                print('上')
                aircraft.moveUp()
            elif event.key == K_s or event.key == K_DOWN:
            #判断是否按下了s键或者下键
                print('下')
                aircraft.moveDown()
            elif event.key == K_SPACE:
            #判断是否按下了空格键
                print('射子弹')
                aircraft.shoot()
    #time.sleep(0.001)
    pygame.display.update()
    #更新屏幕