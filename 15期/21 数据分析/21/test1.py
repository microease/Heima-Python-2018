# coding:utf-8
# File Name：     test1
# Description :
# Author :       huxiaoyi
# Date：          2019-05-16
import pandas as pd
from
file_path = "./BeijingPM20100101_20151231.csv"

df = pd.read_csv(file_path)

print(df.head())
print(df.info())

period = pd.PeriodIndex(year=df["year"], month=df["month"],day = df["day"],hour = df["hour"],freq = "H")

df["datetime"] = period

df.set_index("datetime",inplace = True)

date = df["PM_US Post"].dropna()
