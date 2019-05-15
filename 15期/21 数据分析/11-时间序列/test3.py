# coding:utf-8
# File Name：     test3
# Description :
# Author :       huxiaoyi
# Date：          2019-05-15
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

df = pd.read_csv("./911.csv")

print(df.head(5))
df["timeStamp"] = pd.to_datetime(df["timeStamp"])

df.set_index("timeStamp", inplace=True)
print(df.head(10))
count_by_month = df.resample("M").count()
print(count_by_month)

_x = count_by_month.index
_y = count_by_month.values
plt.figure(figsize=(20,8),dpi=80)

plt.plot(range(len(_x)), _y)
plt.xticks(range(len(_x)), _x, rotation=45)
plt.show()
