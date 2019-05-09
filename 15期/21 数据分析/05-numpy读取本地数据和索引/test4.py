# coding:utf-8
# File Name：     test4
# Description :
# Author :       huxiaoyi
# Date：          2019-05-09
import numpy as np
from matplotlib import pyplot as plt

us_file_path = "./USvideos.csv"
gb_file_path = "./GBvideos.csv"
# category_id	views	likes	dislikes	comment_total
us_data = np.loadtxt(us_file_path, encoding="ISO-8859-1", delimiter=",", dtype="str")
t_us_comments = us_data[:, -1].astype(int)
print(t_us_comments.max(), t_us_comments.min())
d = 100000
bin_nums = (t_us_comments.max() - t_us_comments.min()) // d
plt.figure(figsize=(20, 8), dpi=80)
plt.hist(t_us_comments, bin_nums)
plt.show()
