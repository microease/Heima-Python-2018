# coding:utf-8
# File Name：     test1
# Description :
# Author :       huxiaoyi
# Date：          2019-05-12
import pandas as pd
from matplotlib import pyplot as plt
file_path = "./IMDB-Movie-Data.csv"
df = pd.read_csv(file_path)
# print(df.head(1))
# print(df.info())
runtime_data = df["Runtime (Minutes)"].values
max_runtime = runtime_data.max()
min_runtime = runtime_data.min()

# 计算组数
num_bin = (max_runtime-min_runtime)//5

plt.figure(figsize=(20,8),dpi=80)
plt.hist(runtime_data,num_bin)
plt.show()