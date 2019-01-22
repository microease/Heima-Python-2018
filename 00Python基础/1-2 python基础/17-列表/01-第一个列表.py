name_list = ["zhangsan", "lisi", "wangwu"]
for name in name_list:
    print(name)

name_list.append("aa")
print(name_list)

print(name_list.index("lisi"))

name_list.insert(2, "11")
print(name_list)

temp = ["11"]
name_list.extend(temp)
print(name_list)

name_list.pop()
print(name_list)

print(len(name_list))

name_list.sort()
print(name_list)

name_list.sort(reverse=True)
print(name_list)
