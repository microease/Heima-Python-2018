import multiprocessing

q = multiprocessing.Queue(3)

q.put("111")
q.put(22)

q.put([1, 2, 2.2])

print(q.get())
print(q.get())
print(q.get())
print(q.get())
