class Cat:
    def __init__(self, new_name):
        self.name = new_name
        print("%s来了" % self.name)

    def __del__(self):
        print("%s我去了" % self.name)

    def __str__(self):
        return "我是小猫"

tom  = Cat("Tom")
print(tom)
print(tom)
print(tom)