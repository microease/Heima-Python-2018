# coding:utf-8
# File Name：     test2
# Description :
# Author :       microease
# Date：          2019/5/6

from matplotlib import pyplot as plt
import random
import matplotlib
from matplotlib import font_manager

font = {
    'family': 'MicroSoft YaHei',
    'weight': 'bold',
    'size': 'larger'
}
matplotlib.rc(font)
my_font = font_manager.FontProperties(fname="C:\Windows\Fonts\msyh.ttc")

fig = plt.figure(figsize=(20, 8), dpi=80)

x = range(0, 120)
y = [random.randint(20, 35) for i in range(120)]

plt.plot(x, y)

_xticks_labels = ["10点{}分".format(i) for i in range(60)]
_xticks_labels += ["11点{}分".format(i) for i in range(60)]

plt.xlabel('时间', fontproperties=my_font)
plt.ylabel("温度 单位℃", fontproperties=my_font)
plt.title('10点到12点每分钟气温变化', fontproperties=my_font)
plt.xticks(list(x)[::3], _xticks_labels[::3], rotation=90, fontproperties=my_font)

plt.show()
