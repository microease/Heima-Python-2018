#coding=utf-8
#如果 a+b+c=1000，且 a^2+b^2=c^2（a,b,c 为自然数），如何求出所有a、b、c可能的组合?
import time
startTime = time.time()
print(startTime)
for a in range(0,1001):
    for b in range(0,1001):
        for c in range(0,1001):
            if a + b + c == 1000 and a**2 + b**2 == c**2:
                print("a,b,c:%d,%d,%d"%(a,b,c))
endTime = time.time()
print(endTime)
print("总共消耗时间：%f"%(endTime-startTime))
print("hello,huyankai")
#这个程序让我的Mac风扇狂转。。
# a,b,c:0,500,500
# a,b,c:200,375,425
# a,b,c:375,200,425
# a,b,c:500,0,500
# 1527447514.7960682
# 总共消耗时间：203.880976
# hello,huyankai