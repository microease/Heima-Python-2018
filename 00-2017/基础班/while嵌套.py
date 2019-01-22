#coding=utf-8
i=1
while i<=5:
	j=1
	while j<=i:
		print("*",end="")
		j+=1
	i+=1
while i>0:
	while j>=i:
		print("*",end="")
		j-=1
	i-=1
