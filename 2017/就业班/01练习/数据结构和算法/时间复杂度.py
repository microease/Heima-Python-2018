#coding=utf-8
#如果 a+b+c=1000，且 a^2+b^2=c^2（a,b,c 为自然数），如何求出所有a、b、c可能的组合?
import time
startTime = time.time()
print(startTime)
for a in range(0,1001):
    for b in range(0,1001):
        c = 1000 - a -b
        if a**2 + b**2 == c**2:
            print("a,b,c:%d,%d,%d"%(a,b,c))
#T代表时间复杂度
T = 1000 * 1000 * 1000 * 2
T = N * N * N * 2
T(n) = n^3 * 2
g(n) = n^3

T(n) = n * n * (1 + (1,0))
T(n) = n^2 *2
T(n) = O(n^2)
endTime = time.time()
print(endTime)
print("总共消耗时间：%f"%(endTime-startTime))
print("hello,huyankai")
#稍微优化了一下程序，Mac的风扇也不会狂转了，原因是第一，减少了第三次的循环判断C的值，当a和b的值确定以后，c的值就已经确定了。
#而且也不用判断a+b+c=1000
# a,b,c:0,500,500
# a,b,c:200,375,425
# a,b,c:375,200,425
# a,b,c:500,0,500
# 1527453224.260499
# 总共消耗时间：1.295151
# hello,huyankai