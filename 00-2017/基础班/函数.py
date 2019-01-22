#coding=utf-8
def sumNums(a,b,c):
	result = a+b+c
	print ("%d+%d+%d=%d"%(a,b,c,result))
	return result
def averageNums(a1,b1,c1):
	result = sumNums(a1,b1,c1)
	result = result/3
	print("%d"%result)

num1 = int(input("第一个值："))
num2 = int(input("第二个值："))
num3 = int(input("第三个值："))
averageNums(num1,num2,num3)