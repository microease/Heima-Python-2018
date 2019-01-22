class Animal:
    def eat(self):
        print("能吃")

    def drink(self):
        print("能喝")

    def run(self):
        print("能跑")

    def sleep(self):
        print("能睡")


class Dog(Animal):
    def bark(self):
        print("能叫")


class XiaoTianQuan(Dog):
    def fly(self):
        print("能飞")

    def bark(self):
        print("神狗叫")
        super().bark()
        print("xxx")


xiaomei = XiaoTianQuan()

xiaomei.bark()
