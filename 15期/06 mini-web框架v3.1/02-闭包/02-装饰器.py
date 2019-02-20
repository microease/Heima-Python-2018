import time


def set_func(func):
    def call_func():
        start_time = time.time()
        print("这是权限认证1")
        func()
        print("这是权限认证2")
        stop_time = time.time()
        print("%f" % (stop_time - start_time))

    return call_func


@set_func
def test1():
    print("test1")


# ret = set_func(test1)
print("111")

test1()
