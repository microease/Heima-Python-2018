# coding:utf-8
# File Name：     test1
# Description :
# Author :       huxiaoyi
# Date：          2019-05-14
import pandas as pd
import numpy as np

file_path = "./directory.csv"
df = pd.read_csv(file_path)
print(df.head(1))
grouped = df.groupby(by="Country")
# print(grouped)
# for i in grouped:
#     print(i)
#     print("*"*80)

country_count = grouped["Brand"].count()
print(country_count["US"])
print(country_count["CN"])
china_data = df[df["Country"] == "CN"]