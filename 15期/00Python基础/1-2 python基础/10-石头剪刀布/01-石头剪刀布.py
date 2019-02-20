import random
player = int(input("请输入您要出：石头(1)/剪刀(2)/布(3):\n"))
computer = random.randint(1,3)
if player == computer:
    print("平局")
elif player == 1:
    if computer == 2:
        print("你输了")
    else:
        print("你赢了")
elif player == 2:
    if computer == 1:
        print("你输了")
    else:
        print("你赢了")
else:
    if computer == 1:
        print("你赢了")
    else:
        print("你输了")

print("玩家出的是%d,电脑出的是%d" % (player, computer))
