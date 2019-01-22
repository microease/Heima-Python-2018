def test(num):
	if num>1:
		return num+test(num-1)
	else:
		return 1
result = test(100)
print (result)