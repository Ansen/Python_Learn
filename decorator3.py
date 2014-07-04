def deco(func):
    print "deco"
    return func


@deco
def foo():
    return "hello"


if __name__ == "__main__":
    pass
    #    print foo()