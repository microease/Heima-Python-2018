import multiprocessing


def test1(q):
    data = [11, 22, 33, 44, 55]
    for temp in data:
        q.put(temp)
    print("列表全部放进去了") 


def test2(q):
    waiting = []
    while True:
        data = q.get()
        waiting.append(data)
        if q.empty():
            break
    print(waiting)


def main():
    q = multiprocessing.Queue()
    p1 = multiprocessing.Process(target=test1, args=(q,))
    p2 = multiprocessing.Process(target=test2, args=(q,))
    p1.start()
    p2.start()


if __name__ == '__main__':
    main()
