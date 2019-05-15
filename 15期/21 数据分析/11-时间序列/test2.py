# coding:utf-8
# File Name：     test1
# Description :
# Author :       microease
# Date：          2019/5/15
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

df = pd.read_csv("./911.csv")
print(df.head(5))

temp_list = df["title"].str.split(": ").to_list()
cate_list = [i[0] for i in temp_list]

df["cate"] = pd.DataFrame(np.array(cate_list).reshape((df.shape[0], 1)))
print(df.groupby(by="cate").count()["title"])