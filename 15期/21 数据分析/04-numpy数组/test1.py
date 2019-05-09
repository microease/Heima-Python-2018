# coding:utf-8
# File Name：     test1
# Description :
# Author :       microease
# Date：          2019/5/8
import numpy as np

t1 = np.arange(12)
print(t1)
print(type(t1))
print(t1.dtype)

t2 = np.array(range(1,4),dtype=float)
print(t2)
print(t2.dtype)
t2 = t2.astype("int8")
print(t2.dtype)