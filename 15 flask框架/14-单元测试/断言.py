# coding=utf-8
def num_div(num1, num2):
    assert isinstance(num1, int)
    assert isinstance(num2, int)
    assert num2 != 0
    print(num1 / num2)


num_div(50, 1000)

num_div(3, 1000)
num_div(3, 0)
