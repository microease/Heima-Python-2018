def create_num(all_num):
    a, b = 0, 1
    current_num = 0
    while current_num < all_num:
        ret = yield a
        print("aaa",ret)
        a, b = b, a + b
        current_num += 1


obj = create_num(10)
ret = next(obj)
print(ret)
obj.send("aaa")
print(ret)
