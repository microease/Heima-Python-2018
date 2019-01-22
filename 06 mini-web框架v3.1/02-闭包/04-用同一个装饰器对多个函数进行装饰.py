import time


def set_func(func):
    def call_func(num):
        start_time = time.time()
        print("这是权限认证1")
        func(num)
        print("这是权限认证2")
        stop_time = time.time()
        print("%f" % (stop_time - start_time))

    return call_func


@set_func
def test1(num):
    print("test1")


@set_func
def test2(num):
    print("test2")


# ret = set_func(test1)
print("111")

test1(100)
test2(200)
