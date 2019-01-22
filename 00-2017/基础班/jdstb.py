#conding=utf-8 
inport random;
user = int(input(请输入：剪刀0 石头1 布2))
computer = random.randint(0,2)
print("电脑选的是%d"%computer)

if (user > computer) or (user == 0 and computer == 2):
	print ("你赢了！")
elif user == conputer:
	print("平局，重来！")
else:
	print("你输了！")

