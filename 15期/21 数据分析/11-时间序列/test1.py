# coding:utf-8
# File Name：     test1
# Description :
# Author :       microease
# Date：          2019/5/15
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

df = pd.read_csv("./911.csv")
# print(df.head(10))
# print(df.info())
# print(df["title"].str.split(": "))
temp_list = df["title"].str.split(": ").to_list()
cate_list = list(set([i[0] for i in temp_list]))
print(cate_list)
# 构造全为0的数组
zero_df = pd.DataFrame(np.zeros(df.shape[0], len(cate_list)), columns=cate_list)
for cate in cate_list:
    zero_df[cate][df["title"].str.contains(cate)] = 1
    print(zero_df)
