age = int(input("请输入你的年龄：\n"))
if age >= 18:
    print("可以进网吧")
else:
    print("过%d年再来吧" % int(18 - age))
print("什么时候都会执行")
