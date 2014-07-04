func = lambda x, y: x + y


def test(f, a, b):
    print 'test'
    print f(a, b)


test(func, 3, 5)

test((lambda x, y: x ** 2 + y ), 6, 9)