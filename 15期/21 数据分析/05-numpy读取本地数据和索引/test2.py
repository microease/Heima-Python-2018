# coding:utf-8
# File Name：     test2
# Description :
# Author :       microease
# Date：          2019/5/9
import numpy as np

us_file_path = "./USvideos.csv"
gb_file_path = "./GBvideos.csv"
# 加载国家数据
us_data = np.loadtxt(us_file_path, encoding="ISO-8859-1", delimiter=",", dtype="str", unpack=True).astype(int)
uk_data = np.loadtxt(gb_file_path, encoding="ISO-8859-1", delimiter=",", dtype="str", unpack=True).astype(int)
# 构造全为0的数据
zero_data = np.zeros((us_data.shape[0], 1)).astype(int)
ones_data = np.ones((uk_data.shape[0], 1)).astype(int)
us_data = np.hstack((us_data, zero_data))
uk_data = np.hstack((uk_data, ones_data))
# 拼接两组数据
final_data = np.vstack((uk_data,us_data))
print(final_data)
