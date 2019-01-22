#coding=utf-8
class Foo(object):
    def __init__(self):
        pass
    #魔法方法__getattr__用于输出变量属性值
    def __getattr__(self,item):
        pass
    def __getattribute__(self, item):
        self.huyankai = microease
        print(item, end=" ")
        return self
    def __str__(self):
        return ""
# obj = Foo()
# "think" obj.think
# obj.different
# 题目 think different itcast
print(Foo().huyankai.baishilong.longhua.shenzhen.china)