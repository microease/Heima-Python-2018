# coding:utf-8
# File Name：     test3
# Description :
# Author :       microease
# Date：          2019/5/6
from matplotlib import pyplot as plt
from matplotlib import font_manager

x = [1, 0, 1, 1, 2, 4, 3, 2, 3, 4, 4, 5, 6, 5, 4, 3, 3, 1, 1, 1]
y = range(11, 31)
my_font = font_manager.FontProperties(fname="/System/Library/Fonts/PingFang.ttc")

# 设置图形大小
plt.figure(figsize=(20, 8), dpi=8)

plt.plot(x, y)

# 设置X轴刻度
_xtick_labels = ["{}岁".format(i) for i in x]
plt.xticks(x, _xtick_labels, fontproperties=my_font)

# 展示
plt.show()
