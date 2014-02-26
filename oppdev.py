class SampleMore(object):
    def __call__(self, a):
        return a+5

add = SampleMore()
print(add(2))
map(add, [2, 4, 5])