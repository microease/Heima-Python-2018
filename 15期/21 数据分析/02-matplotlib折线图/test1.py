# coding:utf-8
# File Name：     test1
# Description :
# Author :       microease
# Date：          2019/5/6

from matplotlib import pyplot as plt

fig = plt.figure(figsize=(20, 8), dpi=80)
x = range(2, 26, 2)

y = [15, 13, 14.5, 17, 20, 25, 26, 26, 24, 22, 18, 15]
# 绘图
plt.plot(x, y)
# 设置x轴的刻度
plt.xticks(range(2, 25))
# 保存
plt.savefig("./sig_size.png")
# 展示图形
plt.show()
