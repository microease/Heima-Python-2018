# coding:utf-8
# File Name：     002条形图
# Description :
# Author :       microease
# Date：          2019/5/7
from matplotlib import pyplot as plt
from matplotlib import font_manager

my_font = font_manager.FontProperties(fname="C:\Windows\Fonts\msyh.ttc")

a = ["战狼2", "流浪地球", "复仇者联盟4：终局之战", "红海行动", "美人鱼", "唐人街探案2", "我不是药神", "速度与激情8", "西虹市首富", "速度与激情7", "捉妖记", "复仇者联盟3：无限战争",
     "捉妖记2", "羞羞的铁拳", "疯狂的外星人", "海王", "变形金刚4：绝迹重生", "前任3：再见前任", "毒液：致命守护者", "功夫瑜伽", ]
b = [56.39, 46.18, 38.85, 36.22, 33.9, 33.71, 30.75, 26.49, 25.27, 24.26, 24.21, 23.7, 22.19, 21.9, 21.83, 19.97, 19.79,
     19.26, 18.56, 17.53]
# 设置图形大小
plt.figure(figsize=(20,8),dpi=80)
plt.bar(range(len(a)), b,width=0.3)
# 设置字符到x轴
plt.xticks(range(len(a)),a, fontproperties=my_font, rotation=90)
plt.savefig('./movie.png')
plt.show()
