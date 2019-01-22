#conding=utf-8 
import random
while True:
	user = int(input("请输入：剪刀0 石头1 布2:"))
	computer = random.randint(0,2)
	print("电脑选的是%d"%computer)
	if user==9:
		break
		if (user==0 and computer==2) or (user==1 and computer==0) or (user==2 and computer==1):
			print ("你赢了！")
	elif user == computer:
		print("平局，重来！")
	else:
		print("你输了！")

