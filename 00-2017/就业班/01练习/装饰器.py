'''
无参数
def  func(functionName):
	print("-----func-----1------")
	def func_in():
		print("-----func_in-----1------")
		functionName()
		print("-----func_in-----2------")
	print("-----func-----2-----")
	return func_in

def test():
	print("-----test-----")

test = func(test)

test()
'''
#有参数  
def func(functionName):
	print("-----func-----1------")
	def func_in(a,b):
		print("-----func_in-----1------")
		functionName()
		print("-----func_in-----2------")
	print("-----func-----2-----")
	return func_in
@func
def test(a,b):
	print("-----test-a=%d,b=%d-----"%(a,b))

#test = func(test)

test(11,22)