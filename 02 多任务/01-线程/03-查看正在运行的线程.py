import threading
import time


def test1():
    for i in range(5):
        print("test1---%d" % i)


def test2():
    for i in range(5):
        print("test2--%d" % i)


def main():
    t1 = threading.Thread(target=test1)
    t2 = threading.Thread(target=test2)
    t1.start()
    time.sleep(5)
    t2.start()
    while True:
        print(threading.enumerate())
        time.sleep(1)


if __name__ == '__main__':
    main()
