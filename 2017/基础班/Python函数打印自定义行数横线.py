'''
def hengxian(n):
	i = 1
	while i<num:
		print("-"*30)
	i+=1
num = int(input("请输入您要打印的横线行数："))
hengxian(num)
'''
def hengxian():
	print("-"*30)
def zidingyi(n):
	i = 0
	while i<n:
		hengxian()
		i+=1
num = int(input("请输入您要打印的横线行数："))
zidingyi(num)