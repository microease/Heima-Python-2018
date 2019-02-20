class Personal:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __str__(self):
        return "我的名字叫%s,体重是%.2f公斤" % (self.name, self.weight)

    def run(self):
        print("%s可以跑步"%self.name)
        self.weight -=0.5

    def eat(self):
        print("%s可以吃东西"%self.weight)
        self.weight +=0.5

xiaoming = Personal("小明",75.0)
xiaoming.run()
xiaoming.eat()
print(xiaoming)