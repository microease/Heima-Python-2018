# coding:utf-8
# File Name：     test2
# Description :
# Author :       huxiaoyi
# Date：          2019-05-14
import pandas as pd
from matplotlib import pyplot as plt

file_path = "./directory.csv"
df = pd.read_csv(file_path)

# 使用matplotlib 呈现出店铺总数排名前10的国家
data = df.groupby(by="Country").count()['Brand'].sort_values(ascending=False)[:10]
_