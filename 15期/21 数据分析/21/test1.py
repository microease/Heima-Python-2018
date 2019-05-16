# coding:utf-8
# File Name：     test1
# Description :
# Author :       huxiaoyi
# Date：          2019-05-16
import pandas as pd
from matplotlib import pyplot as plt

file_path = "./BeijingPM20100101_20151231.csv"

df = pd.read_csv(file_path)

print(df.head())
print(df.info())

period = pd.PeriodIndex(year=df["year"], month=df["month"], day=df["day"], hour=df["hour"], freq="H")

df["datetime"] = period

df.set_index("datetime", inplace=True)
df = df.resample("7D").mean()
date = df["PM_US Post"].dropna()
date_china = df["PM_Dongsi"].dropna()
# 画图
_x = date.index
_x = [i.strftime("%Y%m%d") for i in _x]
_x_china = [i.strftime("%Y%m%d") for i in date_china.index]
_y = date.values
_y_china = date_china.values

plt.figure(figsize=(20, 8), dpi=80)

plt.plot(range(len(_x)), _y,label="US_POST")
plt.plot(range(len(_x_china)),_y_china,label="CN_POST")
plt.xticks(range(0, len(_x), 20), list(_x)[::20], rotation=45)
plt.legend(loc="best")
plt.show()
