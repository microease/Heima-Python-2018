price_str = input("请输入苹果单价：\n")

weight_str = input("请输入苹果重量：\n")
money = float(price_str) * float(weight_str)
print("您购买的苹果价值" + str(money))
print("格式化字符串：单价%s,重量%s,%s" % (price_str, weight_str, money))
