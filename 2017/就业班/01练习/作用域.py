num = 100
def test1():
	num = 200
	def test2():
		num = 300
		print(num)
	return test2

ret = test1()
ret()