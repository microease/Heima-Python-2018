# coding:utf-8
# File Name：     test1
# Description :
# Author :       huxiaoyi
# Date：          2019-05-12
import pandas as pd

df = pd.read_csv("./dogNames2.csv")
# print(df.head())
# print(df.info())
df.sort_values(by="Count_AnimalName", ascending=False)
print(df[:20]["Row_Labels"])
