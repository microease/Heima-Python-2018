try:
    num = int(input("输入一个整数："))
    result = 8 / num
    print(result)
except Exception as result:
    print("%s错误" % result)
else:
    print("没错误")
finally:
    print("有错1没错都执行")