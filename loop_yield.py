def gen():
    a = 100
    yield a
    a = a * 8
    yield
    yield 1000


for i in gen():
    print i
