player = int(input("请输入您要出：石头(1)/剪刀(2)/布(3):\n"))
computer = 1
if player == computer:
    print("平局")
elif (player == 1 and computer == 2) or (player == 2 and computer == 3) or (player == 3 and computer == 1):
    print("你赢了")
else:
    print("你输了")

print("玩家出的是%d,电脑出的是%d" % (player, computer))
