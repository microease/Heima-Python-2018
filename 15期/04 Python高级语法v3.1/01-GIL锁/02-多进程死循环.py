import multiprocessing


def test():
    while True:
        pass


t1 = multiprocessing.Process(target=test)
t1.start()
while True:
    pass
