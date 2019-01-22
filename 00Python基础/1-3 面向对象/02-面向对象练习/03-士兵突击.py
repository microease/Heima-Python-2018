class Gun:
    def __init__(self, model):
        self.model = model
        self.bullet_count = 0

    def add_bullet(self, count):
        self.bullet_count += count

    def shoot(self):
        if self.bullet_count <= 0:
            print("%s没有子弹了" % self.model)
            return
        self.bullet_count -= 1
        print("突突突，%s正在发射子弹，还剩%d" % (self.model, self.bullet_count))


class Soldier:
    def __init__(self, name):
        self.name = name
        self.gun = None

    def fire(self):
        if self.gun == None:
            print("%s 还没有枪" % self.name)
            return
        print("冲啊。。%s" % self.name)
        self.gun.add_bullet(50)
        self.gun.shoot()


AK47 = Gun("AK47")

xusanduo = Soldier("许三多")
xusanduo.gun = AK47
xusanduo.fire()
print(xusanduo.gun)
