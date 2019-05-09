# coding:utf-8
# File Name：     test3
# Description :
# Author :       huxiaoyi
# Date：          2019-05-09
import numpy as np


def fill_ndarray(t1):
    for i in range(t1.shape[1]):
        temp_col = t1[:, i]
        nan_num = np.count_nonzero(temp_col != temp_col)  # 当前一列不为nan的array
        if nan_num != 0:
            temp_not_col = temp_col[temp_col == temp_col]
            # 选中当前为nan的位置，把值赋给不为nan的均值
            temp_col[np.isnan(temp_col)] = temp_not_col.mean()
    return t1


if __name__ == '__main__':
    t1 = np.arange(12).reshape((3, 4)).astype("float")
    print(t1)
    t1[1, 2:] = np.nan
    print(t1)
    t1 = fill_ndarray(t1)
    print(t1)
