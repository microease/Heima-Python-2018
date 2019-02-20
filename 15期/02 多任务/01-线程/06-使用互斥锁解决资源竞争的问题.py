import threading
import time

g_num = 0


def test1(num):
    global g_num
    mutex.acquire()
    for i in range(num):
        g_num += 1
    mutex.release()
    print("%d" % g_num)


def test2(num):
    global g_num
    mutex.acquire()
    for i in range(num):
        g_num += 1
    mutex.release()
    print("%d" % g_num)


def main():
    t1 = threading.Thread(target=test1, args=(1000000,))
    t2 = threading.Thread(target=test2, args=(1000000,))
    t1.start()
    t2.start()
    time.sleep(5)
    print("%d" % g_num)


mutex = threading.Lock()

if __name__ == '__main__':
    main()
