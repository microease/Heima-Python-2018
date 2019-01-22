#coding=utf-8
try:
#	print(a)
	open("abc.txr",'r')
#except (Exception,NameError) as e:
except Exception as e:
	print("产生了一个异常： %s"%e)
finally:
	print("结束了。")