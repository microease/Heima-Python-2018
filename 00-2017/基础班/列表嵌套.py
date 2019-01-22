#coding=utf-8
import random
rooms = [[],[],[]]

teachers = ["A","B","C","D","E","F","G","H"]

for name in teachers:
	randomNum = random.randint(0,2)
	rooms[randomNum].append(name)
i = 1
for room in rooms:
	print("办公室%d里面的老师姓名是："%i)
	for name in room:
		print(name,end=" ")
	print()
	i+=1
	