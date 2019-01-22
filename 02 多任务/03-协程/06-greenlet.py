from greenlet import greenlet
import time


def test1():
    while True:
        print("a")
        gr2.switch()
        time.sleep(0.1)


def test2():
    while True:
        print("b")
        gr1.switch()
        time.sleep(0.1)


gr1 = greenlet(test1)
gr2 = greenlet(test2)

gr1.switch()
