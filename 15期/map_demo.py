# coding:utf-8
li1 = [1, 2, 3, 4]
li2 = [2, 3, 4, 5]


def add(num1, num2):
    return num1 + num2


ret = map(add, li1, li2)
for i in ret:
    print(i)
