def deco(**kw):
    print kw

    def _deco(func):
        return func

    return _deco


@deco(key="123")
def foo():
    return "hello"


if __name__ == "__main__":
    print foo()