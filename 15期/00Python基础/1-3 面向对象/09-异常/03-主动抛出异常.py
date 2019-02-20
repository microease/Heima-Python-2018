def input_password():
    password = input("请输入你的密码：")
    if len(password) > 8:
        return password
    print("主动抛出异常")
    ex = Exception("密码长度不足8位")
    raise ex


try:
    print(input_password())
except Exception as result:
    print(result)
