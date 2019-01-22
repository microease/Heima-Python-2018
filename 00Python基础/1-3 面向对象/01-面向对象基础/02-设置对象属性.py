class Cat:
    def eat(self):
        print("小猫爱吃鱼")

    def drink(self):
        print("小猫要喝水")


tom = Cat()
tom.eat()
tom.drink()
tom.name = "大懒猫"
print(tom)