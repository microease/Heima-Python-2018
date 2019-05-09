# coding:utf-8
# File Name：     test1
# Description :
# Author :       microease
# Date：          2019/5/9
import numpy as np

us_file_path = "./USvideos.csv"
gb_file_path = "./GBvideos.csv"
# category_id	views	likes	dislikes	comment_total
t1 = np.loadtxt(us_file_path, encoding="ISO-8859-1", delimiter=",", dtype="str", unpack=True)
print(t1)
