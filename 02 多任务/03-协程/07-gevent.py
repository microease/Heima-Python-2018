import gevent
from gevent import monkey
import time

monkey.patch_all()


def f(n):
    for i in range(n):
        print(gevent.getcurrent(), i)


g1 = gevent.spawn(f, 5)
print("1")
g2 = gevent.spawn(f, 5)
print("2")

g3 = gevent.spawn(f, 5)
print("3")

g1.join()
g2.join()
g3.join()
