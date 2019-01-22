name_list = ("zhangsan", 11, 0.822, False)
for name in name_list:
    print(name)

name1 = name_list.index("zhangsan")
print(name1)

print(list(name_list))
print(tuple(list(name_list)))