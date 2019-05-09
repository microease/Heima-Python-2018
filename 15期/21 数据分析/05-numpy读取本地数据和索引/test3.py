# coding:utf-8
# File Name：     test3
# Description :
# Author :       huxiaoyi
# Date：          2019-05-09
import numpy as np

t1 = np.arange(12).reshape((3, 4)).astype("float")
t1[1, 2:] = np.nan
print(t1)

for i in range(t1.shape[1]):
    temp_col = t1[:, i]
    np.count_nonzero(temp_col != temp_col)
    if nan
