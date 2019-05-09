# coding:utf-8
# File Name：     test5
# Description :
# Author :       huxiaoyi
# Date：          2019-05-09
import numpy as np
from matplotlib import pyplot as plt

us_file_path = "./USvideos.csv"
gb_file_path = "./GBvideos.csv"
# category_id	views	likes	dislikes	comment_total
us_data = np.loadtxt(us_file_path, encoding="ISO-8859-1", delimiter=",", dtype="int")
us_data = us_data[us_data[:, 2] <= 2000]
t_us_comments = us_data[:, -1]
t_us_likes = us_data[:, 2]
plt.figure(figsize=(20, 8), dpi=80)
plt.scatter(t_us_likes, t_us_comments)
plt.show()
